# tdlib logging notes

## class references

### methods

`setLogStream`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_log_stream.html

Sets new log stream for internal logging of TDLib. This is an offline method. Can be called before authorization. Can be called synchronously.

`setLogVerbosityLevel`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1set_log_verbosity_level.html

Sets the verbosity level of the internal logging of TDLib. This is an offline method. Can be called before authorization. Can be called synchronously.

parameter `new_verbosity_level`:

New value of the verbosity level for logging. Value 0 corresponds to fatal errors, value 1 corresponds to errors, value 2 corresponds to warnings and debug warnings, value 3 corresponds to informational, value 4 corresponds to debug, value 5 corresponds to verbose debug, value greater than 5 and up to 1023 can be used to enable even more logging.


### LogStream objects

a `LogStream` describes where the tdlib internal log is written

`LogStream` (base class): https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_log_stream.html

`logStreamDefault`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1log_stream_default.html
`logStreamEmpty`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1log_stream_empty.html
`logStreamFile`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1log_stream_file.html

