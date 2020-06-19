import unittest
import typing
import base64

import attr

from telegram_dl import tdlib_generated as tdg
from telegram_dl import utils


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TestClass:
    binary_data:bytes = attr.ib()
    integer_data:int = attr.ib()
    float_data:float = attr.ib()
    boolean_data:bool = attr.ib()
    str_data:str = attr.ib()
    list_data:typing.Sequence[str] = attr.ib()
    dict_data:typing.Mapping[str,str] = attr.ib()


class TestCattrConverter(unittest.TestCase):


    def test_cattr_converter_round_trip(self):
        '''
        `utils.CustomCattrConverter` round trip test
        '''

        binary_data = "this_is_binary_data 1234567890 🐧".encode("utf-8")
        integer_data = 1234
        float_data = float(1.2)
        boolean_data = True
        null_data = None
        str_data = "hello there"
        list_data = ["hello", "there"]
        dict_data = {"one": "hello", "two": "there"}


        test_instance = TestClass(
            binary_data=binary_data,
            integer_data=integer_data,
            float_data=float_data,
            boolean_data=boolean_data,
            str_data=str_data,
            list_data=list_data,
            dict_data=dict_data)


        converter = utils.CustomCattrConverter(tdg.tdlib_gen_globals, tdg.tdlib_gen_locals)
        utils.register_custom_types_with_cattr_converter(converter)

        ##########################################################
        # serialize the object as a dictionary
        ##########################################################

        obj_as_dict = converter.unstructure(test_instance)

        ##########################################################
        # make sure the dictionary is what we expect
        ##########################################################

        self.assertEqual(obj_as_dict["binary_data"], base64.b64encode(binary_data).decode("utf-8"))
        self.assertEqual(obj_as_dict["integer_data"], integer_data)
        self.assertEqual(obj_as_dict["float_data"], float_data)
        self.assertEqual(obj_as_dict["boolean_data"], boolean_data)
        self.assertEqual(obj_as_dict["str_data"], str_data)

        self.assertEqual(obj_as_dict["list_data"], list_data)
        self.assertEqual(obj_as_dict["list_data"][0], "hello")
        self.assertEqual(obj_as_dict["list_data"][1], "there")

        self.assertEqual(obj_as_dict["dict_data"], dict_data)
        self.assertEqual(obj_as_dict["dict_data"]["one"], "hello")
        self.assertEqual(obj_as_dict["dict_data"]["two"], "there")

        ##########################################################
        # assert the number of keys in the dictionary
        ##########################################################

        self.assertEqual(len(obj_as_dict.keys()), 7)

        ##########################################################
        # now convert back to an object and assert its the same as the one we created
        ##########################################################

        round_trip_obj = converter.structure(obj_as_dict, TestClass)

        self.assertEqual(round_trip_obj, test_instance)

        self.assertEqual(round_trip_obj.binary_data, binary_data)
        self.assertEqual(round_trip_obj.integer_data, integer_data)
        self.assertEqual(round_trip_obj.float_data, float_data)
        self.assertEqual(round_trip_obj.boolean_data, boolean_data)
        self.assertEqual(round_trip_obj.str_data, str_data)

        self.assertEqual(round_trip_obj.list_data, list_data)
        self.assertEqual(round_trip_obj.list_data[0], "hello")
        self.assertEqual(round_trip_obj.list_data[1], "there")

        self.assertEqual(round_trip_obj.dict_data, dict_data)
        self.assertEqual(round_trip_obj.dict_data["one"], "hello")
        self.assertEqual(round_trip_obj.dict_data["two"], "there")






