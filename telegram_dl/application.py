import logging
import asyncio
import concurrent.futures

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from telegram_dl import tdlib
from telegram_dl import utils
from telegram_dl import handlers
from telegram_dl import tdlib_generated
from telegram_dl import input
from telegram_dl import config, constants

logger = logging.getLogger(__name__)

task_logger = logger.getChild("task")
receive_message_logger = task_logger.getChild("ReceiveMessageTask")
process_message_logger = task_logger.getChild("ProcessMessageTask")

class Application:
    '''
    main application class
    '''

    def __init__(self, args):
        ''' constructor
        @param args - the namespace object we get from argparse.parse_args()
        '''

        self.args = args



        self.message_handler = handlers.TdlibBaseMessageHandler(input.TTYInput(), handlers.AuthorizationHandler())

        # load config stuff
        logger.info("creating TdlibConfiguration")
        self.app_config = config.ApplicationConfiguration.init_from_config(self.args.config)

        logger.info("creating engine")

        self.engine = create_engine(self.app_config.sqlalchemy_url, echo=False)
        self.sessionmaker = sessionmaker(bind=self.engine)

        # NOTE: you NEED to create these inside a running loop or else it will use
        # `asyncio.get_event_loop()` which is not the same loop that `asyncio.run()` uses
        self.message_queue = None
        self.stop_event = None

    def should_stop_loop(self):
        return self.stop_event.is_set()

    async def run(self):

        from telegram_dl import tdlib_generated as tdg

        self.message_queue = asyncio.Queue()
        self.stop_event = asyncio.Event()

        # register Ctrl+C/D/whatever signal
        def _please_stop_loop_func():
            self.stop_event.set()

        utils.register_ctrl_c_signal_handler(_please_stop_loop_func)


        logger.info("creating TdlibHandle")
        self.tdlib_handle = await tdlib.TdlibHandle.init_from_config(self.app_config)

        # change log settings
        log_stream_file_obj = tdg.logStreamFile(
                path=self.tdlib_handle.tdlib_config.tdlib_log_file_path,
                max_file_size=10000000)
        set_log_stream_obj = tdlib_generated.setLogStream(log_stream=log_stream_file_obj, extra=utils.new_extra())

        logger.info("setting TDLib log file path: `%s`", set_log_stream_obj)
        await self.tdlib_handle.execute(set_log_stream_obj, without_client_ok=True)

        # create tdlib client
        logger.info("creating TDLib client")
        self.tdlib_handle = await self.tdlib_handle.create_client()


        logger.info("Starting tasks")


        rmt = ReceiveMessageTask(self.stop_event, self.tdlib_handle, self.message_queue)
        receive_message_task = asyncio.create_task(rmt.run())

        pmt = ProcessMessageTask(self.stop_event, self.tdlib_handle, self.message_queue, self.message_handler)
        process_message_task = asyncio.create_task(pmt.run())

        all_tasks = [receive_message_task, process_message_task]

        logger.info("created tasks: `%s`", all_tasks)

        # now wait for the stop event
        logger.info("waiting for stop event...")
        await self.stop_event.wait()

        logger.info("stop event received")

        # wait for all the tasks to finish
        logger.info("waiting for tasks to finish")
        await asyncio.gather(*all_tasks)

        logger.info("all tasks finished")

        # destroy tdlib client
        logger.info("destroying tdlib handle")
        self.tdlib_handle = self.tdlib_handle.destroy_client()
        logger.info("tdlib handle destroyed successfully")


class ReceiveMessageTask:

    def __init__(self, stop_event, tdlib_handle, message_queue):
        self.stop_event = stop_event
        self.tdlib_handle = tdlib_handle
        self.message_queue = message_queue


    async def run(self):

        while not self.stop_event.is_set():

            receive_message_logger.debug("loop iteration")

            # TODO: make tdlib receive act like a real coroutine and have a timeout error when it timeouts?
            result_obj_from_receive = await self.tdlib_handle.receive()

            receive_message_logger.debug("recieved something from receive: `%s`", result_obj_from_receive)

            if not result_obj_from_receive:
                logger.debug("tdjson_receive timed out and returned None, not sending to singledispatch method")
                continue

            # put message into our queue
            # NOTE assuming this queue is infinite or very large so don't use the coroutine version for now
            self.message_queue.put_nowait(result_obj_from_receive)

            logger.debug("added message to queue, queue size is now `%s`", self.message_queue.qsize())

            receive_message_logger.info("stop event is set, returning")


class ProcessMessageTask:

    def __init__(self, stop_event, tdlib_handle, message_queue, message_handler):
        self.stop_event = stop_event
        self.tdlib_handle = tdlib_handle
        self.message_queue = message_queue
        self.message_handler = message_handler


    async def run(self):

        while not self.stop_event.is_set():

            process_message_logger.debug("loop iteration")

            # FIXME should i regenerate this every time or cache it?
            handler_params =  handlers.HandlerParameters(tdlib_handle=self.tdlib_handle)

            try:
                result_obj = await asyncio.wait_for(self.message_queue.get(), constants.PROCESS_MESSAGE_QUEUE_TIMEOUT)

                try:
                    process_message_logger.debug("got object from queue: `%s`, (queue size is now `%s`),  calling single dispatch handler",
                        result_obj, self.message_queue.qsize())
                    handle_result = await self.message_handler.handle_message(result_obj, handler_params)

                    process_message_logger.debug("handle result is: `%s`", handle_result)
                finally:
                    self.message_queue.task_done()

            except asyncio.TimeoutError as e:

                continue
        process_message_logger.info("stop event is set, returning")
