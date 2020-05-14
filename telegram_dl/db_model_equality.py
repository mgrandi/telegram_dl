import logging
import functools

import attr

from phonenumbers.phonenumber import PhoneNumber

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
        base_chat_comparison == isinstance(chat_arg.tdl_chat, db_model.Chat) \
            and isinstance(chat_arg.tdg_chat, tdg.chat) \
            and chat_arg.tdg_chat_id == chat_arg.tdg_chat.id

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

        if not final:
            logger_user.debug("user result: `%s`, profile photo result: `%s`, phone # result: `%s`",
                user_version_comparison, profilephoto_result, phoneno_result)

        return final