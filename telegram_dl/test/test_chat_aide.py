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


    def _assert_common_dbmodel_chat_fields(self, asof_time, dbmodel_chat, tdlib_chat, check_photo):
        '''
        helper so we don't have to copy and paste the same assert statements
        for all 4 chat types
        '''

        #######################################
        # db_model.Chat common checks
        #######################################
        self.assertEquals(dbmodel_chat.tg_chat_id, -1001446368458)

        # chat versions
        self.assertEquals(len(dbmodel_chat.versions), 1)

        self.assertEquals(dbmodel_chat.versions[0].title, "TestingChannel")
        self.assertEquals(dbmodel_chat.versions[0].as_of, asof_time)
        self.assertFalse(dbmodel_chat.versions[0].is_sponsored)


        if check_photo:

            # test photo set

            # test photo set - small photo
            s_photo_list = dbmodel_chat.versions[0].photo_set.get_photos_by_thumnail_type(
                dbe.PhotoSizeThumbnailType.PHOTO_SMALL)

            self.assertEquals(len(s_photo_list), 1)

            self.assertEquals(s_photo_list[0].thumbnail_type, dbe.PhotoSizeThumbnailType.PHOTO_SMALL)
            self.assertEquals(s_photo_list[0].width, -1)
            self.assertEquals(s_photo_list[0].height, -1)
            self.assertEquals(s_photo_list[0].has_stickers, False)

            # test photo set - small photo - file
            self.assertEquals(s_photo_list[0].file.tg_file_id, 39)
            self.assertEquals(s_photo_list[0].file.size, 0)
            self.assertEquals(s_photo_list[0].file.expected_size, 0)

            # test photo set - big photo
            b_photo_list = dbmodel_chat.versions[0].photo_set.get_photos_by_thumnail_type(
                dbe.PhotoSizeThumbnailType.PHOTO_BIG)

            self.assertEquals(len(b_photo_list), 1)

            self.assertEquals(b_photo_list[0].thumbnail_type, dbe.PhotoSizeThumbnailType.PHOTO_BIG)
            self.assertEquals(b_photo_list[0].width, -1)
            self.assertEquals(b_photo_list[0].height, -1)
            self.assertEquals(b_photo_list[0].has_stickers, False)

            # test photo set - small photo - file
            self.assertEquals(b_photo_list[0].file.tg_file_id, 40)
            self.assertEquals(b_photo_list[0].file.size, 0)
            self.assertEquals(b_photo_list[0].file.expected_size, 0)


        #######################################
        # tdlib_generated common checks
        #######################################


        # test to make sure the object is the type we expect
        self.assertTrue(isinstance(tdlib_chat, tdg.chat))

        self.assertEquals(tdlib_chat.id, -1001446368458)
        self.assertEquals(tdlib_chat.title, "TestingChannel")


        if check_photo:
            # test photo

            self.assertEquals(tdlib_chat.photo.small.id, 39)
            self.assertEquals(tdlib_chat.photo.small.size, 0)
            self.assertEquals(tdlib_chat.photo.small.expected_size, 0)
            self.assertEquals(tdlib_chat.photo.small.remote.id, "AQADAQATfeJuBgAEAgADNhsl1Rb___999EMQGh7tDwI9AgABGAQ")
            self.assertEquals(tdlib_chat.photo.small.remote.unique_id, "AQADfeJuBgAEAj0CAAE")

            self.assertEquals(tdlib_chat.photo.big.id, 40)
            self.assertEquals(tdlib_chat.photo.big.size, 0)
            self.assertEquals(tdlib_chat.photo.big.expected_size, 0)
            self.assertEquals(tdlib_chat.photo.big.remote.id, "AQADAQATfeJuBgAEAwADNhsl1Rb___999EMQGh7tDwQ9AgABGAQ")
            self.assertEquals(tdlib_chat.photo.big.remote.unique_id, "AQADfeJuBgAEBD0CAAE")

#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################


    def test_load_supergroup_channel_from_file_photo(self):
        '''
        loading a `db_model.SuperGroupChat`, has photo
        '''

        p = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001446368458_channel_has_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        # create the db_model objects from JSON

        asof_time = arrow.utcnow()
        chat_dbmodel_obj = self._get_supergroup_channel_chat_photo(asof_time)

        # test our custom created db_model object

        # supergroup / channel specific stuff
        self.assertEquals(chat_dbmodel_obj.tg_super_group_id, 1446368458)
        self.assertTrue(chat_dbmodel_obj.is_channel)

        # assert common fields
        self._assert_common_dbmodel_chat_fields(asof_time, chat_dbmodel_obj, tdlib_obj, True)

        # make sure the object we loaded from JSON is what we expect

        # the `chat.type` fields
        self.assertEquals(type(tdlib_obj.type), tdg.chatTypeSupergroup)
        self.assertEquals(tdlib_obj.type.supergroup_id, 1446368458)
        self.assertTrue(tdlib_obj.type.is_channel)


    def test_load_supergroup_channel_from_file_no_photo(self):
        '''
        loading a `db_model.SuperGroupChat`, no photo
        '''

        p = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001446368458_channel_no_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        # create the db_model objects from JSON

        asof_time = arrow.utcnow()
        chat_dbmodel_obj = self._get_supergroup_channel_chat_nophoto(asof_time)

        # test our custom created db_model object

        # supergroup / channel specific stuff
        self.assertEquals(chat_dbmodel_obj.tg_super_group_id, 1446368458)
        self.assertTrue(chat_dbmodel_obj.is_channel)

        # assert common fields
        self._assert_common_dbmodel_chat_fields(asof_time, chat_dbmodel_obj, tdlib_obj, False)

        # make sure the object we loaded from JSON is what we expect

        # the `chat.type` fields
        self.assertEquals(type(tdlib_obj.type), tdg.chatTypeSupergroup)
        self.assertEquals(tdlib_obj.type.supergroup_id, 1446368458)
        self.assertTrue(tdlib_obj.type.is_channel)



    # TODO FIXME: do i even need any of these `test load` unit tests?
    # does it really make sense to test the fake tdlib messags files?
    # maybe i should just get rid of them...

    @unittest.skip("not finished yet")
    def test_load_basic_group_from_file_no_photo(self):
        '''
        loading a `db_model.BasicGroupChat`, no photo
        '''
        pass

    @unittest.skip("not finished yet")
    def test_load_basic_group_from_file_has_photo(self):
        '''
        loading a `db_model.BasicGroupChat`, has photo
        '''
        pass

    @unittest.skip("not finished yet")
    def test_load_secret_chat_from_file(self):
        pass

    @unittest.skip("not finished yet")
    def test_load_secret_chat_from_file(self):
        pass


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




