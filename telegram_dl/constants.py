import re


# according to this page, short codes are not actually E164 and are 5-6 digits in length
# https://support.twilio.com/hc/en-us/articles/360013980754-Formatting-Short-Code-Numbers
PHONE_NUMBER_SHORT_CODE_MIN_LENGTH = 5
PHONE_NUMBER_SHORT_CODE_MAX_LENGTH = 6
PHONE_NUMBER_DEFAULT_REGION = "US"
PHONE_NUMBER_MAX_LENGTH = 20

# logger that just only logs the raw messages we get
# from telegram
MESSAGE_ARCHIVE_LOGGER_FROM_TELEGRAM_NAME = "telegram_dl.message_archive.in"
MESSAGE_ARCHIVE_LOGGER_TO_TELEGRAM_NAME = "telegram_dl.message_archive.out"


# in seconds
TDLIB_CLIENT_RECEIVE_TIMEOUT = 2.0
PROCESS_MESSAGE_QUEUE_TIMEOUT = 2.0

TDLIB_JSON_TYPE_STR = "@type"
TDLIB_JSON_EXTRA_STR = "@extra"
TDLIB_ORIGINAL_JSON_EXTRA_STR = "_extra"


TDLIB_TYPE_VAR_NAME = "__tdlib_type__"

# used to pass in our own config path into alembic commands using `alembic -x key=value`
ALEMBIC_CMD_X_ARGUMENT_NAME = "telegram_dl_config"

CONFIG_ROOT_GROUP = "telegram_dl"
CONFIG_KEY_SHARED_LIBRARY_PATH = "library_path"
CONFIG_KEY_TDLIB_LOG_FILE = "tdlib_log_file_path"
CONFIG_KEY_API_ID = "api_id"
CONFIG_KEY_API_HASH = "api_hash"
CONFIG_KEY_TDLIB_WORKING_PATH = "tdlib_working_path"
CONFIG_KEY_TDLIB_ENABLE_STORAGE_OPTIMIZER = "tdlib_enable_storage_optimizer"
CONFIG_KEY_TDLIB_IGNORE_FILE_NAMES = "tdlib_ignore_file_names"

CONFIG_DATABASE_GROUP = "database"
CONFIG_KEY_DATABASE_DRIVER = "driver_name"
CONFIG_KEY_DATABASE_USER = "user_name"
CONFIG_KEY_DATABASE_PASSWORD = "password"
CONFIG_KEY_DATABASE_HOST = "host"
CONFIG_KEY_DATABASE_PORT = "port"
CONFIG_KEY_DATABASE_DATABASE = "database"
CONFIG_KEY_DATABASE_QUERY = "query"



# as in a message type was not registered wiht TdlibBaseMessageHandler.handle_message
# so we ran the base implementation
TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED = -1
TDLIB_RESULT_CODE_OK = 0


# TODO: should make these translatable strings?
# NOTE: these should all have a space at the end or else the input text runs against the
# prompt text!
INPUT_ASK_FOR_PHONE_NUMBER = "Please enter your phone number (+X-XXX-XXX-XXXX): "
INPUT_ASK_FOR_CODE = "Please enter the 2FA code sent to your phone: "
INPUT_ASK_FOR_FIRST_NAME = "Please enter your first name: "
INPUT_ASK_FOR_LAST_NAME = "Please enter your last name: "
INPUT_ASK_FOR_PASSWORD = "Please enter your Cloud Password: "


PHONE_NO_REGEX_CC = "country_code"
PHONE_NO_REGEX_AC = "area_code"
PHONE_NO_REGEX_PN1 = "phone_num_part_one"
PHONE_NO_REGEX_PN2 = "phone_num_part_two"
# i was originally gonna use a `f` string and then replace the group names with `{}` but then it was also replacing the
# multiplicity modifiers (like `{3}` or `{1,3}`) and i would have to double up the braces which looks ugly, so just type
# the group names manually here
INPUT_PHONE_NUMBER_REGEX = re.compile(r"^\+(?P<country_code>[0-9]{1,3})-(?P<area_code>[0-9]{3})-(?P<phone_num_part_one>[0-9]{3})-(?P<phone_num_part_two>[0-9]{4})")