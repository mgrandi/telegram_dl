import unittest

import phonenumbers

from telegram_dl.aides.phone_number_aide import PhoneNumberAide

class TestPhoneNumberAide(unittest.TestCase):

    def test_fix_phone_number_from_string_plus_sign_us_number(self):
        '''
        PhoneNumberAide.fix_phone_number_from_string - standard 1+3+7 digit number, has plus sign
        '''

        plus_str = "+"
        country_code = "1"
        area_code = "415"
        regional_number = "5551234"

        test_number_str = f"{plus_str}{country_code}{area_code}{regional_number}"

        fixed_number = PhoneNumberAide.fix_phone_number_from_string(test_number_str)

        expected_number = "+14155551234"
        self.assertEqual(expected_number, fixed_number)
