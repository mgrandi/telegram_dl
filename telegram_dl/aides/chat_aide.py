import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
from telegram_dl.aides import photo_set_aide

logger = logging.getLogger(__name__)

class ChatAide:


    def __init__(self):

        pass

    @staticmethod
    def compare_tdlib_and_dbmodel_chat(
        dbmodel_chat:typing.Optional[db_model.Chat],
        tdlib_chat:typing.Optional[tdg.chat]) -> bool:
        '''
        method chat compares a `telegram_dl.db_model.Chat` and a
        `telegram_dl.tdlib_generated.chat` instance

        '''

        logger.debug("comparing `%s` and `%s`", dbmodel_chat, tdlib_chat)

        if dbmodel_chat is None or tdlib_chat is None:
            logger.debug("one of the args is None, doing fast comparison")

            fast_result = dbmodel_chat == tdlib_chat

            logger.debug("fast result: `%s`", fast_result)

            return fast_result

        if len(dbmodel_chat.tdl_chat.versions) == 0:

            logger.debug("returning False because Chat exists but has no versions")
            return False

        # check the base chat
        base_chat_comparison = isinstance(dbmodel_chat, db_model.Chat) \
            and isinstance(tdlib_chat, tdg.chat) \
            and dbmodel_chat.tg_chat_id == tdlib_chat.id

        # get the latest version

        # should be sorted by ascending so the LAST index is the latest

        latest_version = dbmodel_chat.versions[-1]

        chat_version_comparison = tdlib_chat is not None \
            and isinstance(tdlib_chat, tdg.chat) \
            and latest_version.chat.tg_chat_id == tdlib_chat.id \
            and latest_version.title ==tdlib_chat.title \
            and latest_version.is_sponsored == tdlib_chat.is_sponsored


        # chat_photo_arg = EqualityArgumentChatPhoto(
        #     tdl_photo_set=latest_version.photo_set,
        #     tdg_chat_photo=chat_arg.tdg_chat.photo)

        # chat_photo_result = self.is_equal(chat_photo_arg)

        chat_photo_result = photo_set_aide.PhotoSetAide.compare_dbmodel_photoset_and_tdlib_chatphoto(
            dbmodel_photoset=latest_version.photo_set,
            tdlib_chatphoto=tdlib_chat.photo)

        # get final result
        final_result =  base_chat_comparison and chat_version_comparison and chat_photo_result

        logger.debug("final result: `%s`", final_result)

        return final_result


    @staticmethod
    def get_latest_dbmodel_chat_by_telegram_chat_id(sqla_session) -> typing.Optional[db_model.Chat]:

        pass


    @staticmethod
    def new_chat_version_from_tdlib_chat(tdlib_chat:tdg.chat) -> db_model.ChatVersion:

        pass


    @staticmethod
    def new_chat_from_tdlib_chat():
        pass
