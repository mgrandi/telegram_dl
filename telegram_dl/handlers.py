import functools
import logging
import typing

import attr

from telegram_dl import tdlib
from telegram_dl import constants
from telegram_dl import tdlib_generated as tdg

logger = logging.getLogger(__name__)

authstate_logger = logger.getChild("authstate")


class TdlibBaseMessageHandler:

    @staticmethod
    @functools.singledispatch
    async def handle_message(message:tdg.RootObject, tdlib_handle:tdlib.TdlibHandle) -> typing.Optional[tdlib.TdlibResult]:

        logger.error("TdlibBaseMessageHandler.handle_message got `%s`", message)
        return tdlib.TdlibResult(
            code=constants.TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED,
            message=f"Unimplemented message of type `{type(message)}`: `{message}`",
            result_obj=None)





class BaseAuthenticationHandle:
    ''' this is so i can register with the single dispatch function
    or else it complains that it doesn't exist becuase it hasn't finished
    reading the class yet
    '''

    @staticmethod
    @functools.singledispatch
    async def handle_auth_state(auth_state:tdg.AuthorizationState, tdlib_handle:tdlib.TdlibHandle) -> None:

        authstate_logger.error("Unimplemented AuthorizationState! we got: `%s`", auth_state)


class AuthenticationHandler:
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


    @staticmethod
    @BaseAuthenticationHandle.handle_auth_state.register
    async def handle_auth_state_wait_tdlib_params(message:tdg.authorizationStateWaitTdlibParameters, tdlib_handle:tdlib.TdlibHandle) -> None:



        authstate_logger.debug("handle_auth_state_wait_tdlib_params got message: `%s`", message)

        set_param = tdg.setTdlibParameters(parameters=tdlib_handle.tdlib_parameters_config)

        authstate_logger.debug("calling send with setTdlibParameters")
        await tdlib_handle.send(set_param)

    @staticmethod
    @TdlibBaseMessageHandler.handle_message.register
    async def handle_message_update_auth_state(message:tdg.updateAuthorizationState, tdlib_handle:tdlib.TdlibHandle) -> tdlib.TdlibResult:

        logger.debug("handle_message_update_authorization_state.handle_message got `%s`", message)

        auth_state = message.authorization_state

        await BaseAuthenticationHandle.handle_auth_state(auth_state, tdlib_handle)

        return tdlib.TdlibResult(
                code=constants.TDLIB_RESULT_CODE_OK,
                message=f"OK",
                result_obj=None)







