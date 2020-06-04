import unittest

import phonenumbers

from telegram_dl.aides.phone_number_aide import PhoneNumberAide

class TestPhoneNumberAideFix(unittest.TestCase):
    '''
    tests relating to `PhoneNumberAide.fix_phone_number_from_string`
    '''

    def test_fix_phone_number_from_string_plus_sign_us_number(self):
        '''
        PhoneNumberAide.fix_phone_number_from_string - standard 1+3+7 digit US number, has plus sign
        '''

        maybe_plus_str = "+"
        country_code = "1"
        area_code = "415"
        regional_number = "5551234"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "+14155551234")

        fixed_number = PhoneNumberAide.fix_phone_number_from_string(test_number_str)

        expected_number = "+14155551234"
        self.assertEqual(expected_number, fixed_number)


    def test_fix_phone_number_from_string_no_plus_sign_us_number(self):
        '''
        PhoneNumberAide.fix_phone_number_from_string - standard 1+3+7 digit US number, no plus sign
        '''

        maybe_plus_str = ""
        country_code = "1"
        area_code = "415"
        regional_number = "5551234"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "14155551234")

        fixed_number = PhoneNumberAide.fix_phone_number_from_string(test_number_str)

        expected_number = "+14155551234"
        self.assertEqual(expected_number, fixed_number)


    def test_fix_phone_number_from_string_plus_sign_non_us_number(self):
        '''
        PhoneNumberAide.fix_phone_number_from_string - non-US number, has plus sign

        number taken from https://support.twilio.com/hc/en-us/articles/223183008-Formatting-International-Phone-Numbers
        '''
        maybe_plus_str = "+"
        country_code = "44"
        area_code = "20"
        regional_number = "71838750"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "+442071838750")

        fixed_number = PhoneNumberAide.fix_phone_number_from_string(test_number_str)

        expected_number = "+442071838750"
        self.assertEqual(expected_number, fixed_number)


    def test_fix_phone_number_from_string_no_plus_sign_non_us_number(self):
        '''
        PhoneNumberAide.fix_phone_number_from_string - non-US number, has plus sign

        number taken from https://support.twilio.com/hc/en-us/articles/223183008-Formatting-International-Phone-Numbers

        '''

        maybe_plus_str = ""
        country_code = "44"
        area_code = "20"
        regional_number = "71838750"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "442071838750")

        fixed_number = PhoneNumberAide.fix_phone_number_from_string(test_number_str)

        expected_number = "+442071838750"
        self.assertEqual(expected_number, fixed_number)



    def test_fix_phone_number_from_string_no_plus_shortcode(self):
        '''
        PhoneNumberAide.fix_phone_number_from_string - shortcode US number, no plus sign
        '''

        maybe_plus_str = ""
        country_code = ""
        area_code = ""
        regional_number = "42777"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "42777")

        fixed_number = PhoneNumberAide.fix_phone_number_from_string(test_number_str)

        expected_number = "42777"
        self.assertEqual(expected_number, fixed_number)


