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


    def test_compare_chat_supergroup_channel_nophoto_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, no photo, should be equal
        '''

        p = u.get_fake_tdlib_messages_path("updateNewChat_supergroup_id_1446368458_channel_no_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        #######################################
        # create the db_model objects
        #######################################

        asof_time = arrow.utcnow()

        chat_version = db_model.ChatVersion(
            as_of=asof_time,
            title="TestingChannel",
            photo_set=None,
            is_sponsored=False)

        chat_dbmodel_obj = db_model.SuperGroupChat(
            tg_chat_id=-1001446368458,
            tg_super_group_id=1446368458,
            is_channel=True)

        chat_dbmodel_obj.versions.append(chat_version)

        #######################################
        # test our custom created db_model object
        #######################################

        self.assertEquals(chat_dbmodel_obj.tg_chat_id, -1001446368458)
        self.assertEquals(chat_dbmodel_obj.tg_super_group_id, 1446368458)
        self.assertTrue(chat_dbmodel_obj.is_channel)

        self.assertEquals(len(chat_dbmodel_obj.versions), 1)

        self.assertEquals(chat_dbmodel_obj.versions[0].title, "TestingChannel")
        self.assertEquals(chat_dbmodel_obj.versions[0].as_of, asof_time)
        self.assertFalse(chat_dbmodel_obj.versions[0].is_sponsored)
        self.assertEquals(chat_dbmodel_obj.versions[0].photo_set, None)


        #######################################
        # make sure the object we loaded from JSON is what we expect
        #######################################

        # test to make sure the object is the type we expect
        self.assertTrue(isinstance(tdlib_obj, tdg.updateNewChat))

        self.assertEquals(tdlib_obj.chat.id, -1001446368458)
        self.assertEquals(tdlib_obj.chat.title, "TestingChannel")
        self.assertEquals(tdlib_obj.chat.photo, None)

        # the `chat.type` fields
        self.assertEquals(type(tdlib_obj.chat.type), tdg.chatTypeSupergroup)
        self.assertEquals(tdlib_obj.chat.type.supergroup_id, 1446368458)
        self.assertTrue(tdlib_obj.chat.type.is_channel)

        #######################################
        # assert that we correctly compare these as true
        #######################################

        compare_result = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj.chat)

        self.assertTrue(compare_result)

    def test_compare_chat_supergroup_channel_photo_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, photo, should be equal
        '''
        p = u.get_fake_tdlib_messages_path("updateNewChat_supergroup_id_1446368458_channel_has_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, self.converter)

        #######################################
        # create the db_model objects
        #######################################

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

        asof_time = arrow.utcnow()

        chat_version = db_model.ChatVersion(
            as_of=asof_time,
            title="TestingChannel",
            photo_set=new_photo_set,
            is_sponsored=False)

        chat_dbmodel_obj = db_model.SuperGroupChat(
            tg_chat_id=-1001446368458,
            tg_super_group_id=1446368458,
            is_channel=True)

        chat_dbmodel_obj.versions.append(chat_version)

        #######################################
        # test our custom created db_model object
        #######################################

        self.assertEquals(chat_dbmodel_obj.tg_chat_id, -1001446368458)
        self.assertEquals(chat_dbmodel_obj.tg_super_group_id, 1446368458)
        self.assertTrue(chat_dbmodel_obj.is_channel)

        self.assertEquals(len(chat_dbmodel_obj.versions), 1)

        self.assertEquals(chat_dbmodel_obj.versions[0].title, "TestingChannel")
        self.assertEquals(chat_dbmodel_obj.versions[0].as_of, asof_time)
        self.assertFalse(chat_dbmodel_obj.versions[0].is_sponsored)

        # test photo set

        # test photo set - small photo
        s_photo_list = chat_dbmodel_obj.versions[0].photo_set.get_photos_by_thumnail_type(
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
        b_photo_list = chat_dbmodel_obj.versions[0].photo_set.get_photos_by_thumnail_type(
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
        # make sure the object we loaded from JSON is what we expect
        #######################################

        # test to make sure the object is the type we expect
        self.assertTrue(isinstance(tdlib_obj, tdg.updateNewChat))

        self.assertEquals(tdlib_obj.chat.id, -1001446368458)
        self.assertEquals(tdlib_obj.chat.title, "TestingChannel")

        # test photo
        self.assertEquals(tdlib_obj.chat.photo.small.id, 39)
        self.assertEquals(tdlib_obj.chat.photo.small.size, 0)
        self.assertEquals(tdlib_obj.chat.photo.small.expected_size, 0)
        self.assertEquals(tdlib_obj.chat.photo.small.remote.id, "AQADAQATfeJuBgAEAgADNhsl1Rb___999EMQGh7tDwI9AgABGAQ")
        self.assertEquals(tdlib_obj.chat.photo.small.remote.unique_id, "AQADfeJuBgAEAj0CAAE")




        self.assertEquals(tdlib_obj.chat.photo.big.id, 40)
        self.assertEquals(tdlib_obj.chat.photo.big.size, 0)
        self.assertEquals(tdlib_obj.chat.photo.big.expected_size, 0)
        self.assertEquals(tdlib_obj.chat.photo.big.remote.id, "AQADAQATfeJuBgAEAwADNhsl1Rb___999EMQGh7tDwQ9AgABGAQ")
        self.assertEquals(tdlib_obj.chat.photo.big.remote.unique_id, "AQADfeJuBgAEBD0CAAE")


        # the `chat.type` fields
        self.assertEquals(type(tdlib_obj.chat.type), tdg.chatTypeSupergroup)
        self.assertEquals(tdlib_obj.chat.type.supergroup_id, 1446368458)
        self.assertTrue(tdlib_obj.chat.type.is_channel)

        #######################################
        # assert that we correctly compare these as true
        #######################################

        compare_result = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj.chat)

        self.assertTrue(compare_result)