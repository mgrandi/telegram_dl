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
