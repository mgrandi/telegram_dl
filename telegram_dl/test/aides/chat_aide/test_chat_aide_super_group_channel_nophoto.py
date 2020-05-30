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

class TestChatAideSuperGroupChannelNoPhoto(unittest.TestCase):


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

    def test_compare_tdlib_and_dbmodel_chat_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat`, should be equal
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

    @unittest.skip("TODO")
    def test_get_chat_by_tg_chat_id(self):
        '''
        `ChatAide.get_chat_by_tg_chat_id`, insert chat into database and assert we can get it out
        '''

        pass

    @unittest.skip("TODO")
    def test_new_chat_from_tdlib_chat(self):
        '''
        `ChatAide.new_chat_from_tdlib_chat`, get new `db_model.Chat` from `tdlib_generated.chat`
        '''

        pass

    @unittest.skip("TODO")
    def test_new_chat_version_from_tdlib_chat(self):
        '''
        `ChatAide.new_chat_version_from_tdlib_chat`, get new `db_model.ChatVersion` from `tdlib_generated.chat`
        '''

        pass








