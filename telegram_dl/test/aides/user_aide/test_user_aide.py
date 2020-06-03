import unittest
import pathlib

import arrow
import phonenumbers

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbe
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides import chat_aide
from telegram_dl.aides.user_aide import UserAide
from telegram_dl.aides.phone_number_aide import PhoneNumberAide
from telegram_dl import constants

class TestUserAide(unittest.TestCase):

    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)


    def test_new_user_from_tdlib_user_equal(self):
        '''
        `UserAide.new_user_from_tdlib_user`, should be equal
        '''

        with u.get_testing_sqla_session_contextmanager() as session:

            # add the db_model.User that this private chat is with, or else it
            # will have a integrity error when we add the chat
            user_json =  u.get_fake_tdlib_messages_path("user/user_id_80661419.json")
            user_obj = u.load_tdlib_generated_obj_from_file(user_json, self.converter)
            self.assertEqual(type(user_obj), tdg.user)
            user_tdlib_obj = UserAide.new_user_from_tdlib_user(session, user_obj)
            session.add(user_tdlib_obj)

            # assertions

            self.assertEquals(user_tdlib_obj.tg_user_id, 80661419)

            self.assertEquals(len(user_tdlib_obj.versions), 1)

            latest_ver = user_tdlib_obj.versions[-1]

            self.assertEquals(latest_ver.first_name, "John")
            self.assertEquals(latest_ver.last_name, "Doe")
            self.assertEquals(latest_ver.user_name, "TestingJohnDoe")

            # NOTE: it seems that the `sqlalchemy_utils.PhoneNumberType` converts
            # a string phone number into a `phonenumbers` object only when its been
            # loaded from the database
            # so that means we should expect the number to be a STRING here
            # but in other tests (like in a `get_user_by_tg_user_id` test) the phone number
            # would be a `phonenumber` object
            expected_phone_number = phonenumbers.parse("+15555555",
                region=constants.PHONE_NUMBER_DEFAULT_REGION)
            phone_number_from_user_parsed_from_str = PhoneNumberAide \
                .parse_phone_number_from_string(latest_ver.phone_number)
            self.assertEquals(type(latest_ver.phone_number), str)
            self.assertEquals(phone_number_from_user_parsed_from_str, expected_phone_number)

            self.assertTrue(latest_ver.is_contact)
            self.assertTrue(latest_ver.is_mutual_contact)
            self.assertFalse(latest_ver.is_verified)
            self.assertFalse(latest_ver.is_support)
            self.assertEquals(latest_ver.restriction_reason, "")
            self.assertFalse(latest_ver.is_scam)
            self.assertTrue(latest_ver.have_access)
            self.assertEquals(latest_ver.language_code, "")
            self.assertEquals(latest_ver.user_type, dbe.UserTypeEnum.USER_TYPE_REGULAR)

            #########################
            # test profile photo set
            #########################

            latest_ver_profile_photo_set = latest_ver.profile_photo_set

            self.assertEqual(len(latest_ver_profile_photo_set.photos), 2)

            self.assertEqual(latest_ver_profile_photo_set.tg_id, 346438157110192450)

            # test big

            # NOTE: we _cannot_ use the `big` and `small` relationship properties here since we
            # created this object manually and have not loaded it from the database, and the relationship
            # is a `primaryjoin` so even though the relationship should exist, they are None at the moment
            # unless we fetch the object fresh from the database again
            big_list = latest_ver_profile_photo_set \
                .get_photos_by_thumnail_type(dbe.PhotoSizeThumbnailType.PHOTO_BIG)
            self.assertEquals(len(big_list), 1)
            big_photo = big_list[0]

            self.assertEqual(big_photo.thumbnail_type, dbe.PhotoSizeThumbnailType.PHOTO_BIG)
            self.assertEqual(big_photo.width, -1)
            self.assertEqual(big_photo.height, -1)
            self.assertFalse(big_photo.has_stickers)

            big_file = big_photo.file

            self.assertEqual(big_file.tg_file_id, 15)
            self.assertEqual(big_file.size, 0)
            self.assertEqual(big_file.expected_size, 0)
            self.assertEqual(big_file.remote_file_id, "AQADAQADXKkxG6vLzgQACLJsEjAABAMAA6vLzgQABHHpJIC1z601EmwAAhgE")
            self.assertEqual(big_file.remote_unique_id, "AQADsmwSMAAEEmwAAg")

            # test small

            # see note above
            small_list = latest_ver_profile_photo_set \
                .get_photos_by_thumnail_type(dbe.PhotoSizeThumbnailType.PHOTO_SMALL)
            self.assertEquals(len(small_list), 1)
            small_photo = small_list[0]

            self.assertEqual(small_photo.thumbnail_type, dbe.PhotoSizeThumbnailType.PHOTO_SMALL)
            self.assertEqual(small_photo.width, -1)
            self.assertEqual(small_photo.height, -1)
            self.assertFalse(small_photo.has_stickers)

            small_file = small_photo.file

            # see note above
            self.assertEqual(small_file.tg_file_id, 14)
            self.assertEqual(small_file.size, 0)
            self.assertEqual(small_file.expected_size, 0)
            self.assertEqual(small_file.remote_file_id, "AQADAQADXKkxG6vLzgQACLJsEjAABAIAA6vLzgQABHHpJIC1z601EGwAAhgE")
            self.assertEqual(small_file.remote_unique_id, "AQADsmwSMAAEEGwAAg")
