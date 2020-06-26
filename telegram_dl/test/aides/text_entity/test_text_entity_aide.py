import unittest
import pathlib
import typing

import attr

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbme
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides.text_entity_aide import TextEntityAide
from telegram_dl.aides.message_aide import MessageAide
from telegram_dl.aides.chat_aide import ChatAide


@attr.s()
class TextEntityTestParams:
    json_path:typing.Optional[pathlib.Path] = attr.ib()
    te_offset:int = attr.ib()
    te_length:int = attr.ib()
    msg_text:str = attr.ib()
    should_skip:bool = attr.ib()
    te_type:dbme.TextEntityTypeEnum = attr.ib()

class TestTextEntityAide(unittest.TestCase):


    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)

        self.fake_message_prefix = pathlib.Path("message/messageText/textEntities/")

        self.test_params = [
            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_18874368_chat_id_-1001446368458_text_entity_bold.json",
                te_offset=11,
                te_length=4,
                msg_text="TESTING123 BOLD",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_BOLD),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_33554432_chat_id_-1001446368458_text_entity_bot_command.json",
                te_offset=0,
                te_length=6,
                msg_text="/start",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_BOT_COMMAND),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_32505856_chat_id_-1001446368458_text_entity_cashtag.json",
                te_offset=0,
                te_length=4,
                msg_text="$USD CASHTAG TESTING123",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_CASHTAG),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_17825792_chat_id_-1001446368458_text_entity_code.json",
                te_offset=11,
                te_length=12,
                msg_text="TESTING123 preformatted",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_CODE),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_24117248_chat_id_-1001446368458_text_entity_email_address.json",
                te_offset=11,
                te_length=16,
                msg_text="TESTING123 mark@example.com",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_EMAIL_ADDRESS),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_27262976_chat_id_-1001446368458_text_entity_hash_tag.json",
                te_offset=11,
                te_length=8,
                msg_text="testing123 #hashtag",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_HASHTAG),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_19922944_chat_id_-1001446368458_text_entity_italic.json",
                te_offset=11,
                te_length=6,
                msg_text="TESTING123 ITALIC",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_ITALIC),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_31457280_chat_id_-1001446368458_text_entity_mention.json",
                te_offset=4,
                te_length=14,
                msg_text="hey @ExampleUser12 how are you TESTING123",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_MENTION),

            # TODO: get a example of one of these
            TextEntityTestParams(
                json_path=None,
                te_offset=-1,
                te_length=-1,
                msg_text="",
                should_skip=True,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_MENTION_NAME),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_26214400_chat_id_-1001446368458_text_entity_phone_number.json",
                te_offset=11,
                te_length=14,
                msg_text="TESTING123 (415) 555-5555",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_PHONE_NUMBER),

            # TODO: get a example of one of these
            TextEntityTestParams(
                json_path=None,
                te_offset=-1,
                te_length=-1,
                msg_text="",
                should_skip=True,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_PRE),

            # TODO: get a example of one of these
            TextEntityTestParams(
                json_path=None,
                te_offset=-1,
                te_length=-1,
                msg_text="",
                should_skip=True,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_PRE_CODE),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_22020096_chat_id_-1001446368458_text_entity_strikethrough.json",
                te_offset=11,
                te_length=6,
                msg_text="TESTING123 STRIKE",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_STRIKETHROUGH),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_23068672_chat_id_-1001446368458_text_entity_text_url.json",
                te_offset=16,
                te_length=17,
                msg_text="TESTING123 LINK https://zombo.com",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_TEXT_URL),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_20971520_chat_id_-1001446368458_text_entity_underline.json",
                te_offset=11,
                te_length=9,
                msg_text="TESTING123 UNDERLINE",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_UNDERLINE),

            TextEntityTestParams(
                json_path=self.fake_message_prefix / "message_id_46137344_chat_id_-1001446368458_text_entity_url.json",
                te_offset=0,
                te_length=22,
                msg_text="https://html5zombo.com",
                should_skip=False,
                te_type=dbme.TextEntityTypeEnum.TEXT_ENTITY_TYPE_URL),
        ]


    def _add_testing_data_to_session(self, session):
        '''
        Adds testing data that all of the unit tests in this file will use, since all
        of the examples are messages that were sent in a channel (so therefore no user)
        and were all sent within the same chat (a supergroup channel)
        '''

        # load the chat
        path_chat = u.get_fake_tdlib_messages_path("chat/chat_supergroup_id_-1001446368458_channel_no_photo.json")
        tdlib_obj_chat = u.load_tdlib_generated_obj_from_file(path_chat, self.converter)
        self.assertIsInstance(tdlib_obj_chat, tdg.chat)
        chat = ChatAide.new_chat_from_tdlib_chat(session, tdlib_obj_chat)
        session.add(chat)

        session.commit()

    def test_get_text_entities_single_entity_per_message(self):
        '''
        `TextEntityAide.get_text_entity_from_tdlib_text_entity` with the various types of TextEntities
        '''


        for iter_param in self.test_params:

            if not iter_param.should_skip:
                with self.subTest(textEntityType=iter_param.te_type):

                    json_path = self.fake_message_prefix / "message_id_18874368_chat_id_-1001446368458_text_entity_bold.json"
                    message_json =  u.get_fake_tdlib_messages_path(iter_param.json_path)
                    message_obj = u.load_tdlib_generated_obj_from_file(message_json, self.converter)

                    # assert that the loaded type is what we expect
                    self.assertIsInstance(message_obj, tdg.message)

                    with u.get_testing_sqla_session_contextmanager() as session:

                        self._add_testing_data_to_session(session)

                        # Message related assertions, just to be safe
                        loaded_message = MessageAide.new_message_from_tdlib_message(session, message_obj)
                        self.assertEqual(len(loaded_message.versions), 1, "make sure we only have 1 loaded version")
                        message_version = loaded_message.versions[-1]
                        self.assertIsInstance(message_version, db_model.MessageVersionText, "verify db_model.MessageVersion subclass")
                        self.assertEqual(iter_param.msg_text, message_version.text, "verify message text")

                        # Text Entity related assertions

                        loaded_text_entities = TextEntityAide.get_text_entities_from_tdlib_text_entity_sequence(
                            message_version, message_obj.content.text.entities)

                        self.assertEqual(len(loaded_text_entities), 1, "make sure we only have 1 text entity")
                        te = loaded_text_entities[0]
                        self.assertIsInstance(te, db_model.TextEntity, "verify type is db_model.TextEntity")
                        self.assertEqual(te.offset, iter_param.te_offset, "verify TextEntity offset")
                        self.assertEqual(te.length, iter_param.te_length, "verify TextEntity length")
                        self.assertEqual(te.text_entity_type, iter_param.te_type, "verify type of TextEntity")



    @unittest.skip("TODO")
    def test_get_text_entities_multiple_per_message(self):

        pass


    @unittest.skip("TODO")
    def test_compare_dbmodel_and_tdlib_text_entity_sequence(self):
        pass