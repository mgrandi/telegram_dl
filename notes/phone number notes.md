# phone number notes

## urls

https://github.com/google/libphonenumber
https://github.com/daviddrysdale/python-phonenumbers

https://support.twilio.com/hc/en-us/articles/223182068-What-is-a-Messaging-Short-Code-
https://support.twilio.com/hc/en-us/articles/360013980754-Formatting-Short-Code-Numbers

https://support.twilio.com/hc/en-us/articles/223183008-Formatting-International-Phone-Numbers

## basics

we are using the `phonenumbers` library (https://github.com/google/libphonenumber) to parse phone numbers

basic parts of a phone number:

* country code
* area code
* regional number

(area code + regional number add together to be a 'national number')

so given a phone number `+14155551234`, the country code is `1`, the area code is `415`, and the regional number is `5551234`.

## parsing a phone number

use the `phonenumbers.parse` function, with the string phone number and the country code as the second argument. You can specify different countries for the formatting but I always just specify US and pass in E164 format numbers

```python3
>>> import phonenumbers
>>> x = phonenumbers.parse("+14155551234", "US")
>>> x
PhoneNumber(country_code=1, national_number=4155551234, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)
```

it can be in a variety of formats too (aka not E164)

```python3
>>> x = phonenumbers.parse("+1 (415) 555-1234", "US")
>>> x
PhoneNumber(country_code=1, national_number=4155551234, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)
```

## formatting a phone number

use the `phonenumbers.format_number` function, using one of the `phonenumbers.PhoneNumberFormat` constants

```python3
>>> import phonenumbers
>>> x = phonenumbers.parse("+14155551234", "US")
>>> x
PhoneNumber(country_code=1, national_number=4155551234, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)

>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
'(415) 555-1234'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
'+1 415-555-1234'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
'+14155551234'
```

## International Numbers

see https://support.twilio.com/hc/en-us/articles/223183008-Formatting-International-Phone-Numbers

same thing applies for parsing and formatting

```python3
>>> import phonenumbers

>>> x = phonenumbers.parse("+44 020 7183 8750", "US")
>>> x
PhoneNumber(country_code=44, national_number=2071838750, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)


>>> x = phonenumbers.parse("+4402071838750", "US")


>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
'020 7183 8750'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
'+44 20 7183 8750'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
'+442071838750'

```

## Short Code numbers

apparently this is a US thing, but the `phonenumbers` library handles it fine

```python3
>>> import phonenumbers


>>> x = phonenumbers.parse("42777", "US")
>>> x
PhoneNumber(country_code=1, national_number=42777, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)


>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL)
'42777'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
'+1 42777'
>>> phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164)
'+142777'

```

HOWEVER, if you are adding a `+` sign to a short code number, you need to add the US country code of `1` to it as
well or else it will not parse.
```python3
>>> x = phonenumbers.parse("+42777", "US")

Traceback (most recent call last):
  File "C:\Users\auror\AppData\Local\pypoetry\Cache\virtualenvs\telegram-dl-a1fmb41G-py3.8\lib\site-packages\phonenumbers\phonenumberutil.py", line 2822, in parse
    country_code, normalized_national_number = _maybe_extract_country_code(national_number,
  File "C:\Users\auror\AppData\Local\pypoetry\Cache\virtualenvs\telegram-dl-a1fmb41G-py3.8\lib\site-packages\phonenumbers\phonenumberutil.py", line 2514, in _maybe_extract_country_code
    raise NumberParseException(NumberParseException.INVALID_COUNTRY_CODE,
phonenumbers.phonenumberutil.NumberParseException: (0) Country calling code supplied was not recognised.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\auror\AppData\Local\pypoetry\Cache\virtualenvs\telegram-dl-a1fmb41G-py3.8\lib\site-packages\phonenumbers\phonenumberutil.py", line 2837, in parse
    raise NumberParseException(NumberParseException.INVALID_COUNTRY_CODE,
phonenumbers.phonenumberutil.NumberParseException: (0) Could not interpret numbers after plus-sign.



>>> x = phonenumbers.parse("+142777", "US")
>>> x
PhoneNumber(country_code=1, national_number=42777, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)

```


If you have a short code number whose first digits happen to be a valid country code, then it will parse, but the country code will be incorrect! To be correct 100% of the time, either do not add a `+` infront of the number at all, or add a `+1` infront of the number!

```python3

>>> x = phonenumbers.parse("44227", "US")
>>> x
PhoneNumber(country_code=1, national_number=44227, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)

>>> y = phonenumbers.parse("+44227", "US")
>>> y
PhoneNumber(country_code=44, national_number=227, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)

>>> z = phonenumbers.parse("+144227", "US")
>>> z
PhoneNumber(country_code=1, national_number=44227, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=0, preferred_domestic_carrier_code=None)
```

