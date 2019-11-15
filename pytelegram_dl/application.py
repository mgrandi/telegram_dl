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

        self.tdlib_handle = None



    def run(self):

        cfg = self.args.config

        tdlib_config = tdlib.TdlibConfiguration.init_from_config(cfg)

        self.tdlib_handle = tdlib.TdlibHandle.init_from_config(tdlib_config)


