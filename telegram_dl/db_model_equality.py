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
    def is_equal_message(self, msg_arg:EqualityArgumentMessage) -> bool:

        if msg_arg.tdl_message == None or msg_arg.tdg_message == None:
            logger_message.debug("one of the args is None, doing fast comparison")

            fast_result =  msg_arg.tdl_message == msg_arg.tdg_message

            logger_message.debug("fast result: `%s`", fast_result)

            return fast_result

        logger_message.debug("comparing `%s`", msg_arg)


        # check stuff for the base message

        tdlmsg = msg_arg.tdl_message
        tdgmsg = msg_arg.tdg_message

        tdl_sender_id = tdlmsg.sender_user.tg_user_id if tdlmsg.sender_user else None
        tdg_sender_id = tdgmsg.sender_user_id if tdgmsg.sender_user_id != 0 else None

        tdl_chat_id = tdlmsg.chat.tg_chat_id if tdlmsg.chat else None
        tdg_chat_id = tdgmsg.chat_id if tdgmsg.chat_id != 0 else None

        tdl_reply_msg_id = tdlmsg.reply_to_message.tg_message_id if tdlmsg.reply_to_message else None
        tdg_reply_msg_id = tdgmsg.reply_to_message_id if tdgmsg.reply_to_message_id != 0 else None

        tdl_via_bot_id = tdlmsg.via_bot_user.tg_user_id if tdlmsg.via_bot_user else None
        tdg_via_bot_id = tdgmsg.via_bot_user_id if tdgmsg.via_bot_user_id != 0 else None

        base_message_result = isinstance(tdlmsg, db_model.Message) \
            and isinstance(tdgmsg, tdg.message) \
            and tdlmsg.tg_message_id == tdgmsg.id \
            and tdl_sender_id == tdg_sender_id \
            and tdl_chat_id == tdg_chat_id \
            and tdl_reply_msg_id == tdg_reply_msg_id \
            and tdl_via_bot_id == tdg_via_bot_id \
            and tdlmsg.is_outgoing == tdgmsg.is_outgoing \
            and tdlmsg.is_channel_post == tdgmsg.is_channel_post \
            and tdlmsg.can_edit == tdgmsg.can_be_edited \
            and tdlmsg.can_forward == tdgmsg.can_be_forwarded \
            and tdlmsg.can_be_deleted_only_for_self == tdgmsg.can_be_deleted_only_for_self \
            and tdlmsg.can_be_deleted_for_all_users  == tdgmsg.can_be_deleted_for_all_users \
            and tdlmsg.restriction_reason == tdgmsg.restriction_reason

        # now check the versions

        if len(tdlmsg.versions) == 0:
            logger_message.debug("returning False because Chat exists but has no versions")
            return False

        latest_msg_version = tdlmsg.versions[-1]

        # so messages are fun, since they have a base `MessageVersion` which has the common
        # shared info among all of the `messageContent` subclasses and then there are
        # subclasses of `MessageVersion` that have extra fields based on the `MessageContent`
        # type, so we call the equality methods for those types
        msg_ver_args = EqualityArgumentMessageVersion(tdl_message_version=latest_msg_version, tdg_message=tdgmsg)

        msg_ver_result = self.is_equal(msg_ver_args)

        final_result = base_message_result and msg_ver_result

        logger_message.debug("final result: base: `%s` , msgver: `%s`, final: `%s`",
            base_message_result, msg_ver_result, final_result)

        return final_result


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
        logger_message_version_text.warning("TODO `tdg.messageText.web_page` parameter is unchecked")

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
    def is_equal_text_entity(self, text_entity_arg:EqualityArgumentTextEntity) -> bool:

        logger_text_entity.debug("comparing: `%s`", text_entity_arg)


        # here go through and check all of the `tdg.textEntity` that are
        # in the `messageText.text.entities` list and then compare them
        # in a loop to the `TextEntity` objects that the
        # given `MessageVersionText` has

        # do fast comparison, if the number of entities differ then we know we have
        # a difference
        tdl_msg_ver_text = text_entity_arg.tdl_message_version_text
        tdg_msg = text_entity_arg.tdg_message

        tdl_entities = tdl_msg_ver_text.text_entities
        tdg_entities = tdg_msg.content.text.entities

        tdl_len = len(tdl_entities)
        tdg_len = len(tdg_entities)

        if tdl_len != tdg_len:
            logger_text_entity.debug(utils.strip_margin('''fast comparison,
                |returning False because the lengths are different tdl: `%s` and
                |tdg: `%s`'''), tdl_len, tdg_len)

            return False

        # make a copy of the list so we don't accidentally remove them from the database
        # when we remove from this list to make the searching slightly faster
        tdl_text_entities = [x for x in tdl_entities]

        for iter_tdg_text_entity in tdg_entities:

            found = None
            for iter_tdl_text_entity in tdl_text_entities:

                tdg_te_type = dbme.TextEntityTypeEnum.parse_from_tdg_text_entity_type(iter_tdg_text_entity.type)
                tmp_result = \
                    iter_tdl_text_entity.message_version_text.message.tg_message_id == tdg_msg.id \
                    and iter_tdl_text_entity.offset == iter_tdg_text_entity.offset \
                    and iter_tdl_text_entity.length == iter_tdg_text_entity.length \
                    and iter_tdl_text_entity.text_entity_type == tdg_te_type

                if tmp_result:
                    # found a match, set it to `found` and break so we can remove it
                    found = iter_tdl_text_entity
                    break

            # if we found a match, remove it, if we didn't, then we can return false immediately
            if found:
                tdl_text_entities.remove(found)
                found = None
                continue
            else:
                logger_text_entity.debug(utils.strip_margin('''returning false, found text entity in tdg message
                    |that doesn't exist in tdl message: `%s`'''), iter_tdg_text_entity)
                return False

        # if we get here we have found all of the text entities and they all match, return true
        logger_text_entity.debug("all text entities match, returning true")
        return True

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
