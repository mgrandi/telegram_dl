# Unit Testing Notes

## Configuration

the configuration file is in the root of the codebase, `node2.cfg`

see https://docs.nose2.io/en/latest/configuration.html for information on the configuration file
and what can go in it

## Running the unit tests

`cd` to the root directory of the codebase, and then just run `nose2`

```plaintext
PS C:\Users\mark\Code\personal\telegram_dl> nose2
......
----------------------------------------------------------------------
Ran 6 tests in 0.051s

OK
```

you can also run it with `-v` for more verbose output

```plaintext
PS C:\Users\mark\Code\personal\telegram_dl> nose2 -v

test_cattr_converter_round_trip (telegram_dl.test.test_cattr_converter.TestCattrConverter)
`utils.CustomCattrConverter` round trip test ... ok
test_compare_chat_supergroup_channel_nophoto_equal (telegram_dl.test.test_chat_aide.TestChatAide)
`ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, no photo, should be equal ... ok
test_compare_chat_supergroup_channel_photo_equal (telegram_dl.test.test_chat_aide.TestChatAide)
`ChatAide.test_compare_tdlib_and_dbmodel_chat` with a supergroup, photo, should be equal ... ok
test_load_supergroup_channel_from_file_no_photo (telegram_dl.test.test_chat_aide.TestChatAide)
loading a `db_model.SuperGroupChat`, no photo ... ok
test_load_supergroup_channel_from_file_photo (telegram_dl.test.test_chat_aide.TestChatAide)
loading a `db_model.SuperGroupChat`, has photo ... ok
test_multiple_chat_versions (telegram_dl.test.test_chat_aide.TestChatAide)
chat with multiple versions, checking against the most recent version ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.038s

OK
```

## warnings

it seems that nose2 doesn't log warnings very easily that I can tell, unlike
`python -m unittest`.

example:

```plaintext


PS C:\Users\auror\Code\Personal\telegram_dl> nose2

sss.sssssssssssssssss..ss.sssss..s.sssss.ssssssss.....................s...
----------------------------------------------------------------------
Ran 74 tests in 0.380s

OK (skipped=42)


PS C:\Users\auror\Code\Personal\telegram_dl> python -m unittest
sss.sssssssssssssssss..ss.sssss..s.sssss.ssssssss.....................s..C:\Users\auror\Code\Personal\telegram_dl\telegram_dl\test\test_cattr_converter.py:103: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(round_trip_obj.dict_data["two"], "there")
.
----------------------------------------------------------------------
Ran 74 tests in 0.331s

OK (skipped=42)

PS C:\Users\auror\Code\Personal\telegram_dl>
```

## subtests

it seems that nose2 doesn't list out the subtests like `unittest` does, see
this bug report: https://github.com/nose-devs/nose2/issues/334