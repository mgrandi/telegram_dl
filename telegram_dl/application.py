import logging
import asyncio
import concurrent.futures
import functools

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from telegram_dl import tdlib
from telegram_dl import utils
from telegram_dl import handlers
from telegram_dl import tdlib_generated
from telegram_dl import input
from telegram_dl import config, constants
from telegram_dl import db_actions

logger = logging.getLogger(__name__)


message_archive_logger = logging.getLogger(constants.MESSAGE_ARCHIVE_LOGGER_NAME)
task_logger = logger.getChild("task")
logic_task_logger = task_logger.getChild("LogicTask")
send_messages_to_tl_logger = task_logger.getChild("SendMessagesToTelegramTask")
receive_messages_from_tl_logger = task_logger.getChild("ReceiveMessagesFromTelegramTask")
process_messages_from_tl_logger = task_logger.getChild("ProcessMessagesFromTelegram")
database_task_logger = task_logger.getChild("DatabaseTask")

database_task_action_logger = database_task_logger.getChild("actions")



class Application:
    '''
    main application class
    '''

    def __init__(self, args):
        ''' constructor
        @param args - the namespace object we get from argparse.parse_args()
        '''

        self.args = args

        self.message_handler = handlers.TdlibBaseMessageHandler(handlers.AuthorizationHandler(input.TTYInput()))

        self.dbaction_handler = db_actions.DbActionHandler()

        # load config stuff
        logger.info("creating TdlibConfiguration")
        self.app_config = config.ApplicationConfiguration.init_from_config(self.args.config)

        logger.info("creating engine")

        self.engine = create_engine(self.app_config.sqlalchemy_url, echo=False)
        self.sessionmaker = sessionmaker(bind=self.engine)

        # NOTE: you NEED to create these inside a running loop or else it will use
        # `asyncio.get_event_loop()` which is not the same loop that `asyncio.run()` uses
        self.to_telegram_queue = None
        self.from_telegram_queue = None
        self.database_queue = None
        self.stop_event = None

    def should_stop_loop(self):
        return self.stop_event.is_set()

    async def run(self):

        from telegram_dl import tdlib_generated as tdg

        self.to_telegram_queue = asyncio.Queue()
        self.from_telegram_queue = asyncio.Queue()
        self.database_queue = asyncio.Queue()
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
        self.tdlib_handle.execute(set_log_stream_obj, without_client_ok=True)

        # create tdlib client
        logger.info("creating TDLib client")
        self.tdlib_handle = self.tdlib_handle.create_client()


        logger.info("Starting tasks")


        recieve_messages_task_notstarted = ReceiveMessagesFromTelegramTask(self.stop_event, self.tdlib_handle, self.from_telegram_queue)
        receive_message_task = asyncio.create_task(recieve_messages_task_notstarted.run(), name="ReceiveMessagesFromTelegramTask")

        process_messages_task_notstarted = ProcessMessagesFromTelegram(self.stop_event, self.tdlib_handle, self.from_telegram_queue, self.to_telegram_queue, self.database_queue, self.message_handler)
        process_message_task = asyncio.create_task(process_messages_task_notstarted.run(), name="ProcessMessagesFromTelegram")

        send_messages_task_notstarted = SendMessagesToTelegramTask(self.stop_event, self.tdlib_handle, self.to_telegram_queue)
        send_messages_task = asyncio.create_task(send_messages_task_notstarted.run(), name="SendMessagesToTelegramTask")

        database_task_notstarted = DatabaseTask(self.stop_event, self.database_queue, self.sessionmaker, self.dbaction_handler)
        database_task = asyncio.create_task(database_task_notstarted.run(), name="DatabaseTask")

        logic_task_notstarted = LogicTask(self.stop_event, self.to_telegram_queue)
        logic_task = asyncio.create_task(logic_task_notstarted.run(), name="LogicTask")

        all_tasks = [receive_message_task, process_message_task, send_messages_task, database_task, logic_task]

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



class LogicTask:

    def __init__(self, stop_event, to_telegram_queue):

        self.stop_event = stop_event
        self.to_telegram_queue = to_telegram_queue

        self.temp = True


    async def run(self):


        # TODO: SOMEHOW need to figure out when the tdlibParameters have been sent and we can send messages

        await asyncio.sleep(5)
        while not self.stop_event.is_set():

            logic_task_logger.debug("loop iteration")

            if self.temp:

                import uuid


                x = tdlib_generated.getChats(extra=uuid.uuid4(), offset_order=0, offset_chat_id=0, limit=1000)



                logic_task_logger.info("sending get chat message: `%s`", x)

                self.temp = False
                self.to_telegram_queue.put_nowait(x)
            else:


                await asyncio.sleep(5)


        logic_task_logger.info("stop event is set, returning")

class DatabaseTask:

    def __init__(self, stop_event, db_input_queue, sqla_sessionmaker, dbaction_handler):

        self.stop_event = stop_event
        self.db_input_queue = db_input_queue
        self.sqla_sessionmaker = sqla_sessionmaker
        self.dbaction_handler = dbaction_handler


    async def run(self):

        while not self.stop_event.is_set():

            database_task_logger.debug("loop iteration")


            try:
                result_obj = await asyncio.wait_for(self.db_input_queue.get(), constants.PROCESS_MESSAGE_QUEUE_TIMEOUT)


                session = self.sqla_sessionmaker()

                try:

                    database_task_logger.debug("got object: `%s`, sending to single dispatch")
                    await self.dbaction_handler.handle_database_action(result_obj, session)


                    session.commit()

                except Exception as e:

                    database_task_logger.exception("Uncaught exception with database action, rolling back session")
                    session.rollback()
                    raise e

                finally:

                    database_task_logger.debug("closing session")
                    session.close()

                database_task_logger.debug("object handled successfully, marking queue object as done")
                self.db_input_queue.task_done()


            except asyncio.TimeoutError as e:

                continue

            except Exception as e:

                database_task_logger.exception("uncaught exception!")

        database_task_logger.info("stop event is set, returning")


class SendMessagesToTelegramTask:

    def __init__(self, stop_event, tdlib_handle, to_telegram_queue):
        self.stop_event = stop_event
        self.tdlib_handle = tdlib_handle
        self.to_telegram_queue = to_telegram_queue


    async def run(self):

        with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:

            while not self.stop_event.is_set():
                send_messages_to_tl_logger.debug("loop iteration")


                try:
                    result_obj = await asyncio.wait_for(self.to_telegram_queue.get(), constants.PROCESS_MESSAGE_QUEUE_TIMEOUT)

                    send_messages_to_tl_logger.debug("got object from queue: `%s`, (queue size is now `%s`)",
                        result_obj, self.to_telegram_queue.qsize())


                    # TODO: make tdlib receive act like a real coroutine and have a timeout error when it timeouts?
                    # and put this executor stuff in tdlib.py

                    # send message to telegram
                    result_obj_from_receive = await asyncio.get_running_loop().run_in_executor(
                        thread_pool_executor, self.tdlib_handle.send, result_obj)

                    send_messages_to_tl_logger.debug("send successful")
                    self.to_telegram_queue.task_done()


                except asyncio.TimeoutError as e:

                    continue

                except Exception as e:

                    send_messages_to_tl_logger.exception("uncaught exception!")

            send_messages_to_tl_logger.info("stop event is set, returning")


class ReceiveMessagesFromTelegramTask:

    def __init__(self, stop_event, tdlib_handle, from_telegram_queue):
        self.stop_event = stop_event
        self.tdlib_handle = tdlib_handle
        self.from_telegram_queue = from_telegram_queue

    async def run(self):

        # we need this as the tdlib json library blocks and there is no way to
        # use async/await on those ctypes calls, so by default this task will just
        # run forever and never give any of the other tasks a chance to run
        # so we run the tdlib json ctypes calls in a separate executor that is
        # on a different thread, so that way it doesn't block any of the other tasks
        with concurrent.futures.ThreadPoolExecutor() as thread_pool_executor:
            while not self.stop_event.is_set():

                try:
                    receive_messages_from_tl_logger.debug("loop iteration")

                    # TODO: make tdlib receive act like a real coroutine and have a timeout error when it timeouts?
                    # and put this executor stuff in tdlib.py
                    result_obj_from_receive = await asyncio.get_running_loop().run_in_executor(
                        thread_pool_executor, self.tdlib_handle.receive)

                    receive_messages_from_tl_logger.debug("recieved something from receive: `%s`", result_obj_from_receive)

                    # log the raw message from telegram
                    if result_obj_from_receive is not None:
                        message_archive_logger.info("%s", result_obj_from_receive)

                    if not result_obj_from_receive:
                        receive_messages_from_tl_logger.debug("tdjson_receive timed out and returned None, not sending to singledispatch method")
                        continue

                    # put message into our queue
                    # NOTE assuming this queue is infinite or very large so don't use the coroutine version for now
                    self.from_telegram_queue.put_nowait(result_obj_from_receive)

                    receive_messages_from_tl_logger.debug("added message to queue, queue size is now `%s`", self.from_telegram_queue.qsize())

                except Exception as e:

                    receive_messages_from_tl_logger.exception("uncaught exception!")

            receive_messages_from_tl_logger.info("stop event is set, returning")


class ProcessMessagesFromTelegram:

    def __init__(self, stop_event, tdlib_handle, from_telegram_queue, to_telegram_queue, database_queue, message_handler):
        self.stop_event = stop_event
        self.tdlib_handle = tdlib_handle
        self.from_telegram_queue = from_telegram_queue
        self.to_telegram_queue = to_telegram_queue
        self.database_queue = database_queue

        self.message_handler = message_handler


    async def run(self):

        while not self.stop_event.is_set():

            process_messages_from_tl_logger.debug("loop iteration")

            # FIXME should i regenerate this every time or cache it?
            handler_params =  handlers.HandlerParameters(
                tdlib_handle=self.tdlib_handle,
                to_telegram_queue=self.to_telegram_queue,
                database_queue=self.database_queue)

            try:
                result_obj = await asyncio.wait_for(self.from_telegram_queue.get(), constants.PROCESS_MESSAGE_QUEUE_TIMEOUT)

                process_messages_from_tl_logger.debug("got object from queue: `%s`, (queue size is now `%s`),  calling single dispatch handler",
                    result_obj, self.from_telegram_queue.qsize())
                handle_result = await self.message_handler.handle_message(result_obj, handler_params)

                process_messages_from_tl_logger.debug("handle result is: `%s`", handle_result)

                self.from_telegram_queue.task_done()

            except asyncio.TimeoutError as e:

                continue

            except Exception as e:

                process_messages_from_tl_logger.exception("uncaught exception!")

        process_messages_from_tl_logger.info("stop event is set, returning")
