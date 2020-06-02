from __future__ import annotations

import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
import telegram_dl.db_model_enums as dbme
from telegram_dl import constants

import phonenumbers
from phonenumbers.phonenumber import PhoneNumber

logger = logging.getLogger(__name__)

class PhoneNumberAide:

    @staticmethod
    def parse_phone_number_from_string(phone_number_str:str) -> PhoneNumber:
        '''
        parses a phone number string and returns a PhoneNumber object
        '''

        return phonenumbers.parse(phone_number_str, region=constants.PHONE_NUMBER_DEFAULT_REGION)

    @staticmethod
    def fix_phone_number_from_string(phone_number_str:str) -> str:
        ''' add a plus infront of the phone number if it
        doesn't have one so `phonenumbers` can parse it
        '''

        # NOTE: it seems that we are NOT supposed to put a plus infront of the number
        # if it is a short code number
        # see:
        # https://support.twilio.com/hc/en-us/articles/223182068-What-is-a-Messaging-Short-Code-
        # https://support.twilio.com/hc/en-us/articles/360013980754-Formatting-Short-Code-Numbers
        if not phone_number_str.startswith("+"):

            if len(phone_number_str) >= constants.PHONE_NUMBER_SHORT_CODE_MIN_LENGTH \
                and len(phone_number_str) <= constants.PHONE_NUMBER_SHORT_CODE_MIN_LENGTH:

                return phone_number_str
            else:
                return f"+{phone_number_str}"
        else:
            return phone_number_str


    @staticmethod
    def compare_phonenumberslite_to_tdlib_phonenumber(
        phonenumbers_lib_obj:PhoneNumber,
        tdlib_phone_number_str:str) -> bool:
        '''
        Compare a `phonenumbers.PhoneNumber` object to a string representation
        of a phone numberthat we get back from telegram
        '''

        phone_number_compare_result = None

        logger.debug("comparing `%s` and `%s`", phonenumbers_lib_obj, tdlib_phone_number_str)

        if not phonenumbers_lib_obj:

            if not tdlib_phone_number_str:
                # both phone numbers are empty, just mark as unchanged right
                phone_number_compare_result = True
            else:
                # old phone number doesn't exist but the new one does exist, mark as different
                phone_number_compare_result = False
        else:
            if not tdlib_phone_number_str:
                # old phone exists but new one doesn't, mark as different
                phone_number_compare_result = False
            else:
                # both old and new phone numbers exist, compare
                fixed_phone_number_str = PhoneNumberAide.fix_phone_number_from_string(tdlib_phone_number_str)

                tdlib_parsed_phone = PhoneNumberAide.parse_phone_number_from_string(fixed_phone_number_str)

                phone_number_compare_result = phonenumbers_lib_obj == tdlib_parsed_phone

        logger.debug("final result: `%s`", phone_number_compare_result)

        return phone_number_compare_result