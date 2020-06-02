import unittest
import pathlib
import unittest

import arrow

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbe
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides import chat_aide
from telegram_dl.aides.user_aide import UserAide
from telegram_dl import constants

class TestChatAidePrivateChatPhoto(unittest.TestCase):

    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)

    @unittest.skip("TODO")
    def test_compare_tdlib_and_dbmodel_chat_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat`, should be equal
        '''

        pass

    @unittest.skip("TODO")
    def test_compare_tdlib_and_dbmodel_chat_not_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat`, should be NOT equal
        '''

        pass

    @unittest.skip("TODO")
    def test_compare_tdlib_and_dbmodel_chat_multiple_chat_versions(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat`, with multiple `db_model.ChatVersion` objects
        '''

        pass

    def test_get_chat_by_tg_chat_id(self):
        '''
        `ChatAide.get_chat_by_tg_chat_id`, insert chat into database and assert we can get it out
        '''

        with u.get_testing_sqla_session_contextmanager() as session:

            # add the db_model.User that this private chat is with, or else it
            # will have a integrity error when we add the chat
            user_json =  u.get_fake_tdlib_messages_path("user/user_id_80661419.json")
            user_obj = u.load_tdlib_generated_obj_from_file(user_json, self.converter)
            self.assertEqual(type(user_obj), tdg.user)
            user_tdlib_obj = UserAide.new_user_from_tdlib_user(session, user_obj)
            session.add(user_tdlib_obj)


            # add the db_model.PrivateChat
            p4 = u.get_fake_tdlib_messages_path("chat/chat_private_id_80661419_has_photo.json")
            tdlib_obj4 = u.load_tdlib_generated_obj_from_file(p4, self.converter)
            self.assertEqual(type(tdlib_obj4), tdg.chat)
            chat_four = chat_aide.ChatAide.new_chat_from_tdlib_chat(session, tdlib_obj4)
            session.add(chat_four)

            # commit it
            session.commit()

            # do assertions
            result_chat_four = chat_aide.ChatAide.get_chat_by_tg_chat_id(session, 80661419)
            self.assertEquals(result_chat_four.tg_chat_id, 80661419)
            self.assertEquals(len(result_chat_four.versions), 1)
            self.assertEquals(type(result_chat_four), db_model.PrivateChat)
            self.assertEquals(result_chat_four.versions[0].title, "John Smith")

    def test_new_chat_from_tdlib_chat(self):
        '''
        `ChatAide.new_chat_from_tdlib_chat`, get new `db_model.Chat` from `tdlib_generated.chat`
        '''

        with u.get_testing_sqla_session_contextmanager() as session:

            # add the db_model.User that this private chat is with, or else it
            # will have a integrity error when we add the chat
            user_json =  u.get_fake_tdlib_messages_path("user/user_id_80661419.json")
            user_obj = u.load_tdlib_generated_obj_from_file(user_json, self.converter)
            self.assertEqual(type(user_obj), tdg.user)
            user_tdlib_obj = UserAide.new_user_from_tdlib_user(session, user_obj)
            session.add(user_tdlib_obj)

            # add the db_model.PrivateChat
            p = u.get_fake_tdlib_messages_path("chat/chat_private_id_80661419_has_photo.json")
            tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

            self.assertEqual(type(tdlib_obj), tdg.chat)

            db_model_chat_obj = chat_aide.ChatAide.new_chat_from_tdlib_chat(session, tdlib_obj)

            # assertions
            self.assertEquals(type(db_model_chat_obj), db_model.PrivateChat)

            self.assertEquals(db_model_chat_obj.tg_chat_id, 80661419)

            self.assertEquals(len(db_model_chat_obj.versions), 1)

            latest_ver = db_model_chat_obj.versions[-1]

            self.assertEquals(latest_ver.title, "John Smith")
            self.assertFalse(latest_ver.is_sponsored )

            ##################################
            # test the photo set
            ##################################

            latest_ver_photo_set = latest_ver.photo_set

            self.assertEqual(len(latest_ver_photo_set.photos), 2)

            # big chat photo
            big_list = latest_ver_photo_set \
                .get_photos_by_thumnail_type(dbe.PhotoSizeThumbnailType.PHOTO_BIG)
            self.assertEquals(len(big_list), 1)
            big_photo = big_list[0]

            self.assertEqual(big_photo.thumbnail_type, dbe.PhotoSizeThumbnailType.PHOTO_BIG)
            self.assertEqual(big_photo.width, -1)
            self.assertEqual(big_photo.height, -1)
            self.assertFalse(big_photo.has_stickers)

            big_file = big_photo.file

            # NOTE: so this seems weird, since if you look at the JSON, the `file.id` for this
            # is clearly 30 (and 29 for the user), but since a Private Chat is between you
            # and another user, the photo is the other user's profile photo.
            # so since we have to add the user that this chat is with to the database session
            # (or else we get an integrity error), the `file.id` is actually of the file of the
            # user's photo , and therefore in the user json rather than the chat json
            # however the remote_file_id and remote_unique_id should be the same!
            self.assertEqual(big_file.tg_file_id, 15)
            self.assertEqual(big_file.size, 0)
            self.assertEqual(big_file.expected_size, 0)
            self.assertEqual(big_file.remote_file_id, "AQADAQADXKkxG6vLzgQACLJsEjAABAMAA6vLzgQABHHpJIC1z601EmwAAhgE")
            self.assertEqual(big_file.remote_unique_id, "AQADsmwSMAAEEmwAAg")

            # small chat photo
            small_list = latest_ver_photo_set \
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



    @unittest.skip("TODO")
    def test_new_chat_version_from_tdlib_chat(self):
        '''
        `ChatAide.new_chat_version_from_tdlib_chat`, get new `db_model.ChatVersion` from `tdlib_generated.chat`
        '''

        pass


    @unittest.skip("TODO")
    def test_private_chat_photo_matches_user_photo(self):

        # since a private chat photo basically is the same exact photo as the user's current photo
        # assert that if a user photo is the same the private chat photo and that it matches when changed

        # taken from `test_new_chat_from_tdlib_chat` above:
        #
        # NOTE: so this seems weird, since if you look at the JSON, the `file.id` for this
        # is clearly 30 (and 29 for the user), but since a Private Chat is between you
        # and another user, the photo is the other user's profile photo.
        # so since we have to add the user that this chat is with to the database session
        # (or else we get an integrity error), the `file.id` is actually of the file of the
        # user's photo , and therefore in the user json rather than the chat json
        # however the remote_file_id and remote_unique_id should be the same!

        pass
