import logging
import signal

from telegram_dl import tdlib
from telegram_dl import utils
from telegram_dl import tdlib_generated

logger = logging.getLogger(__name__)


class Application:
    '''
    main application class
    '''

    def __init__(self, args):
        ''' constructor
        @param args - the namespace object we get from argparse.parse_args()
        '''

        self.args = args




    async def run(self):

        from telegram_dl import tdlib_generated as tdg

        # log_stream_file_obj = tdg.logStreamFile(
        #     path="C:/Users/auror/Temp/log.txt",
        #     max_file_size=10000000)
        # set_log_stream_obj = tdg.setLogStream(log_stream=log_stream_file_obj)


        # logger.info("original: `%s`", set_log_stream_obj)
        # converter = utils.CustomCattrConverter(tdlib_generated.tdlib_gen_globals, tdlib_generated.tdlib_gen_locals)

        # # utils.register_tdlib_gen_classes_with_cattr(converter)

        # x =converter.unstructure(set_log_stream_obj)

        # logger.info("unstructure result: `%s`", x)

        # y = converter.structure(x, tdg.RootObject)

        # logger.info("structure result: `%s`", y)

        # start the tdlib session

        logger.info("creating TdlibConfiguration")
        tdlib_config = tdlib.TdlibConfiguration.init_from_config(self.args.config)
        logger.info("creating TdlibHandle")
        self.tdlib_handle = await tdlib.TdlibHandle.init_from_config(tdlib_config)

        # change log settings
        log_stream_file_obj = tdg.logStreamFile(
                path=self.tdlib_handle.tdlib_config.tdlib_log_file_path,
                max_file_size=10000000)
        set_log_stream_obj = tdlib_generated.setLogStream(log_stream=log_stream_file_obj)

        logger.info("setting TDLib log file path: `%s`", set_log_stream_obj)
        await self.tdlib_handle.execute(set_log_stream_obj, without_client_ok=True)

        logger.info("creating TDLib client")
        self.tdlib_handle = await self.tdlib_handle.create_client()



        while True:
            logger.debug("loop iteration")
            resultdict = await self.tdlib_handle.receive()

            logger.debug("recieved something from receive: `%s`", resultdict)









        self.tdlib_handle = self.tdlib_handle.destroy_client()





