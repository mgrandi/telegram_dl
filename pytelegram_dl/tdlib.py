from __future__ import annotations

import logging
import ctypes
import typing
import pathlib
import locale
import platform

import attr
import pyhocon

import pytelegram_dl

logger = logging.getLogger(__name__)

@attr.s(auto_attribs=True, frozen=True)
class TdlibConfiguration:

   database_directory:pathlib.Path = attr.ib()
   use_message_database:bool = attr.ib()
   use_secret_chats:bool = attr.ib()
   api_id:int = attr.ib()
   api_hash:str = attr.ib()
   enable_storage_optimizer:bool = attr.ib()
   system_language_code:str = attr.ib()
   device_model:str = attr.ib()
   system_version:str = attr.ib()
   application_version:str = attr.ib()
   library_path:pathlib.Path = attr.ib()

   @staticmethod
   def init_from_config(config:pyhocon.config_tree.ConfigTree) -> TdlibConfiguration:

        try:

            c = config.get_config("pytelegram_dl.tdlib_configuration")

            tmp_path = pathlib.Path(c.get_string("database_directory_path")).resolve()
            tmp_msgdb = c.get_bool("use_message_database")
            tmp_secretchat = c.get_bool("use_secret_chats")
            tmp_storageopt = c.get_bool("enable_storage_optimizer")

            tmp_authid = c.get_int("auth.api_id")
            tmp_authhash = c.get_string("auth.api_hash")

            # use defaultlocale for now becuase of https://bugs.python.org/issue38805
            tmp_lang = locale.getdefaultlocale()[0]
            tmp_model = "Desktop"
            tmp_sysver = f"{platform.system()} {platform.version()}"
            tmp_ver = f"pytelegram_dl v{pytelegram_dl.__version__} / Python {platform.python_version()}"
            tmp_lpath = pathlib.Path(config.get_string("pytelegram_dl.library_path"))

            final_cfg = TdlibConfiguration(
                database_directory=tmp_path,
                use_message_database=tmp_msgdb,
                use_secret_chats=tmp_secretchat,
                api_id=tmp_authid,
                api_hash=tmp_authhash,
                enable_storage_optimizer=tmp_storageopt,
                system_language_code=tmp_lang,
                device_model=tmp_model,
                system_version=tmp_sysver,
                application_version=tmp_ver,
                library_path=tmp_lpath)

            logger.debug("new TdlibConfiguration from configuration: `%s`", final_cfg)
            return final_cfg


        except pyhocon.exceptions.ConfigException as e:

            logger.exception("TdlibConfiguration.init_from_config: error when reading needed values from configuration")
            raise e
        except Exception as e:
            logger.exception("TdlibConfiguration.init_from_config: unexpected error")
            raise e


@attr.s(auto_attribs=True, frozen=True)
class TdlibHandle:


    tdlib_shared_library:ctypes.CDLL = attr.ib()

    tdlib_config:TdlibConfiguration = attr.ib()

    # these are all of these types:
    #
    # <class 'ctypes.CDLL.__init__.<locals>._FuncPtr'>
    # not sure how to represent that with typing.Callable
    func_client_create:typing.Any = attr.ib()
    func_client_receive:typing.Any = attr.ib()
    func_client_send:typing.Any = attr.ib()
    func_client_execute:typing.Any = attr.ib()
    func_client_destroy:typing.Any = attr.ib()
    func_set_log_fatal_error_callback:typing.Any = attr.ib()

    # type for passing in a python function to the tdlib function set+log_fatal_error_callback
    fatal_error_callback_type = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

    # gets set afterwards
    tdlib_client:typing.Any = attr.ib(default=None)

    @staticmethod
    def fatal_error_callback(error_message:str) -> None:
        logger.error("TDLib fatal error: `%s`", error_message)


    @staticmethod
    def init_from_config(tdlib_config:TdlibConfiguration) -> TdlibHandle:

        try:

            tdjson = ctypes.CDLL(str(tdlib_config.library_path))


            # load TDLib functions from shared library
            td_json_client_create = tdjson.td_json_client_create
            td_json_client_create.restype = ctypes.c_void_p
            td_json_client_create.argtypes = []

            td_json_client_receive = tdjson.td_json_client_receive
            td_json_client_receive.restype = ctypes.c_char_p
            td_json_client_receive.argtypes = [ctypes.c_void_p, ctypes.c_double]

            td_json_client_send = tdjson.td_json_client_send
            td_json_client_send.restype = None
            td_json_client_send.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

            td_json_client_execute = tdjson.td_json_client_execute
            td_json_client_execute.restype = ctypes.c_char_p
            td_json_client_execute.argtypes = [ctypes.c_void_p, ctypes.c_char_p]

            td_json_client_destroy = tdjson.td_json_client_destroy
            td_json_client_destroy.restype = None
            td_json_client_destroy.argtypes = [ctypes.c_void_p]

            fatal_error_callback_type = ctypes.CFUNCTYPE(None, ctypes.c_char_p)

            td_set_log_fatal_error_callback = tdjson.td_set_log_fatal_error_callback
            td_set_log_fatal_error_callback.restype = None
            td_set_log_fatal_error_callback.argtypes = [TdlibHandle.fatal_error_callback_type]

            # set the callback
            c_on_fatal_error_callback = fatal_error_callback_type(TdlibHandle.fatal_error_callback)
            td_set_log_fatal_error_callback(c_on_fatal_error_callback)

            res = TdlibHandle(
                tdlib_shared_library=tdjson,
                tdlib_config=tdlib_config,
                tdlib_client=None, # no client yet
                func_client_create=td_json_client_create,
                func_client_receive=td_json_client_receive,
                func_client_send=td_json_client_send,
                func_client_execute=td_json_client_execute,
                func_client_destroy=td_json_client_destroy,
                func_set_log_fatal_error_callback=td_set_log_fatal_error_callback)

            logger.debug("new TdlibHandle from configuration: `%s`", res)
            return res

        except Exception as e:
            logger.exception("TdlibHandle.init_with_configuration: unknown exception")
            raise e




    def create_client(self) -> TdlibHandle:
        ''' creates a client and returns a new instance of TdlibHandle with the new client
        '''

        if self.tdlib_client is not None:
            raise Exception("TdlibHandle.create_client called when a client already exists")

        logger.info("creating tdlib client")
        new_client = self.func_client_create()
        logger.info("tdlib client created successfully")

        return attr.evolve(self, tdlib_client=new_client)



    def destroy_client(self) -> TdlibHandle:
        ''' destroys the client and returns a new instance of TdlibHandle with the
        client removed
        '''

        logger.info("destroying tdlib client")
        self.func_client_destroy(self.tdlib_client)
        logger.info("tdlib client destroyed successfully")
        return attr.evolve(self, tdlib_client=None)