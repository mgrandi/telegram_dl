import logging


import pytelegram_dl.tdlib as tdlib

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

        tdlib_config = tdlib.TdlibConfiguration.init_from_config(self.args.config)

        self.tdlib_handle = tdlib.TdlibHandle.init_from_config(tdlib_config)

    def run(self):


        # start the tdlib session

        self.tdlib_handle = self.tdlib_handle.create_client()

        self.tdlib_handle = self.tdlib_handle.destroy_client()





