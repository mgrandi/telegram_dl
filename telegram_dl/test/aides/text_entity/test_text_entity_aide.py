import unittest

from telegram_dl import utils
from telegram_dl import tdlib_generated as tdg
from telegram_dl import db_model_enums as dbe
from telegram_dl import db_model
from telegram_dl.test import utilities as u
from telegram_dl.aides.text_entity_aide import TextEntityAide

class TestTextEntityAide(unittest.TestCase):


    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)

        self.fake_message_prefix = pathlib.Path("message/messageText/textEntities/")

    def test_get_text_entity_from_tdlib_text_entity(self):

        pass
        # json_path = fake_message_prefix / "message_id_47185920_chat_id_-1001446368458_multiple_text_entities.json"
        # message_json =  u.get_fake_tdlib_messages_path(json_path)
        # message_obj = u.load_tdlib_generated_obj_from_file(message_json, self.converter)
        # self.assertEqual(type(message_obj), tdg.message)




    def test_get_text_entities_from_tdlib_text_entity_sequence(self):

        pass
