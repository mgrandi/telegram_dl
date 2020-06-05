import unittest

import phonenumbers

from telegram_dl.aides.phone_number_aide import PhoneNumberAide

class TestPhoneNumberAideParse(unittest.TestCase):
    '''
    tests relating to `PhoneNumberAide.parse_phone_number_from_string`
    '''

    def test_parse_phone_number_from_string_us_no_plus_standard(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - US number, no plus, standard number
        '''

        maybe_plus_str = ""
        country_code = "1"
        area_code = "415"
        regional_number = "5551234"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "14155551234")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 1)
        self.assertEqual(parsed_number.national_number, 4155551234)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+14155551234")


    def test_parse_phone_number_from_string_us_plus_standard(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - US number, has plus, standard number
        '''

        maybe_plus_str = "+"
        country_code = "1"
        area_code = "415"
        regional_number = "5551234"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "+14155551234")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 1)
        self.assertEqual(parsed_number.national_number, 4155551234)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+14155551234")


    def test_parse_phone_number_from_string_non_us_no_plus_standard(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - Non US number, no plus, standard number
        '''

        maybe_plus_str = ""
        country_code = "44"
        area_code = "20"
        regional_number = "71838750"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "442071838750")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 44)
        self.assertEqual(parsed_number.national_number, 2071838750)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+442071838750")


    def test_parse_phone_number_from_string_non_us_plus_standard(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - Non US number, has plus, standard number
        '''

        maybe_plus_str = "+"
        country_code = "44"
        area_code = "20"
        regional_number = "71838750"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "+442071838750")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 44)
        self.assertEqual(parsed_number.national_number, 2071838750)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+442071838750")


    def test_parse_phone_number_from_string_us_no_plus_shortcode_five_digits(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - US number, no plus, short code number, 5 digits
        '''

        maybe_plus_str = ""
        country_code = ""
        area_code = ""
        regional_number = "42777"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "42777")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 1)
        self.assertEqual(parsed_number.national_number, 42777)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+142777")


    def test_parse_phone_number_from_string_us_no_plus_shortcode_six_digits(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - US number, no plus, short code number, 6 digits
        '''

        maybe_plus_str = ""
        country_code = ""
        area_code = ""
        regional_number = "427778"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "427778")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 1)
        self.assertEqual(parsed_number.national_number, 427778)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+1427778")

    def test_parse_phone_number_from_string_us_plus_shortcode_five_digits(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - US number, has plus, short code number, 5 digits
        '''

        maybe_plus_str = "+"
        country_code = "1"
        area_code = ""
        regional_number = "42777"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "+142777")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 1)
        self.assertEqual(parsed_number.national_number, 42777)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+142777")


    def test_parse_phone_number_from_string_us_plus_shortcode_six_digits(self):
        '''
        PhoneNumberAide.parse_phone_number_from_string - US number, no plus, short code number, 6 digits
        '''

        maybe_plus_str = "+"
        country_code = "1"
        area_code = ""
        regional_number = "427778"

        test_number_str = f"{maybe_plus_str}{country_code}{area_code}{regional_number}"

        self.assertEqual(test_number_str, "+1427778")

        parsed_number = PhoneNumberAide.parse_phone_number_from_string(test_number_str)

        self.assertEqual(parsed_number.country_code, 1)
        self.assertEqual(parsed_number.national_number, 427778)

        parsed_number_formatted = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        self.assertEqual(parsed_number_formatted, "+1427778")

