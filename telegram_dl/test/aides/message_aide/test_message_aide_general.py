import unittest
import pathlib
import unittest
import typing

import arrow
import attr

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbme
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides.chat_aide import ChatAide
from telegram_dl.aides.user_aide import UserAide
from telegram_dl.aides.message_aide import MessageAide


@attr.s
class AttributeToModify:
    attr_name:str = attr.ib()
    attr_value:typing.Any = attr.ib()

class TestMessageAideGeneral(unittest.TestCase):

    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)


    def _load_user_and_chat_id_80661419(self, session, commit_to_db=True):
        '''
        helper function that loads the db_model.User and
        db_model.Chat for user / chat id `80661419` which we need if we want to
        test messages

        if commit_to_db is true, we add it to the database and commit it
        '''

        # load user
        user_json_path =  u.get_fake_tdlib_messages_path("user/user_id_80661419.json")
        user_obj = u.load_tdlib_generated_obj_from_file(user_json_path, self.converter)
        self.assertIsInstance(user_obj, tdg.user)
        user_dbmodel_obj = UserAide.new_user_from_tdlib_user(session, user_obj)
        self.assertEqual(user_dbmodel_obj.tg_user_id, 80661419)

        if commit_to_db:
            session.add(user_dbmodel_obj)
            session.commit()

        # load chat
        chat_json_path = u.get_fake_tdlib_messages_path("chat/chat_private_id_80661419_has_photo.json")
        chat_tdlib_obj = u.load_tdlib_generated_obj_from_file(chat_json_path, self.converter)
        self.assertIsInstance(chat_tdlib_obj, tdg.chat)
        chat_dbmodel_obj = ChatAide.new_chat_from_tdlib_chat(session, chat_tdlib_obj)
        self.assertEqual(chat_dbmodel_obj.tg_chat_id, 80661419)

        if commit_to_db:
            session.add(chat_dbmodel_obj)
            session.commit()


    def _load_and_return_message_id_599515987968(self, session, commit_to_db=True):
        '''
        helper function that loads the db_model.Message for message id `599515987968`
        and returns the resulting db_model.Message object

        if commit_to_db is true, we add it to the database and commit it
        '''

        # load message from JSON
        message_json =  u.get_fake_tdlib_messages_path("message/messageText/message_id_599515987968_chat_id_80661419_message_text.json")
        message_tdlib_obj = u.load_tdlib_generated_obj_from_file(message_json, self.converter)
        self.assertIsInstance(message_tdlib_obj, tdg.message)
        self.assertIsInstance(message_tdlib_obj.content, tdg.messageText)
        message_dbmodel_obj = MessageAide.new_message_from_tdlib_message(session, message_tdlib_obj)

        if commit_to_db:
            session.add(message_dbmodel_obj)
            session.commit()

        return message_dbmodel_obj

    def test_get_message_by_tg_message_and_chat_id(self):
        '''
        test `MessageAide.get_message_by_tg_message_and_tg_chat_id`
        but not anything relating to db_model.MessageVersion or
        tdlib_generated.MessageContent
        '''

        with u.get_testing_sqla_session_contextmanager() as session:

            # add the db_model.User and db_model.Chat that this private chat is with, or else it
            # will have a integrity error when we add the chat
            self._load_user_and_chat_id_80661419(session, commit_to_db=True)

            # load message
            initial_message_obj = self._load_and_return_message_id_599515987968(session, commit_to_db=True)

            # retrieve the message again from the database
            retrieved_message_dbmodel_obj = MessageAide.get_message_by_tg_message_and_tg_chat_id(
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

            self.assertEqual(retrieved_message_dbmodel_obj.sender_user.tg_user_id, 80661419)
            self.assertEqual(retrieved_message_dbmodel_obj.chat.tg_chat_id, 80661419)

            # not testing MessageVersion assertions in this test since we just want to
            # test the 'MessageAide.get_message_by_tg_message_and_tg_chat_id' method


    @unittest.skip("TODO")
    def test_get_message_same_message_id_different_chat_id(self):
        '''
        test `MessageAide.get_message_by...` with two messages, same message id, differnet chat id
        '''
        pass




    def test_compare_dbmodel_and_tdlib_message(self):
        '''
        test `MessageAide.compare_dbmodel_and_tdlib_message` for general Message stuff
        not for anything in db_model.MessageVersion / tdlib_generated.MessageContent
        '''
        message_json =  u.get_fake_tdlib_messages_path("message/messageText/message_id_599515987968_chat_id_80661419_message_text.json")
        message_tdlib_obj = u.load_tdlib_generated_obj_from_file(message_json, self.converter)

        with u.get_testing_sqla_session_contextmanager() as session:

            # add the db_model.User and db_model.Chat that this private chat is with, or else it
            # will have a integrity error when we add the chat
            self._load_user_and_chat_id_80661419(session, commit_to_db=True)


            # do the initial load of the first message
            initial_dbmodel_message_obj = self._load_and_return_message_id_599515987968(session, commit_to_db=True)

            # assert that the db_model.Message and tdlib_generated.message are equal

            is_equal_unmodified_message = MessageAide.compare_dbmodel_and_tdlib_message(
                initial_dbmodel_message_obj, message_tdlib_obj)

            self.assertTrue(is_equal_unmodified_message, "unmodified message should be equal")

            # do a second load but DON'T commit it since we are going to be modifying it
            modified_dbmodel_message_obj = self._load_and_return_message_id_599515987968(session, commit_to_db=False)


            attributes_to_modify = [
                AttributeToModify(attr_name="is_outgoing", attr_value=False)
            ]

            for iter_attr_to_mod in attributes_to_modify:

                old_value = getattr(modified_dbmodel_message_obj, iter_attr_to_mod.attr_name)

                setattr(modified_dbmodel_message_obj, iter_attr_to_mod.attr_name, iter_attr_to_mod.attr_value)

                is_equal_with_modified_message = MessageAide.compare_dbmodel_and_tdlib_message(
                    modified_dbmodel_message_obj, message_tdlib_obj)

                self.assertFalse(is_equal_with_modified_message, "modified message should not be equal")

