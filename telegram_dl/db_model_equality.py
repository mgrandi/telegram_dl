import logging
import functools

import attr

from phonenumbers.phonenumber import PhoneNumber
import arrow

from telegram_dl import utils
from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
import telegram_dl.db_model_enums as dbme
from telegram_dl.aides import chat_aide
from telegram_dl.aides import photo_set_aide
from telegram_dl.aides import file_aide

logger = logging.getLogger(__name__)

logger_user = logger.getChild("user")
logger_profile_photo = logger.getChild("profile_photo")
logger_file = logger.getChild("file")
logger_phonenumber = logger.getChild("phonenumber")
logger_chat = logger.getChild("chat")
logger_chat_photo = logger.getChild("chat_photo")
logger_message = logger.getChild("message")
logger_message_version = logger.getChild("message_version")
logger_message_version_text = logger.getChild("message_version_text")
logger_text_entity = logger.getChild("text_entity")

# These case classes will be the thing that functools.singledispatchmethod
# calls methods on, and these will basically holders for data that is the same,
# but represented in two different classes, ours and telegrams, such as
#`telegram_dl.db_model.User` and  `tdlib_generated.user`
@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentUser:
    tdl_user:db_model.User = attr.ib()
    tdg_user:tdg.user = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentChatPhoto:
    # again, this is kinda weird as a chat photo is basically the same
    # as a profile photo but without one field
    # so we just use a PhotoSet here with 2 images, big and small

    tdl_photo_set:db_model.PhotoSet = attr.ib()
    tdg_chat_photo:tdg.chatPhoto = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentProfilePhoto:

    # this is slightly strange because we abstract the profile photo as a
    # profile photo set (subclassed from photo set) so there is not a
    # simple 1 to 1 mapping here
    tdl_profile_photo_set:db_model.ProfilePhotoSet = attr.ib()
    tdg_profile_photo:tdg.profilePhoto = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentFile:
    tdl_file:db_model.File = attr.ib()
    tdg_file:tdg.file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentPhoneNumber:
    phonenumbers_lib_obj:PhoneNumber = attr.ib()
    str_phonenumber:str = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentChat:
    tdl_chat:db_model.Chat = attr.ib()
    tdg_chat:tdg.chat = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentMessage:
    tdl_message:db_model.Message = attr.ib()
    tdg_message:tdg.message

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentMessageVersion:
    tdl_message_version:db_model.MessageVersion
    tdg_message:tdg.message

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentMessageVersionText:
    tdl_message_version_text:db_model.MessageVersionText
    tdg_message:tdg.message

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class EqualityArgumentTextEntity:

    # the MessageVersionText has all of the TextEntity references
    tdl_message_version_text:db_model.MessageVersionText
    tdg_message:tdg.message

class DbModelEqualityTester:
    '''

    this class has one method that is a functools_singledispatchmethod , `is_equal`,
    which does comparions between like classes of our own model classes and the classes
    we generated from telegram's api definition

    '''

    def __init__(self):
        pass

    @functools.singledispatchmethod
    def is_equal(self, equality_argument:object) -> bool:
        '''
        @param one of the EqualityArgument* attr classes in this file, to compare

        @return
        '''

        logger.error(utils.strip_margin('''missing implementation of `DbModelEqualityTester.is_equal_*`,
            |base method was called! Object passed in was `%s` of type `%s`'''),
             equality_argument, type(equality_argument))


    @is_equal.register
    def is_equal_message_version(self, msg_ver_arg:EqualityArgumentMessageVersion) -> bool:

        # i should not have to check against None because they should both exist at this point,
        # given that this is called by `is_equal_message`

        logger_message_version.debug("comparing: `%s`", msg_ver_arg)

        # do base `MessageVersion` comparison
        tdlmsgver = msg_ver_arg.tdl_message_version
        tdgmsg = msg_ver_arg.tdg_message

        # compare the edit dates since we store the edit date as None if it is `0`
        tdl_edit_date = tdlmsgver.edit_date
        tdg_edit_date = arrow.get(tdgmsg.edit_date) if tdgmsg.edit_date != 0 else None

        base_msg_ver_result = isinstance(tdlmsgver, db_model.MessageVersion) \
            and isinstance(tdgmsg, tdg.message) \
            and tdlmsgver.message.tg_message_id == tdgmsg.id \
            and tdlmsgver.date ==  arrow.get(tdgmsg.date) \
            and tdl_edit_date == tdg_edit_date \
            and tdlmsgver.author_signature == tdgmsg.author_signature \
            and tdlmsgver.ttl == tdgmsg.ttl

        # do comparison based on the type of `MessageVersion` this is

        message_ver_subclass_result = None

        if isinstance(tdlmsgver, db_model.MessageVersionText):
            msg_ver_text_args = EqualityArgumentMessageVersionText(
                tdl_message_version_text=tdlmsgver, tdg_message=tdgmsg)

            message_ver_subclass_result = self.is_equal(msg_ver_text_args)

        else:
            raise Exception("unhandled MessageVersion subclass! argument: `%s`", msg_ver_arg)

        final_result = base_msg_ver_result and message_ver_subclass_result

        logger_message_version.debug("final result: base_message_ver: `%s` , message_ver_subclass_result: `%s`, final: `%s`",
            base_msg_ver_result, message_ver_subclass_result, final_result)

        return final_result


    @is_equal.register
    def is_equal_message_version_text(self, msg_ver_text_arg:EqualityArgumentMessageVersionText) -> bool:

        logger_message_version_text.debug("comparing: `%s`", msg_ver_text_arg)

        # i should not have to check against None because they should both exist at this point,
        # given that this is called by `is_equal_message` and `is_equal_message_version`

        tdl_msg_ver_text = msg_ver_text_arg.tdl_message_version_text
        tdg_msg = msg_ver_text_arg.tdg_message

        # TODO HANDLE THE `web_page` argument
        logger_message_version_text.debug("TODO `tdg.messageText.web_page` parameter is unchecked")

        message_ver_text_result = isinstance(tdl_msg_ver_text, db_model.MessageVersionText) \
            and isinstance(tdg_msg, tdg.message) \
            and tdl_msg_ver_text.text == tdg_msg.content.text.text

        # check the text entities
        text_entities_arg = EqualityArgumentTextEntity(
            tdl_message_version_text=tdl_msg_ver_text, tdg_message=tdg_msg)

        text_entity_result = self.is_equal(text_entities_arg)

        final_result = message_ver_text_result and text_entity_result

        logger_message_version_text.debug("final result: message_version_text: `%s` , text_entities: `%s`, final: `%s`",
            message_ver_text_result, text_entity_result, final_result)

        return final_result


    @is_equal.register
    def is_equal_file(self, file_arg:EqualityArgumentFile) -> bool:

        # FIXME REMOVE THIS METHOD
        return file_aide.FileAide.compare_dbmodel_file_and_tdlib_file(
            dbmodel_file=file_arg.tdl_file,
            tdlib_file=file_arg.tdg_file)


    @is_equal.register
    def is_equal_chat_photo(self, chat_photo_arg:EqualityArgumentChatPhoto) -> bool:


        # FIXME REMOVE THIS METHOD
        return photo_set_aide.PhotoSetAide.compare_dbmodel_photoset_and_tdlib_chatphoto(
            dbmodel_photoset=chat_photo_arg.tdl_photo_set,
            tdlib_chatphoto=chat_photo_arg.tdg_chat_photo)


    @is_equal.register
    def is_equal_chat(self, chat_arg:EqualityArgumentChat) -> bool:

        # FIXME REMOVE THIS METHOD
        return chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_arg.tdl_chat,
            tdlib_chat=chat_arg.tdg_chat)
