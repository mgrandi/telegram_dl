from __future__ import annotations

import pathlib
import logging

import attr
from sqlalchemy.engine.url import URL
import pyhocon

from telegram_dl import constants
from telegram_dl import utils

logger = logging.getLogger(__name__)


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class ApplicationConfiguration:

    use_test_dc:bool = attr.ib()
    library_path:str = attr.ib()
    tdlib_log_file_path:pathlib.Path = attr.ib()
    tdlib_log_file_max_size_bytes:int = attr.ib()
    tdlib_log_verbosity:int = attr.ib()
    api_id:str = attr.ib(repr=False)
    api_hash:str = attr.ib(repr=False)
    tdlib_working_path:pathlib.Path = attr.ib()
    tdlib_enable_storage_optimizer:bool = attr.ib()
    tdlib_ignore_file_names:bool = attr.ib()
    sqlalchemy_url:URL = attr.ib()

    @staticmethod
    def init_from_config(config:pyhocon.config_tree.ConfigTree) -> ApplicationConfiguration:

        logger.info("loading config")
        try:

            c = config.get_config(constants.CONFIG_ROOT_GROUP)

            tmp_library_path = pathlib.Path(c.get_string(constants.CONFIG_KEY_SHARED_LIBRARY_PATH)).resolve()
            if not tmp_library_path.exists():
                raise Exception(f"the shared tdjson library path provided `{tmp_library_path}` doesn't exist!")

            tmp_tdlib_log_file_path = pathlib.Path(c.get_string(constants.CONFIG_KEY_TDLIB_LOG_FILE))
            if not tmp_tdlib_log_file_path.parent.exists():
                raise Exception(f"the path provided for the tdlib log file `{tmp_tdlib_log_file_path}`'s parent doesn't exist!")

            tmp_log_max_size = c.get_int(constants.CONFIG_KEY_TDLIB_LOG_FILE_MAX_SIZE_BYTES)
            tmp_log_verbosity = c.get_int(constants.CONFIG_KEY_TDLIB_LOG_VERBOSITY)

            tmp_api_id = c.get_int(constants.CONFIG_KEY_API_ID)
            tmp_api_hash = c.get_string(constants.CONFIG_KEY_API_HASH)

            tmp_use_test = c.get_bool(constants.CONFIG_KEY_USE_TEST_DC)

            tmp_tdlib_working_path = pathlib.Path(c.get_string(constants.CONFIG_KEY_TDLIB_WORKING_PATH))
            if not tmp_tdlib_working_path.exists() or not tmp_tdlib_working_path.is_dir():
                raise Exception(f"the tdlib working path provided `{tmp_tdlib_working_path}` is not a folder or doesn't exist!")

            tmp_enable_storage_opt = c.get_bool(constants.CONFIG_KEY_TDLIB_ENABLE_STORAGE_OPTIMIZER)
            tmp_ignore_file_names = c.get_bool(constants.CONFIG_KEY_TDLIB_IGNORE_FILE_NAMES)


            # get sqlalchemy url:
            db_group = c.get_config(constants.CONFIG_DATABASE_GROUP)
            sqla_url = utils.get_sqlalchemy_url_from_hocon_config(db_group)

            tdlibcfg =  ApplicationConfiguration(
                use_test_dc=tmp_use_test,
                library_path=tmp_library_path,
                tdlib_log_file_path=tmp_tdlib_log_file_path,
                tdlib_log_file_max_size_bytes=tmp_log_max_size,
                tdlib_log_verbosity=tmp_log_verbosity,
                api_id=tmp_api_id,
                api_hash=tmp_api_hash,
                tdlib_working_path=tmp_tdlib_working_path,
                tdlib_enable_storage_optimizer=tmp_enable_storage_opt,
                tdlib_ignore_file_names=tmp_ignore_file_names,
                sqlalchemy_url=sqla_url)

            logger.debug("loaded ApplicationConfiguration: `%s`", tdlibcfg)

            return tdlibcfg

        except pyhocon.exceptions.ConfigException as e:

            logger.exception("ApplicationConfiguration.init_from_config: error when reading needed values from configuration")
            raise e
        except Exception as e:
            logger.exception("ApplicationConfiguration.init_from_config: unexpected error")
            raise e