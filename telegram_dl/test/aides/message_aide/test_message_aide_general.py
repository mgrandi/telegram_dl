import unittest
import pathlib
import unittest

import arrow

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbe
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides.chat_aide import ChatAide
from telegram_dl.aides.user_aide import UserAide
from telegram_dl.aides.message_aide import MessageAide

class TestMessageAideGeneral(unittest.TestCase):

    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)


    def test_get_message_by_tg_message_and_chat_id(self):

        # TODO: TEST TO MAKE SURE THAT TWO MESSAGES WITH THE SAME ID
        # BUT IN DIFFERENT CHATS ARE TESTED


        with u.get_testing_sqla_session_contextmanager() as session:

            # add the db_model.User that this private chat is with, or else it
            # will have a integrity error when we add the chat
            message_json =  u.get_fake_tdlib_messages_path("message/messageText/message_id_599515987968_chat_id_80661419_message_text.json")
            message_tdlib_obj = u.load_tdlib_generated_obj_from_file(message_json, self.converter)
            self.assertIsInstance(message_tdlib_obj, tdg.message)
            self.assertIsInstance(message_tdlib_obj.content, tdg.messageText)

            # load user
            user_json_path =  u.get_fake_tdlib_messages_path("user/user_id_80661419.json")
            user_obj = u.load_tdlib_generated_obj_from_file(user_json_path, self.converter)
            self.assertIsInstance(user_obj, tdg.user)
            user_dbmodel_obj = UserAide.new_user_from_tdlib_user(session, user_obj)
            session.add(user_dbmodel_obj)
            session.commit()
            self.assertEqual(user_dbmodel_obj.tg_user_id, 80661419)

            # load chat

            chat_json_path = u.get_fake_tdlib_messages_path("chat/chat_private_id_80661419_has_photo.json")
            chat_tdlib_obj = u.load_tdlib_generated_obj_from_file(chat_json_path, self.converter)
            self.assertIsInstance(chat_tdlib_obj, tdg.chat)
            chat_dbmodel_obj = ChatAide.new_chat_from_tdlib_chat(session, chat_tdlib_obj)
            session.add(chat_dbmodel_obj)
            session.commit()

            # save and load message

            message_dbmodel_obj = MessageAide.new_message_from_tdlib_message(session, message_tdlib_obj)

            session.add(message_dbmodel_obj)
            session.commit()

            retrieved_message_dbmodel_obj = MessageAide.get_message_by_tg_message_and_chat_id(
                session, 599515987968, 80661419)

            # message assertions
            self.assertEqual(retrieved_message_dbmodel_obj.tg_message_id, 599515987968)
            self.assertTrue(retrieved_message_dbmodel_obj.is_outgoing)
            self.assertFalse(retrieved_message_dbmodel_obj.is_channel_post)
            self.assertTrue(retrieved_message_dbmodel_obj.can_edit)
            self.assertTrue(retrieved_message_dbmodel_obj.can_forward)
            self.assertTrue(retrieved_message_dbmodel_obj.can_be_deleted_only_for_self)
            self.assertFalse(retrieved_message_dbmodel_obj.can_be_deleted_for_all_users)
            self.assertEqual(retrieved_message_dbmodel_obj.restriction_reason, "")

            self.assertIsNone(retrieved_message_dbmodel_obj.via_bot_user)
            self.assertIsNone(retrieved_message_dbmodel_obj.reply_to_message)

            self.assertEqual(retrieved_message_dbmodel_obj.sender_user.user_id, user_dbmodel_obj.user_id)
            self.assertEqual(retrieved_message_dbmodel_obj.chat.chat_id, chat_dbmodel_obj.chat_id)

            self.assertEqual(len(retrieved_message_dbmodel_obj.versions), 1)




