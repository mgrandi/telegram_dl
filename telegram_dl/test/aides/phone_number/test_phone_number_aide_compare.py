import unittest

import phonenumbers

from telegram_dl.aides.phone_number_aide import PhoneNumberAide

class TestPhoneNumberAideCompare(unittest.TestCase):
    '''
    tests relating to `PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber`

    note: i don't really want to implement just unit tests for what should already be
    unit tested by the `phonenumbers` library, so this will just test the behavior in
    the method
    '''


    def test_compare_both_empty(self):
        '''
        both tdlib (str) and PhoneNumber objects are empty
        '''

        # `tdlib` phone number (as a string)
        tdlib_combined_number_str = ""

        # `phonenumbers` object
        pn_obj_parsed_number = None

        # assertion
        self.assertTrue(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))


    def test_compare_tdlib_empty(self):
        '''
        tdlib phone number (str) is empty, PhoneNumber object is not empty
        '''

        # `tdlib` phone number (as a string)
        tdlib_combined_number_str = ""


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "1"
        pn_obj_area_code = "415"
        pn_obj_regional_number = "5551234"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertFalse(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))


    def test_compare_phonenumber_obj_empty(self):
        '''
        tdlib phone number (str) is not empty, PhoneNumber object is empty
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "1"
        tdlib_area_code = "415"
        tdlib_regional_number = "5551234"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_parsed_number = None

        # assertion
        self.assertFalse(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))



    def test_compare_both_present_us_standard_equal(self):
        '''
        both parameters are present, US, standard number, equal
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "1"
        tdlib_area_code = "415"
        tdlib_regional_number = "5551234"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "1"
        pn_obj_area_code = "415"
        pn_obj_regional_number = "5551234"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertTrue(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))

    def test_compare_both_present_us_standard_non_equal(self):
        '''
        both parameters are present, US, standard number, not equal
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "1"
        tdlib_area_code = "415"
        tdlib_regional_number = "5553333"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "1"
        pn_obj_area_code = "415"
        pn_obj_regional_number = "5551234"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertFalse(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))


    def test_compare_both_present_us_short_code_equal(self):
        '''
        both parameters are present, US, short code number, equal
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "1"
        tdlib_area_code = ""
        tdlib_regional_number = "42777"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "1"
        pn_obj_area_code = ""
        pn_obj_regional_number = "42777"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertTrue(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))

    def test_compare_both_present_us_standard_non_equal(self):
        '''
        both parameters are present, US, short code number, not equal
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "1"
        tdlib_area_code = ""
        tdlib_regional_number = "42777"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "1"
        pn_obj_area_code = ""
        pn_obj_regional_number = "44123"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertFalse(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))


    def test_compare_both_present_non_us_standard_equal(self):
        '''
        both parameters are present, non US, standard number, equal
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "44"
        tdlib_area_code = "20"
        tdlib_regional_number = "71838750"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "44"
        pn_obj_area_code = "20"
        pn_obj_regional_number = "71838750"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertTrue(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))

    def test_compare_both_present_non_us_standard_not_equal(self):
        '''
        both parameters are present, non US, standard number, not equal
        '''

        # `tdlib` phone number (as a string)
        tdlib_maybe_plus_str = "+"
        tdlib_country_code = "44"
        tdlib_area_code = "20"
        tdlib_regional_number = "71838750"

        tdlib_combined_number_str = f"{tdlib_maybe_plus_str}{tdlib_country_code}{tdlib_area_code}{tdlib_regional_number}"


        # `phonenumbers` object
        pn_obj_maybe_plus_str = "+"
        pn_obj_country_code = "44"
        pn_obj_area_code = "21"
        pn_obj_regional_number = "71838751"
        pn_obj_combined_number_str = f"{pn_obj_maybe_plus_str}{pn_obj_country_code}{pn_obj_area_code}{pn_obj_regional_number}"

        pn_obj_parsed_number = phonenumbers.parse(pn_obj_combined_number_str)

        # assertion
        self.assertFalse(PhoneNumberAide.compare_phonenumberslite_to_tdlib_phonenumber(
            pn_obj_parsed_number, tdlib_combined_number_str))