from __future__ import annotations

import logging
import ctypes
import typing
import pathlib
import locale
import platform
import json

import attr
import pyhocon

import telegram_dl
from telegram_dl import utils
from telegram_dl import constants

from telegram_dl import tdlib_generated


logger = logging.getLogger(__name__)
receive_logger = logger.getChild("receive")
send_logger = logger.getChild("send")
execute_logger = logger.getChild("execute")
create_logger = logger.getChild("create")
destroy_logger = logger.getChild("destroy")

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TdlibResult:
    code:int = attr.ib()
    message:str = attr.ib()
    result_obj:tdlib_generated.RootObject = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TdlibConfiguration:

    library_path:str = attr.ib()
    tdlib_log_file_path:pathlib.Path = attr.ib()
    api_id:str = attr.ib(repr=False)
    api_hash:str = attr.ib(repr=False)
    tdlib_working_path:pathlib.Path = attr.ib()
    tdlib_enable_storage_optimizer:bool = attr.ib()
    tdlib_ignore_file_names:bool = attr.ib()

    @staticmethod
    def init_from_config(config:pyhocon.config_tree.ConfigTree) -> TdlibConfiguration:

        logger.info("loading config")
        try:

            c = config.get_config(constants.CONFIG_ROOT_GROUP)

            tmp_library_path = pathlib.Path(c.get_string(constants.CONFIG_KEY_SHARED_LIBRARY_PATH)).resolve()
            if not tmp_library_path.exists():
                raise Exception(f"the shared tdjson library path provided `{tmp_library_path}` doesn't exist!")

            tmp_tdlib_log_file_path = pathlib.Path(c.get_string(constants.CONFIG_KEY_TDLIB_LOG_FILE))
            if not tmp_tdlib_log_file_path.parent.exists():
                raise Exception(f"the path provided for the tdlib log file `{tmp_tdlib_log_file_path}`'s parent doesn't exist!")

            tmp_api_id = c.get_int(constants.CONFIG_KEY_API_ID)
            tmp_api_hash = c.get_string(constants.CONFIG_KEY_API_HASH)


            tmp_tdlib_working_path = pathlib.Path(c.get_string(constants.CONFIG_KEY_TDLIB_WORKING_PATH))
            if not tmp_tdlib_working_path.exists() or not tmp_tdlib_working_path.is_dir():
                raise Exception(f"the tdlib working path provided `{tmp_tdlib_working_path}` is not a folder or doesn't exist!")

            tmp_enable_storage_opt = c.get_bool(constants.CONFIG_KEY_TDLIB_ENABLE_STORAGE_OPTIMIZER)
            tmp_ignore_file_names = c.get_bool(constants.CONFIG_KEY_TDLIB_IGNORE_FILE_NAMES)

            tdlibcfg =  TdlibConfiguration(
                library_path=tmp_library_path,
                tdlib_log_file_path=tmp_tdlib_log_file_path,
                api_id=tmp_api_id,
                api_hash=tmp_api_hash,
                tdlib_working_path=tmp_tdlib_working_path,
                tdlib_enable_storage_optimizer=tmp_enable_storage_opt,
                tdlib_ignore_file_names=tmp_ignore_file_names)

            logger.debug("loaded TdlibConfiguration: `%s`", tdlibcfg)

            return tdlibcfg

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

    tdlib_parameters_config:tdlibParameters = attr.ib(repr=False)

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
    tdlib_client:typing.Any = attr.ib()

    cattr_converter:utils.CustomCattrConverter = attr.ib()


    @staticmethod
    def fatal_error_callback(error_message:str) -> None:
        logger.error("TDLib fatal error: `%s`", error_message)

    @staticmethod
    def create_tdlib_parameters(config:TdlibConfiguration) -> tdlib_generated.tdlibParameters:

        # use defaultlocale for now becuase of https://bugs.python.org/issue38805
        tmp_lang = locale.getdefaultlocale()[0]
        tmp_model = "Desktop"
        tmp_sysver = f"{platform.system()} {platform.version()}"
        tmp_appver = f"telegram_dl {telegram_dl.__version__} / Python {platform.python_version()}"

        files_dir = config.tdlib_working_path / "files"
        if not files_dir.exists():
            logger.debug("creating directory for the files inside the tdlib working directory: `%s`", files_dir)
            files_dir.mkdir()

        tp = tdlib_generated.tdlibParameters(
            use_test_dc=False,
            database_directory=str(config.tdlib_working_path),
            files_directory=str(files_dir),
            use_file_database=True,
            use_chat_info_database=True,
            use_message_database=True,
            use_secret_chats=True,
            api_id=config.api_id,
            api_hash=config.api_hash,
            system_language_code=tmp_lang,
            device_model=tmp_model,
            system_version=tmp_sysver,
            application_version=tmp_appver,
            enable_storage_optimizer=config.tdlib_enable_storage_optimizer,
            ignore_file_names=config.tdlib_ignore_file_names )

        return tp


    @staticmethod
    async def init_from_config(config:TdlibConfiguration) -> TdlibHandle:

        try:


            logger.info("loading tdjson shared library at `%s`", config.library_path)
            tdjson = ctypes.CDLL(str(config.library_path))
            logger.info("tdjson shared library loaded successfully")

            tdlib_parameters_config = TdlibHandle.create_tdlib_parameters(config)
            logger.debug("tdlibParameters: `%s`", tdlib_parameters_config)

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

            # cattr converter
            converter = utils.CustomCattrConverter(tdlib_generated.tdlib_gen_globals, tdlib_generated.tdlib_gen_locals)

            tdlib_handle = TdlibHandle(
                tdlib_shared_library=tdjson,
                tdlib_config=config,
                tdlib_parameters_config=tdlib_parameters_config,
                tdlib_client=None, # no client yet
                func_client_create=td_json_client_create,
                func_client_receive=td_json_client_receive,
                func_client_send=td_json_client_send,
                func_client_execute=td_json_client_execute,
                func_client_destroy=td_json_client_destroy,
                func_set_log_fatal_error_callback=td_set_log_fatal_error_callback,
                cattr_converter=converter)


            logger.debug("new TdlibHandle from configuration: `%s`", tdlib_handle)
            return tdlib_handle

        except Exception as e:
            logger.exception("TdlibHandle.init_with_configuration: unknown exception")
            raise e


    async def create_client(self) -> TdlibHandle:
        ''' creates a client and returns a new instance of TdlibHandle with the new client
        '''

        if self.tdlib_client is not None:
            raise Exception("TdlibHandle.create_client called when a client already exists")

        create_logger.debug("creating tdlib client")
        new_client = self.func_client_create()
        create_logger.debug("tdlib client created successfully: `%s`", new_client)

        return attr.evolve(self, tdlib_client=new_client)

    async def send(self, obj_to_send:tdlib_generated.RootObject) -> None:

        if self.tdlib_client is None:
            raise Exception("TdlibHandle.send called when no client has been created")

        send_logger.debug("tdlib client `%s` called with: `%s`", "send", obj_to_send)

        # convert the object to a dictionary
        # TODO: replace cattrs
        obj_as_dict = self.cattr_converter.unstructure(obj_to_send)

        json_str = json.dumps(obj_as_dict, cls=utils.CustomJSONEncoder)
        json_bytes = json_str.encode("utf-8")

        self.func_client_send(self.tdlib_client, json_bytes)
        send_logger.debug("tdlib client `%s` called successfully", "send")

    async def execute(self, obj_to_send:tdlib_generated.RootObject, without_client_ok:bool=False) -> tdlib_generated.RootObject:

        if self.tdlib_client is None and not without_client_ok:
            raise Exception("TdlibHandle.send called when no client has been created")

        execute_logger.debug("tdlib client `%s` called with: `%s`", "execute", obj_to_send)

        # convert the object to a dictionary
        # TODO: replace cattrs
        obj_as_dict = self.cattr_converter.unstructure(obj_to_send)

        json_str = json.dumps(obj_as_dict, cls=utils.CustomJSONEncoder)
        json_bytes = json_str.encode("utf-8")

        res = self.func_client_execute(self.tdlib_client, json_bytes)

        final_result = res

        # need to parse the result, or return None if it was None
        # result is None if the request can't be parsed or timeout i guess?
        if res is not None:

            json_result = json.loads(res)

            # convert the json back into an object
            # TODO: replace cattrs
            final_result = self.cattr_converter.structure(json_result, tdlib_generated.RootObject)

        execute_logger.debug("tdlib client `%s` called successfully: `%s`", "execute", final_result)

        return final_result

    async def receive(self) -> utils.RootObject:

        if self.tdlib_client is None:
            raise Exception("TdlibHandle.receive called when no client has been created")

        receive_logger.debug("tdlib client `%s` called", "receive")
        res = self.func_client_receive(self.tdlib_client, constants.TDLIB_CLIENT_RECEIVE_TIMEOUT)

        receive_logger.debug("raw result: `%s`", res)
        final_result = res

        # need to parse the result, or return None if it was None
        # result is None if the request can't be parsed or timeout i guess?
        if res is not None:

            json_result = json.loads(res)

            # convert the json back into an object
            # TODO: replace cattrs
            final_result = self.cattr_converter.structure(json_result, tdlib_generated.RootObject)

        receive_logger.debug("tdlib client `%s` called successfully, obj result: `%s`", "receive", final_result)

        return final_result

    def destroy_client(self) -> TdlibHandle:
        ''' destroys the client and returns a new instance of TdlibHandle with the
        client removed
        '''

        destroy_logger.info("destroying tdlib client")
        self.func_client_destroy(self.tdlib_client)
        destroy_logger.info("tdlib client destroyed successfully")
        return attr.evolve(self, tdlib_client=None)