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

        note: for short code numbers, add a `+1` to the start of the number OR
        don't add a plus at all (and no `1` as well) , because or else the country
        code will get confused otherwise

        see `notes/phone number notes.md` for more info
        '''

        fixed_phone_number_str = PhoneNumberAide.fix_phone_number_from_string(phone_number_str)

        return phonenumbers.parse(fixed_phone_number_str,
            region=constants.PHONE_NUMBER_DEFAULT_REGION)

    @staticmethod
    def fix_phone_number_from_string(phone_number_str:str) -> str:
        ''' add a plus infront of the phone number if it
        doesn't have one so `phonenumbers` can parse it easier
        '''

        if not phone_number_str.startswith("+"):

            l = len(phone_number_str)


            if l >= constants.PHONE_NUMBER_SHORT_CODE_MIN_LENGTH \
                and l <= constants.PHONE_NUMBER_SHORT_CODE_MAX_LENGTH:

                # short codes are a US thing, don't add a plus, it will be
                # added automatically when parsed

                return f"{phone_number_str}"
            else:
                # not a short code number, add a plus
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

        if phonenumbers_lib_obj is not None and not isinstance(phonenumbers_lib_obj, phonenumbers.PhoneNumber):
            raise Exception(f"`phonenumbers_lib_obj` was not a PhoneNumber, it was {type(phonenumbers_lib_obj)}")

        if tdlib_phone_number_str is not None and not isinstance(tdlib_phone_number_str, str):
            raise Exception(f"`tdlib_phone_number_str` was not a str, it was {type(tdlib_phone_number_str)}")

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
                tdlib_parsed_phone = PhoneNumberAide.parse_phone_number_from_string(tdlib_phone_number_str)

                phone_number_compare_result = phonenumbers_lib_obj == tdlib_parsed_phone

        logger.debug("final result: `%s`", phone_number_compare_result)

        return phone_number_compare_result