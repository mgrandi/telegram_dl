import functools
import logging
import typing

import attr

from telegram_dl import tdlib
from telegram_dl import constants
from telegram_dl import tdlib_generated as tdg
from telegram_dl import utils

logger = logging.getLogger(__name__)

authstate_logger = logger.getChild("authstate")


class TdlibBaseMessageHandler:

    @functools.singledispatchmethod
    async def handle_message(self, message:tdg.RootObject, tdlib_handle:tdlib.TdlibHandle) -> typing.Optional[tdlib.TdlibResult]:

        logger.error("TdlibBaseMessageHandler.handle_message got `%s`", message)
        return tdlib.TdlibResult(
            code=constants.TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED,
            message=f"Unimplemented message of type `{type(message)}`: `{message}`",
            result_obj=None)


    @handle_message.register
    async def handle_message_ok(self, message:tdg.ok, tdlib_handle:tdlib.TdlibHandle) -> tdlib.TdlibResult:

        logger.debug("handle_message_ok got `%s`", message)


    @handle_message.register
    async def handle_message_update_auth_state(self, message:tdg.updateAuthorizationState, tdlib_handle:tdlib.TdlibHandle) -> tdlib.TdlibResult:

        logger.debug("handle_message_update_authorization_state.handle_message got `%s`", message)

        auth_state = message.authorization_state

        await self.handle_auth_state(auth_state, tdlib_handle)

        return tdlib.TdlibResult(
                code=constants.TDLIB_RESULT_CODE_OK,
                message=f"OK",
                result_obj=None)



    '''
    updateAuthorizationState
        authorizationStateClosed

        authorizationStateWaitTdlibParameters
        authorizationStateWaitEncryptionKey

        authorizationStateWaitPhoneNumber

        authorizationStateWaitCode

        authorizationStateWaitRegistration

        authorizationStateWaitPassword
    '''

    @functools.singledispatchmethod
    async def handle_auth_state(self, auth_state:tdg.AuthorizationState, tdlib_handle:tdlib.TdlibHandle) -> None:

        authstate_logger.error("Unimplemented AuthorizationState! we got: `%s`", auth_state)

    @handle_auth_state.register
    async def handle_auth_state_wait_tdlib_params(self, message:tdg.authorizationStateWaitTdlibParameters,
        tdlib_handle:tdlib.TdlibHandle) -> None:


        authstate_logger.debug("handle_auth_state_wait_tdlib_params got message: `%s`", message)

        set_param = tdg.setTdlibParameters(parameters=tdlib_handle.tdlib_parameters_config, extra=utils.new_extra())

        authstate_logger.debug("calling send with setTdlibParameters: `%s`", set_param)
        await tdlib_handle.send(set_param)


    @handle_auth_state.register
    async def handle_auth_state_wait_encryption_key(self, message:tdg.authorizationStateWaitEncryptionKey,
        tdlib_handle:tdlib.TdlibHandle) -> None:

        authstate_logger.debug("handle_auth_state_wait_encryption_key got message: `%s`", message)

        check_key = tdg.checkDatabaseEncryptionKey(encryption_key="", extra=utils.new_extra())
        authstate_logger.debug("calling send with checkDatabaseEncryptionKey: `%s`", check_key)

        await tdlib_handle.send(check_key)









