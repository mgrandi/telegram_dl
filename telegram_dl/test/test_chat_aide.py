import unittest
import pathlib

import arrow

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides import chat_aide

class TestChatAide(unittest.TestCase):


    def test_compare_tdlib_and_dbmodel_chat_supergroup_equal(self):
        '''
        `ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, no photo, should be equal
        '''

        converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(converter)

        p = u.get_fake_tdlib_messages_path("updateNewChat_supergroup_id_1446368458_channel_no_photo.json")
        tdlib_obj = u.load_tdlib_generated_obj_from_file(p, converter)

        asof_time = arrow.utcnow()
        chat_version = db_model.ChatVersion(
            chat_version_id=1,
            as_of=asof_time,
            title="TestingChannel",
            photo_set=None,
            is_sponsored=False)

        chat_dbmodel_obj = db_model.SuperGroupChat(
            super_group_chat_id=1,
            tg_chat_id=-1001446368458,
            tg_super_group_id=1446368458,
            is_channel=True)

        chat_dbmodel_obj.versions.append(chat_version)

        #######################################
        # test our custom created db_model object
        #######################################

        compare_result = chat_aide.ChatAide.compare_tdlib_and_dbmodel_chat(
            dbmodel_chat=chat_dbmodel_obj,
            tdlib_chat=tdlib_obj.chat)

        # make sure the custom created object is what we expect
        self.assertEquals(chat_dbmodel_obj.tg_chat_id, -1001446368458)
        self.assertEquals(chat_dbmodel_obj.tg_super_group_id, 1446368458)
        self.assertTrue(chat_dbmodel_obj.is_channel)

        self.assertEquals(chat_dbmodel_obj.versions[0].title, "TestingChannel")
        self.assertEquals(chat_dbmodel_obj.versions[0].photo_set, None)
        self.assertEquals(chat_dbmodel_obj.versions[0].as_of, asof_time)
        self.assertFalse(chat_dbmodel_obj.versions[0].is_sponsored)

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

        # assert that we correctly compare these as true
        self.assertTrue(compare_result)

