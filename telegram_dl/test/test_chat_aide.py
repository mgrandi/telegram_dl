import unittest
import pathlib

import arrow

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbe
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides import chat_aide

class TestChatAide(unittest.TestCase):


    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)


    def _get_supergroup_channel_chat_nophoto(self, asof_time):

        chat_version = self._get_chat_version(
            asof_time,
            "TestingChannel",
            None,
            False)

        chat_dbmodel_obj = db_model.SuperGroupChat(
            tg_chat_id=-1001446368458,
            tg_super_group_id=1446368458,
            is_channel=True)

        chat_dbmodel_obj.versions.append(chat_version)

        return chat_dbmodel_obj

    def _get_supergroup_channel_chat_photo(self, asof_time):

        chat_version = self._get_chat_version(
            asof_time,
            "TestingChannel",
            self._get_photo_set(),
            False)


        chat_dbmodel_obj = db_model.SuperGroupChat(
            tg_chat_id=-1001446368458,
            tg_super_group_id=1446368458,
            is_channel=True)

        chat_dbmodel_obj.versions.append(chat_version)

        return chat_dbmodel_obj

    def _get_photo_set(self):

        small_file = db_model.File(
            tg_file_id=39,
            size=0,
            expected_size=0,
            remote_file_id="AQADAQATfeJuBgAEAgADNhsl1Rb___999EMQGh7tDwI9AgABGAQ",
            remote_unique_id="AQADfeJuBgAEAj0CAAE")

        big_file = db_model.File(
            tg_file_id=40,
            size=0,
            expected_size=0,
            remote_file_id="AQADAQATfeJuBgAEAwADNhsl1Rb___999EMQGh7tDwQ9AgABGAQ",
            remote_unique_id="AQADfeJuBgAEBD0CAAE")

        new_photo_set = db_model.PhotoSet()

        small_photo = db_model.Photo(
            thumbnail_type=dbe.PhotoSizeThumbnailType.PHOTO_SMALL,
            width=-1,
            height=-1,
            has_stickers=False,
            file=small_file)

        big_photo = db_model.Photo(
            thumbnail_type=dbe.PhotoSizeThumbnailType.PHOTO_BIG,
            width=-1,
            height=-1,
            has_stickers=False,
            file=big_file)

        new_photo_set.photos.append(big_photo)
        new_photo_set.photos.append(small_photo)

        return new_photo_set

    def _get_chat_version(self, asof_time, name, photo_set, is_sponsored):


        chat_version = db_model.ChatVersion(
            as_of=asof_time,
            title=name,
            photo_set=photo_set,
            is_sponsored=is_sponsored)

        return chat_version


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################


    def test_compare_chat_supergroup_channel_nophoto_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, no photo, should be equal
        '''

        p = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001446368458_channel_no_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        # create the db_model objects from JSON

        asof_time = arrow.utcnow()
        chat_dbmodel_obj = self._get_supergroup_channel_chat_nophoto(asof_time)

        # assert that we correctly compare these as true

        compare_result = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj)

        self.assertTrue(compare_result)


    def test_compare_chat_supergroup_channel_photo_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, photo, should be equal
        '''
        p = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001446368458_channel_has_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        # create the db_model objects from JSON

        asof_time = arrow.utcnow()
        chat_dbmodel_obj = self._get_supergroup_channel_chat_photo(asof_time)

        # assert that we correctly compare these as true

        compare_result = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj)

        self.assertTrue(compare_result)


    def test_compare_multiple_chat_versions_supergroup(self):
        '''
        chat with multiple versions, checking against the most recent version

        NOTE: this is not fully testing the `relationship` of the Chat -> ChatVersion
        (the `versions` field), since when loading from the database it will sort by the
        `ChatVersion.as_of` field

        so theoretically we could do `Chat.versions.insert(0, chat_ver_obj)`
        (instead of `append()`) and that will insert it at index 0, even if the
        `chat_ver_obj` is not the earliest ChatVersion (by the `as_of` field),
        but since we aren't loading it from the database, sqlalchemy doesn't
        re-sort it for us or anything
        '''

        asof_time = arrow.utcnow()

        chat_dbmodel_obj = self._get_supergroup_channel_chat_photo(asof_time)


        p = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001446368458_channel_has_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        # so we have a Chat (Supergroup) with a photo, it should equal the message that we loaded
        # from the JSON

        compare_result_one = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj)

        self.assertEqual(len(chat_dbmodel_obj.versions), 1)
        # has a photo to start out with
        self.assertNotEqual(chat_dbmodel_obj.versions[-1].photo_set, None)
        self.assertTrue(compare_result_one)

        # now add a chat version where we 'remove' the photo
        # and add it as a version
        chat_ver_no_photo = self._get_chat_version(arrow.now(), "TestingChannel", None, False)

        chat_dbmodel_obj.versions.append(chat_ver_no_photo)

        # now the compare method should return as not equal
        compare_result_two = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj)

        self.assertEqual(len(chat_dbmodel_obj.versions), 2)
        # does not have a photo for this one
        self.assertEqual(chat_dbmodel_obj.versions[-1].photo_set, None)
        self.assertFalse(compare_result_two)

        # if we add another version that should be the same as the "first" version
        # (has the same photo), then it should compare as equal again
        chat_ver_photo_two = self._get_chat_version(arrow.now(), "TestingChannel", self._get_photo_set(), False)

        chat_dbmodel_obj.versions.append(chat_ver_photo_two)

        compare_result_three = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj)

        self.assertEqual(len(chat_dbmodel_obj.versions), 3)
        # has a photo
        self.assertNotEqual(chat_dbmodel_obj.versions[-1].photo_set, None)
        self.assertTrue(compare_result_three)


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################


    def test_get_chat_by_tg_chat_id_multiple_chats(self):
        '''
        insert multiple chats into the database and call `ChatAide.get_chat_by_tg_chat_id` on the IDs

        '''

        with u.get_testing_sqla_session_contextmanager() as session:

            chat_one = self._get_supergroup_channel_chat_photo(arrow.now())
            session.add(chat_one)

            p = u.get_fake_tdlib_messages_path("chat/chat_basic_group_id_-423872019_no_photo.json")
            tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)
            self.assertEqual(type(tdlib_obj), tdg.chat)
            chat_two = chat_aide.ChatAide.new_chat_from_tdlib_chat(session, tdlib_obj)
            session.add(chat_two)

            p2 = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001266163180_no_photo.json")
            tdlib_obj2 = u.load_tdlib_generated_obj_from_file(p2, self.converter)
            self.assertEquals(type(tdlib_obj2), tdg.chat)
            chat_three = chat_aide.ChatAide.new_chat_from_tdlib_chat(session, tdlib_obj2)
            session.add(chat_three)


            # now make sure we can get all 3 chats

            session.commit()

            result_chat_one = chat_aide.ChatAide.get_chat_by_tg_chat_id(session, -1001446368458)
            self.assertEquals(result_chat_one.tg_chat_id, -1001446368458)
            self.assertEquals(len(result_chat_one.versions), 1)
            self.assertEquals(result_chat_one.versions[0].title, "TestingChannel")

            result_chat_two = chat_aide.ChatAide.get_chat_by_tg_chat_id(session, -423872019)
            self.assertEquals(result_chat_two.tg_chat_id, -423872019)
            self.assertEquals(len(result_chat_two.versions), 1)
            self.assertEquals(result_chat_two.versions[0].title, "telegram_dl development")

            result_chat_three = chat_aide.ChatAide.get_chat_by_tg_chat_id(session, -1001266163180)
            self.assertEquals(result_chat_three.tg_chat_id, -1001266163180)
            self.assertEquals(len(result_chat_three.versions), 1)
            self.assertEquals(result_chat_three.versions[0].title, "TGS stuff")




