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

class TestChatAideBasicGroupNoPhoto(unittest.TestCase):

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

            p3 = u.get_fake_tdlib_messages_path("chat/chat_basic_group_id_-423872019_no_photo.json")
            tdlib_obj3 = u.load_tdlib_generated_obj_from_file(p3, self.converter)
            self.assertIsInstance(tdlib_obj3, tdg.chat)
            chat_three = chat_aide.ChatAide.new_chat_from_tdlib_chat(session, tdlib_obj3)
            session.add(chat_three)

            session.commit()

            result_chat_three = chat_aide.ChatAide.get_chat_by_tg_chat_id(session, -423872019)
            self.assertEqual(result_chat_three.tg_chat_id, -423872019)
            self.assertEqual(len(result_chat_three.versions), 1)
            self.assertIsInstance(result_chat_three, db_model.BasicGroupChat)
            self.assertEqual(result_chat_three.versions[0].title, "telegram_dl development")


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
