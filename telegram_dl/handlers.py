import functools
import logging

import attr

from telegram_dl.tdlib import TdlibResult
from telegram_dl import constants
from telegram_dl import tdlib_generated

logger = logging.getLogger(__name__)




class TdlibBaseMessageHandler:

    @staticmethod
    @functools.singledispatch
    async def handle_message(message:tdlib_generated.RootObject) -> TdlibResult:

        logger.debug("TdlibBaseMessageHandler.handle_message got `%s`", message)
        return new TdlibResult(
            code=constants.TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED,
            message=f"Unimplemented message of type `{type(message)}`: `{message}`")







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

    @TdlibBaseMessageHandler.handle_message.register
    async def handle_message_update_uthorization_state(message:tdlib_generated.updateAuthorizationState) -> TdlibResult:

        logger.debug("handle_message_update_uthorization_state.handle_message got `%s`", message)

        return new TdlibResult(
            code=constants.TDLIB_RESULT_CODE_MANUAL_MESSAGE_NOT_HANDLED,
            message=f"Unimplemented message of type `{type(message)}`: `{message}`")



