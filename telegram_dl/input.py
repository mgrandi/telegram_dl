import logging

import attr
import getpass

from telegram_dl import constants

logger = logging.getLogger(__name__)

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class PhoneNumberResult:
    country_code:str = attr.ib()
    area_code:str = attr.ib()
    phone_number:str = attr.ib()

    def get_as_one_string(self):

        return f"+{self.country_code}{self.area_code}{self.phone_number}"

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class TwoFactorAuthCodeResult:
    code:str = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class FirstLastNameResult:
    first:str = attr.ib()
    last:str = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class CloudPasswordResult:
    password:str = attr.ib(repr=False)

class BaseInput:

    def ask_user_for_phone_number(self) -> PhoneNumberResult:

        raise NotImplementedError("you need to subclass BaseInput")

    def ask_user_for_code(self) -> TwoFactorAuthCodeResult:

        raise NotImplementedError("you need to subclass BaseInput")

    def ask_user_for_first_last_name(self) -> FirstLastNameResult:

        raise NotImplementedError("you need to subclass BaseInput")

    def ask_user_for_password(self) -> CloudPasswordResult:
        raise NotImplementedError("you need to subclass BaseInput")



class TTYInput(BaseInput):

    def _input(self, prompt, description):

        logger.debug("asking for: `%s`", description)

        result = input(prompt)

        logger.debug("asking user for `%s` complete, result: `%s`", description, result)
        return result

    def _secureinput(self, prompt, description):
        logger.debug("asking for: `%s`", description)

        result = getpass.getpass(prompt)

        logger.debug("asking user for `%s` complete, result: `%s`", description, result)
        return result

    def ask_user_for_phone_number(self) -> PhoneNumberResult:

        while True:
            phone_num_result = self._input(constants.INPUT_ASK_FOR_PHONE_NUMBER, "phone number")

            match_result = constants.INPUT_PHONE_NUMBER_REGEX.match(phone_num_result)
            logger.debug("phone # regex match result: `%s`", match_result)

            if match_result:

                g = match_result.groupdict()
                final = PhoneNumberResult(country_code=g[constants.PHONE_NO_REGEX_CC],
                    area_code=g[constants.PHONE_NO_REGEX_AC],
                    phone_number=f"{g[constants.PHONE_NO_REGEX_PN1]}{g[constants.PHONE_NO_REGEX_PN2]}")

                logger.debug("final phone number result: `%s`", final)
                return final


    def ask_user_for_code(self) -> TwoFactorAuthCodeResult:

        result = self._input(constants.INPUT_ASK_FOR_CODE, "2FA Code")


        final =  TwoFactorAuthCodeResult(code=result)

        logger.debug("final 2fa result: `%s`", final)
        return final

    def ask_user_for_first_last_name(self) -> FirstLastNameResult:

        result_first = self._input(constants.INPUT_ASK_FOR_FIRST_NAME, "first name")
        result_last = self.input(constants.INPUT_ASK_FOR_LAST_NAME, "last name")

        final  = FirstLastNameResult(first=result_first, last=result_last)

        logger.debug("final first/last name result: `%s`", final)

        return final

    def ask_user_for_password(self) -> CloudPasswordResult:
        result = self._secureinput(constants.INPUT_ASK_FOR_PASSWORD, "cloud password")

        final = CloudPasswordResult(password=result)

        logger.debug("final password result: `%s`", final)
        return final