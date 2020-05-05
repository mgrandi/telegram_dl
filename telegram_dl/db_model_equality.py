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

# These case classes will be the thing that functools.singledispatchmethod
# calls methods on, and these will basically holders for data that is the same,
# but represented in two different classes, ours and telegrams, such as
#`telegram_dl.db_model.User` and  `tdlib_generated.user`
@attr.s
class EqualityArgumentUser:
    tdl_user:db_model.User = attr.ib()
    tdg_user:tdg.user = attr.ib()

@attr.s
class EqualityArgumentProfilePhoto:

    # this is slightly strange because we abstract the profile photo as a
    # profile photo set (subclassed from photo set) so there is not a
    # simple 1 to 1 mapping here
    tdl_profile_photo_set:db_model.ProfilePhotoSet = attr.ib()
    tdg_profile_photo:tdg.profilePhoto = attr.ib()


@attr.s
class EqualityArgumentFile:
    tdl_file:db_model.File = attr.ib()
    tdg_file:tdg.file = attr.ib()


@attr.s
class EqualityArgumentPhoneNumber:
    phonenumbers_lib_obj:PhoneNumber = attr.ib()
    str_phonenumber:str = attr.ib()

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
    def is_equal_user(self, user_arg:EqualityArgumentUser) -> bool:
        ''' equality test comparing `db_model.User` and `telegram_generated.user`

        '''


        if user_arg.tdl_user is None or user_arg.tdg_user is None:
            logger_user.debug("one of the args is None, doing fast comparison")

            fast_result = user_arg.tdl_user == user_arg.tdg_user

            logger_user.debug("fast result: `%s`", fast_result)

            return fast_result


        user_comparison = user_arg.tdg_user is not None \
            and isinstance(user_arg.tdg_user, tdg.user) \
            and user_arg.tdl_user.tg_user_id == user_arg.tdg_user.id \
            and user_arg.tdl_user.first_name == user_arg.tdg_user.first_name \
            and user_arg.tdl_user.last_name == user_arg.tdg_user.last_name \
            and user_arg.tdl_user.user_name == user_arg.tdg_user.username \
            and user_arg.tdl_user.is_contact == user_arg.tdg_user.is_contact \
            and user_arg.tdl_user.is_mutual_contact == user_arg.tdg_user.is_mutual_contact \
            and user_arg.tdl_user.is_verified == user_arg.tdg_user.is_verified \
            and user_arg.tdl_user.is_support == user_arg.tdg_user.is_support \
            and user_arg.tdl_user.restriction_reason == user_arg.tdg_user.restriction_reason \
            and user_arg.tdl_user.is_scam == user_arg.tdg_user.is_scam \
            and user_arg.tdl_user.have_access == user_arg.tdg_user.have_access \
            and user_arg.tdl_user.user_type == dbme.UserTypeEnum.parse_from_tdg_usertype(user_arg.tdg_user.type) \
            and user_arg.tdl_user.language_code == user_arg.tdg_user.language_code

        # check to see if there
        profile_photo_arg = EqualityArgumentProfilePhoto(
            tdl_profile_photo_set=user_arg.tdl_user.profile_photo_set,
            tdg_profile_photo=user_arg.tdg_user.profile_photo)
        profilephoto_result = self.is_equal(profile_photo_arg)

        # handle where we get a str from telegram but a Phonenumber object from the database
        # or the user has no phone number at all
        phone_args = EqualityArgumentPhoneNumber(
            phonenumbers_lib_obj=user_arg.tdl_user.phone_number,
            str_phonenumber=user_arg.tdg_user.phone_number)

        phoneno_result = self.is_equal(phone_args)


        final = user_comparison and profilephoto_result and phoneno_result

        if not final:
            logger_user.debug("equals_tdg: user result: `%s`, profile photo result: `%s`, phone # result: `%s`",
                user_comparison, profilephoto_result, phoneno_result)

        return final