import logging
import functools

import attr

from phonenumbers.phonenumber import PhoneNumber
import arrow

from telegram_dl import utils
from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
import telegram_dl.db_model_enums as dbme


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
    def is_equal_phonenumber(self, phonenumber_arg:EqualityArgumentPhoneNumber) -> bool:

        phoneno_result = None

        logger_phonenumber.debug("comparing `%s`", phonenumber_arg)

        if not phonenumber_arg.phonenumbers_lib_obj:

            if not phonenumber_arg.str_phonenumber:
                # both phone numbers are empty, just mark as unchanged right
                phoneno_result = True
            else:
                # old phone number doesn't exist but the new one does exist, mark as different
                phoneno_result = False
        else:
            if not phonenumber_arg.str_phonenumber:
                # old phone exists but new one doesn't, mark as different
                phoneno_result = False
            else:
                # both old and new phone numbers exist, compare
                fixed_phone_no_str = utils.fix_phone_number(phonenumber_arg.str_phonenumber)
                parsed_phone = utils.parse_phone_number_from_str(fixed_phone_no_str)

                phoneno_result = phonenumber_arg.phonenumbers_lib_obj == parsed_phone

        logger_phonenumber.debug("final result: `%s`", phoneno_result)

        return phoneno_result

    @is_equal.register
    def is_equal_file(self, file_arg:EqualityArgumentFile) -> bool:
        '''
        see if a db_model.File equals a tdg.file
        '''

        # here we are just going to check the remote file id and the remote unique id

        if file_arg.tdl_file is None or file_arg.tdg_file is None:
            logger_file.debug("one of the args is None, doing fast comparison")

            fast_result =  file_arg.tdl_file == file_arg.tdg_file

            logger_file.debug("fast result: `%s`", fast_result)

            return fast_result


        logger_file.debug("comparing `%s`", file_arg)

        result_remote_file_id = file_arg.tdl_file.remote_file_id == file_arg.tdg_file.remote.id
        result_remote_unique_id = file_arg.tdl_file.remote_unique_id == file_arg.tdg_file.remote.unique_id

        logger_file.debug("remote id: `%s`, remote unique id: `%s`", result_remote_file_id, result_remote_unique_id)

        final_result = result_remote_unique_id and result_remote_file_id

        logger_file.debug("final result: `%s`", final_result)

        return final_result


    @is_equal.register
    def is_equal_chat_photo(self, chat_photo_arg:EqualityArgumentChatPhoto) -> bool:
        '''
        Testing to see if a `db_model.Chat`s `db_model.PhotoSet` 'matches'
        tdlib's 'chatPhoto' class

        since we are abstracting a `tdg.chatPhoto` as a `db_model.PhotoSet ,
        its slightly more complicated
        '''

        # a `tdg.chatPhoto` has 2 fields, 'big` (file), `small` (file),
        #
        # a db_model.PhotoSet has a collection of db_model.Photo objects,
        # each with a reference to a db_model.File

        # do fast check for None, some users don't have a profile photo or have removed it
        # since we last checked
        logger_chat_photo.debug("comparing `%s`", chat_photo_arg)

        if chat_photo_arg.tdl_photo_set is None or \
            chat_photo_arg.tdg_chat_photo is None:

            logger_chat_photo.debug("one of the args is None, doing fast comparison")

            fast_result = chat_photo_arg.tdl_photo_set == chat_photo_arg.tdg_chat_photo

            logger_chat_photo.debug("fast result: `%s`", fast_result)

            return fast_result

        # check files
        logger_chat_photo.debug("comparing big file")

        big_photo_file_args = EqualityArgumentFile(
            tdl_file=chat_photo_arg.tdl_photo_set.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_BIG)[0].file,
            tdg_file=chat_photo_arg.tdg_chat_photo.big)

        big_photo_comparison = self.is_equal(big_photo_file_args)

        logger_chat_photo.debug("comparing small file")

        small_photo_file_args = EqualityArgumentFile(
            tdl_file=chat_photo_arg.tdl_photo_set.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_SMALL)[0].file,
            tdg_file=chat_photo_arg.tdg_chat_photo.small)

        small_photo_comparison = self.is_equal(small_photo_file_args)

        logger_chat_photo.debug("big photo comparison: `%s`, small photo comparison: `%s`",
            big_photo_comparison, small_photo_comparison)

        # get final result
        final_result = big_photo_comparison and small_photo_comparison

        logger_chat_photo.debug("final result: `%s`", final_result)

        return final_result


    @is_equal.register
    def is_equal_profile_photo(self, profile_photo_arg:EqualityArgumentProfilePhoto) -> bool:
        '''
        Testing to see if a `db_model.User`s `db_model.ProfilePhotoSet` 'matches'
        tdlib's 'profilePhoto' class

        since we are abstracting a `tdg.profilePhoto` as a `db_model.ProfilePhotoSet ,
        its slightly more complicated
        '''

        # a `tdg.profilePhoto` has 3 fields, 'big` (file), `small` (file), and
        # `id` (int)
        #
        # a db_model.PhotoSet has a collection of db_model.Photo objects,
        # each with a reference to a db_model.File
        # tdg.profilePhoto.id corresponds to the db_model.ProfilePhotoSet.tg_id field

        # do fast check for None, some users don't have a profile photo or have removed it
        # since we last checked
        logger_profile_photo.debug("comparing `%s`", profile_photo_arg)

        if profile_photo_arg.tdl_profile_photo_set is None or \
            profile_photo_arg.tdg_profile_photo is None:

            logger_profile_photo.debug("one of the args is None, doing fast comparison")

            fast_result = profile_photo_arg.tdl_profile_photo_set == profile_photo_arg.tdg_profile_photo

            logger_profile_photo.debug("fast result: `%s`", fast_result)

            return fast_result


        # check profile photo 'id'
        id_comparison = profile_photo_arg.tdl_profile_photo_set.tg_id == profile_photo_arg.tdg_profile_photo.id

        # check files
        logger_profile_photo.debug("comparing big file")

        big_photo_file_args = EqualityArgumentFile(
            tdl_file=profile_photo_arg.tdl_profile_photo_set.big.file,
            tdg_file=profile_photo_arg.tdg_profile_photo.big)

        big_photo_comparison = self.is_equal(big_photo_file_args)

        logger_profile_photo.debug("comparing small file")

        small_photo_file_args = EqualityArgumentFile(
            tdl_file=profile_photo_arg.tdl_profile_photo_set.small.file,
            tdg_file=profile_photo_arg.tdg_profile_photo.small)

        small_photo_comparison = self.is_equal(small_photo_file_args)

        logger_profile_photo.debug("big photo comparison: `%s`, small photo comparison: `%s`",
            big_photo_comparison, small_photo_comparison)

        # get final result
        final_result =  id_comparison and big_photo_comparison and small_photo_comparison

        logger_profile_photo.debug("final result: `%s`", final_result)

        return final_result

    @is_equal.register
    def is_equal_chat(self, chat_arg:EqualityArgumentChat) -> bool:

        logger_chat.debug("comparing `%s`", chat_arg)

        if chat_arg.tdl_chat is None or chat_arg.tdg_chat is None:
            logger_chat.debug("one of the args is None, doing fast comparison")

            fast_result = chat_arg.tdl_chat == chat_arg.tdg_chat

            logger_chat.debug("fast result: `%s`", fast_result)

            return fast_result

        if len(chat_arg.tdl_chat.versions) == 0:
            logger_chat.debug("returning False because Chat exists but has no versions")
            return False

        # check the base chat
        base_chat_comparison = isinstance(chat_arg.tdl_chat, db_model.Chat) \
            and isinstance(chat_arg.tdg_chat, tdg.chat) \
            and chat_arg.tdl_chat.tg_chat_id == chat_arg.tdg_chat.id

        # get the latest version

        # should be sorted by ascending so the LAST index is the latest

        latest_version = chat_arg.tdl_chat.versions[-1]

        chat_version_comparison = chat_arg.tdg_chat is not None \
            and isinstance(chat_arg.tdg_chat, tdg.chat) \
            and latest_version.chat.tg_chat_id == chat_arg.tdg_chat.id \
            and latest_version.title == chat_arg.tdg_chat.title \
            and latest_version.is_sponsored == chat_arg.tdg_chat.is_sponsored


        chat_photo_arg = EqualityArgumentChatPhoto(
            tdl_photo_set=latest_version.photo_set,
            tdg_chat_photo=chat_arg.tdg_chat.photo)

        chat_photo_result = self.is_equal(chat_photo_arg)

        # get final result
        final_result =  base_chat_comparison and chat_version_comparison and chat_photo_result

        logger_chat.debug("final result: `%s`", final_result)

        return final_result

    @is_equal.register
    def is_equal_user(self, user_arg:EqualityArgumentUser) -> bool:
        ''' equality test comparing `db_model.User` and `telegram_generated.user`

        '''

        if user_arg.tdl_user is None or user_arg.tdg_user is None:
            logger_user.debug("one of the args is None, doing fast comparison")

            fast_result = user_arg.tdl_user == user_arg.tdg_user

            logger_user.debug("fast result: `%s`", fast_result)

            return fast_result

        if len(user_arg.tdl_user.versions) == 0:
            logger_user.debug("returning False because User exists but has no versions")
            return False

        # get the latest version

        # should be sorted by ascending so the LAST index is the latest

        latest_version = user_arg.tdl_user.versions[-1]


        user_version_comparison = user_arg.tdg_user is not None \
            and isinstance(user_arg.tdg_user, tdg.user) \
            and user_arg.tdl_user.tg_user_id == user_arg.tdg_user.id \
            and latest_version.first_name == user_arg.tdg_user.first_name \
            and latest_version.last_name == user_arg.tdg_user.last_name \
            and latest_version.user_name == user_arg.tdg_user.username \
            and latest_version.is_contact == user_arg.tdg_user.is_contact \
            and latest_version.is_mutual_contact == user_arg.tdg_user.is_mutual_contact \
            and latest_version.is_verified == user_arg.tdg_user.is_verified \
            and latest_version.is_support == user_arg.tdg_user.is_support \
            and latest_version.restriction_reason == user_arg.tdg_user.restriction_reason \
            and latest_version.is_scam == user_arg.tdg_user.is_scam \
            and latest_version.have_access == user_arg.tdg_user.have_access \
            and latest_version.user_type == dbme.UserTypeEnum.parse_from_tdg_usertype(user_arg.tdg_user.type) \
            and latest_version.language_code == user_arg.tdg_user.language_code

        # check to see if there
        profile_photo_arg = EqualityArgumentProfilePhoto(
            tdl_profile_photo_set=latest_version.profile_photo_set,
            tdg_profile_photo=user_arg.tdg_user.profile_photo)
        profilephoto_result = self.is_equal(profile_photo_arg)

        # handle where we get a str from telegram but a Phonenumber object from the database
        # or the user has no phone number at all
        phone_args = EqualityArgumentPhoneNumber(
            phonenumbers_lib_obj=latest_version.phone_number,
            str_phonenumber=user_arg.tdg_user.phone_number)

        phoneno_result = self.is_equal(phone_args)


        final = user_version_comparison and profilephoto_result and phoneno_result

        logger_user.debug("user result: `%s`, profile photo result: `%s`, phone # result: `%s`",
                user_version_comparison, profilephoto_result, phoneno_result)

        return final