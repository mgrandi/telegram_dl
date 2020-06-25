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

class TestMessageAideMessageContentTypeMessageText(unittest.TestCase):
    '''
    tests for `message_aide` that deal with messages that have a
    `messageContent` type of `tdlib_generated.messageText`

    '''

    def setUp(self):

        self.converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(self.converter)

    @unittest.skip("TODO")
    def test_new_message_from_tdlib_message(self):
        pass

    @unittest.skip("TODO")
    def test_new_message_version_from_tdlib_message(self):

        pass

    @unittest.skip("TODO")
    def test_new_message_from_tdlib_message_with_text_entities(self):
        pass