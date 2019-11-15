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

        # temporary: set tdlib logging to a file
        self.tdlib_handle.execute({"@type": "setLogStream", "log_stream": {"@type": "logStreamFile", "path": str(self.tdlib_handle.tdlib_config.tdlib_log_file_path), "max_file_size": 10000000}})

        while True:
            event = self.tdlib_handle.receive()

            logger.debug("new event: `%s`", event)

            if event:

                 # process authorization states
                if event['@type'] == 'updateAuthorizationState':
                    auth_state = event['authorization_state']

                    # if client is closed, we need to destroy it and create new client
                    if auth_state['@type'] == 'authorizationStateClosed':
                        break

                    # set TDLib parameters
                    # you MUST obtain your own api_id and api_hash at https://my.telegram.org
                    # and use them in the setTdlibParameters call
                    if auth_state['@type'] == 'authorizationStateWaitTdlibParameters':

                        tdlibParams = {'@type': 'setTdlibParameters',
                            'parameters': self.tdlib_handle.tdlib_config.get_tdlibparams_json_params()}
                        self.tdlib_handle.send(tdlibParams)

                    # set an encryption key for database to let know TDLib how to open the database
                    if auth_state['@type'] == 'authorizationStateWaitEncryptionKey':
                        self.tdlib_handle.send({'@type': 'checkDatabaseEncryptionKey', 'key': ''})

                    # enter phone number to log in
                    if auth_state['@type'] == 'authorizationStateWaitPhoneNumber':
                        phone_number = input('Please enter your phone number: ')
                        self.tdlib_handle.send({'@type': 'setAuthenticationPhoneNumber', 'phone_number': phone_number})

                    # wait for authorization code
                    if auth_state['@type'] == 'authorizationStateWaitCode':
                        code = input('Please enter the authentication code you received: ')
                        self.tdlib_handle.send({'@type': 'checkAuthenticationCode', 'code': code})

                    # wait for first and last name for new users
                    if auth_state['@type'] == 'authorizationStateWaitRegistration':
                        first_name = input('Please enter your first name: ')
                        last_name = input('Please enter your last name: ')
                        self.tdlib_handle.send({'@type': 'registerUser', 'first_name': first_name, 'last_name': last_name})

                    # wait for password if present
                    if auth_state['@type'] == 'authorizationStateWaitPassword':
                        password = input('Please enter your password: ')
                        self.tdlib_handle.send({'@type': 'checkAuthenticationPassword', 'password': password})




        self.tdlib_handle = self.tdlib_handle.destroy_client()





