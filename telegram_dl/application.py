import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from telegram_dl import tdlib
from telegram_dl import utils
from telegram_dl import handlers
from telegram_dl import tdlib_generated
from telegram_dl import input
from telegram_dl import config

logger = logging.getLogger(__name__)

loop_logger = logger.getChild("loop")

class Application:
    '''
    main application class
    '''

    def __init__(self, args):
        ''' constructor
        @param args - the namespace object we get from argparse.parse_args()
        '''

        self.args = args

        self.please_stop = False

        self.message_handler = handlers.TdlibBaseMessageHandler(input.TTYInput(), handlers.AuthorizationHandler())

        # load config stuff
        logger.info("creating TdlibConfiguration")
        self.app_config = config.ApplicationConfiguration.init_from_config(self.args.config)

        logger.info("creating engine")

        self.engine = create_engine(self.app_config.sqlalchemy_url, echo=False)
        self.sessionmaker = sessionmaker(bind=self.engine)

    def should_stop_loop(self):
        return self.please_stop

    async def run(self):

        from telegram_dl import tdlib_generated as tdg

        # register Ctrl+C/D/whatever signal
        def _please_stop_loop_func():
            self.please_stop = True

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


        loop_logger.info("Starting main loop")

        # FIXME should i regenerate this every time or cache it?
        handler_params =  handlers.HandlerParameters(tdlib_handle=self.tdlib_handle)

        # main loop
        # TODO: might need to make this a asyncio.Task!
        while True:
            loop_logger.debug("loop iteration")

            # handle if the user wants to stop
            if self.should_stop_loop():
                loop_logger.info("Stopping main loop")
                break

            result_obj_from_receive = await self.tdlib_handle.receive()

            loop_logger.debug("recieved something from receive: `%s`", result_obj_from_receive)

            if not result_obj_from_receive:
                logger.debug("tdjson_receive timed out and returned None, not sending to singledispatch method")
                continue

            loop_logger.debug("calling singledispatch handler")
            handle_result = await self.message_handler.handle_message(result_obj_from_receive, handler_params)

            loop_logger.debug("handle result is: `%s`", handle_result)


        loop_logger.info("Main loop finished")
        # destroy tdlib client
        logger.info("destroying tdlib handle")
        self.tdlib_handle = self.tdlib_handle.destroy_client()
        logger.info("tdlib handle destroyed successfully")

