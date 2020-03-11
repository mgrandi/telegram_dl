from __future__ import annotations

import functools
import logging
import typing

import attr

from telegram_dl import tdlib
from telegram_dl import constants
from telegram_dl import tdlib_generated as tdg
from telegram_dl import utils
from telegram_dl import db_model
from telegram_dl import db_actions

logger = logging.getLogger(__name__)

authstate_logger = logger.getChild("authstate")
not_implemented_logger = logger.getChild("not_implemented")


@attr.s
class HandlerParameters:
    ''' something we pass in to every handler method
    '''

    tdlib_handle:tdlib.TdlibHandle = attr.ib()
    to_telegram_queue:asyncio.Queue = attr.ib()
    database_queue:asyncio.Queue = attr.ib()


class TdlibBaseMessageHandler:

    def __init__(self, auth_handler):

        self.auth_handler = auth_handler

    @functools.singledispatchmethod
    async def handle_message(self, message:tdg.RootObject, params:HandlerParameters) -> typing.Optional[tdlib.TdlibResult]:

        #not_implemented_logger.error("Unimplemented type: TdlibBaseMessageHandler.handle_message got `%s`", message)
        return tdlib.TdlibResult(
            code=constants.TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED,
            message=f"Unimplemented message of type `{type(message)}`: `{message}`",
            result_obj=None)

    @handle_message.register
    async def handle_message_ok(self, message:tdg.ok, params:HandlerParameters) -> tdlib.TdlibResult:

        logger.debug("handle_message_ok got `%s`", message)


    @handle_message.register
    async def handle_message_update_auth_state(self, message:tdg.updateAuthorizationState, params:HandlerParameters) -> tdlib.TdlibResult:

        logger.debug("handle_message_update_authorization_state.handle_message got `%s`", message)

        auth_state = message.authorization_state

        await self.auth_handler.handle_auth_state(auth_state, params)

        return tdlib.TdlibResult(
                code=constants.TDLIB_RESULT_CODE_OK,
                message=f"OK",
                result_obj=None)


    @handle_message.register
    async def handle_message_update_option(self, message:tdg.updateOption, params:HandlerParameters) -> tdlib.TdlibResult:

        logger.debug("handle_message_update_option.handle_message got `%s`", message)

    @handle_message.register
    async def handle_message_update_user(self,  message:tdg.updateUser, params:HandlerParameters) -> tdlib.TdlibResult:

        logger.debug("handle_message_update_user.handle_message got `%s`", message)

        params.database_queue.put_nowait(db_actions.InsertDatabaseAction(object_to_insert=message.user))


class AuthorizationHandler:

    def __init__(self, input):

        self.input = input

    @functools.singledispatchmethod
    async def handle_auth_state(self, auth_state:tdg.AuthorizationState, params:HandlerParameters) -> None:
        '''
        GENERIC implementation of AuthorizationState
        '''

        authstate_logger.error("Unimplemented AuthorizationState! we got: `%s`", auth_state)

    @handle_auth_state.register
    async def handle_auth_state_wait_tdlib_params(self, message:tdg.authorizationStateWaitTdlibParameters,
        params:HandlerParameters) -> None:
        '''
        authorizationStateWaitTdlibParameters
        '''


        authstate_logger.debug("handle_auth_state_wait_tdlib_params got message: `%s`", message)

        set_param = tdg.setTdlibParameters(parameters=params.tdlib_handle.tdlib_parameters_config, extra=utils.new_extra())

        authstate_logger.debug("putting into queue: setTdlibParameters: `%s`", set_param)
        params.to_telegram_queue.put_nowait(set_param)


    @handle_auth_state.register
    async def handle_auth_state_wait_encryption_key(self, message:tdg.authorizationStateWaitEncryptionKey,
        params:HandlerParameters) -> None:
        '''
        authorizationStateWaitEncryptionKey
        '''

        authstate_logger.debug("handle_auth_state_wait_encryption_key got message: `%s`", message)

        check_key = tdg.checkDatabaseEncryptionKey(encryption_key="", extra=utils.new_extra())
        authstate_logger.debug("putting into queue: checkDatabaseEncryptionKey: `%s`", check_key)

        params.to_telegram_queue.put_nowait(check_key)



    @handle_auth_state.register
    async def handle_auth_state_wait_phone_number(self, message:tdg.authorizationStateWaitPhoneNumber,
        params:HandlerParameters) -> None:
        '''
        authorizationStateWaitPhoneNumber
        '''

        authstate_logger.debug("handle_auth_state_wait_phone_number got message: `%s`", message)

        ask_phone_no_result = self.input.ask_user_for_phone_number()
        set_auth_phone_no = tdg.setAuthenticationPhoneNumber(phone_number=ask_phone_no_result.get_as_one_string(),
            settings=None, extra=utils.new_extra())
        authstate_logger.debug("putting into queue: setAuthenticationPhoneNumber: `%s`", set_auth_phone_no)

        params.to_telegram_queue.put_nowait(set_auth_phone_no)



    @handle_auth_state.register
    async def handle_auth_state_wait_code(self, message:tdg.authorizationStateWaitCode,
        params:HandlerParameters) -> None:
        '''
        authorizationStateWaitCode
        '''

        authstate_logger.debug("handle_auth_state_wait_code got message: `%s`", message)

        ask_for_code_result = self.input.ask_user_for_code()
        check_auth_code = tdg.checkAuthenticationCode(code=ask_for_code_result.code, extra=utils.new_extra())
        authstate_logger.debug("putting into queue: checkAuthenticationCode: `%s`", check_auth_code)

        params.to_telegram_queue.put_nowait(check_auth_code)


    @handle_auth_state.register
    async def handle_auth_state_wait_registration(self, message:tdg.authorizationStateWaitRegistration,
        params:HandlerParameters) -> None:
        '''
        authorizationStateWaitRegistration
        '''

        authstate_logger.debug("handle_auth_state_wait_registration got message: `%s`", message)

        name_result = self.input.ask_user_for_first_last_name()
        reg_user_ = tdg.registerUser(first_name=name_result.first, last_name=name_result.last, extra=utils.new_extra())
        authstate_logger.debug("putting into queue: registerUser: `%s`", reg_user)

        params.to_telegram_queue.put_nowait(reg_user)


    @handle_auth_state.register
    async def handle_auth_state_wait_password(self, message:tdg.authorizationStateWaitPassword,
        params:HandlerParameters) -> None:
        '''
        authorizationStateWaitPassword
        '''

        authstate_logger.debug("handle_auth_state_wait_password got message: `%s`", message)
        password_result = self.input.ask_user_for_password()

        check_password = tdg.checkAuthenticationPassword(password=password_result.password, extra=utils.new_extra())
        authstate_logger.debug("putting into queue: checkAuthenticationPassword: `%s`", check_password)

        params.to_telegram_queue.put_nowait(check_password)



    @handle_auth_state.register
    async def handle_auth_state_ready(self, message:tdg.authorizationStateReady,
        params:HandlerParameters) -> None:
        '''
        authorizationStateReady
        '''

        authstate_logger.info("Authorization State is now `%s`", "Ready")


    @handle_auth_state.register
    async def handle_auth_state_closing(self, message:tdg.authorizationStateClosing,
        params:HandlerParameters) -> None:
        '''
        authorizationStateClosing
        '''

        authstate_logger.info("Authorization State is now `%s`", "Closing")


    @handle_auth_state.register
    async def handle_auth_state_logging_out(self, message:tdg.authorizationStateLoggingOut,
        params:HandlerParameters) -> None:
        '''
        authorizationStateLoggingOut
        '''
        authstate_logger.info("Authorization State is now `%s`", "Logging Out")


    @handle_auth_state.register
    async def handle_auth_state_closed(self, message:tdg.authorizationStateClosed,
        params:HandlerParameters) -> None:
        '''
        authorizationStateClosed
        '''
        authstate_logger.info("Authorization State is now `%s`", "Closed")
