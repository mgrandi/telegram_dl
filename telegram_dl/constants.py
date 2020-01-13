
# in seconds
TDLIB_CLIENT_RECEIVE_TIMEOUT = 2.0

TDLIB_JSON_TYPE_STR = "@type"
TDLIB_JSON_EXTRA_STR = "@extra"
TDLIB_ORIGINAL_JSON_EXTRA_STR = "_extra"


TDLIB_TYPE_VAR_NAME = "__tdlib_type__"

CONFIG_ROOT_GROUP = "telegram_dl"
CONFIG_KEY_SHARED_LIBRARY_PATH = "library_path"
CONFIG_KEY_TDLIB_LOG_FILE = "tdlib_log_file_path"
CONFIG_KEY_API_ID = "api_id"
CONFIG_KEY_API_HASH = "api_hash"
CONFIG_KEY_TDLIB_WORKING_PATH = "tdlib_working_path"
CONFIG_KEY_TDLIB_ENABLE_STORAGE_OPTIMIZER = "tdlib_enable_storage_optimizer"
CONFIG_KEY_TDLIB_IGNORE_FILE_NAMES = "tdlib_ignore_file_names"


# as in a message type was not registered wiht TdlibBaseMessageHandler.handle_message
# so we ran the base implementation
TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED = -1