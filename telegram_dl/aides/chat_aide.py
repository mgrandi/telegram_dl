from __future__ import annotations

import logging
import typing
import itertools

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
from telegram_dl.aides.photo_set_aide import PhotoSetAide

import arrow

logger = logging.getLogger(__name__)

class ChatAide:


    def __init__(self):

        pass


    @staticmethod
    def get_chat_by_tg_chat_id(
        sqla_session:sqlalchemy.orm.session.Session,
        tg_chat_id_to_get:int) -> typing.Optional[db_model.Chat]:
        '''
        queries the database for a db_model.Chat given the tg_chat_id, or
        returns None (see the documentation for `Query.first()` )
        '''

        maybe_existing_chat = sqla_session.query(db_model.Chat) \
            .filter(db_model.Chat.tg_chat_id == tg_chat_id_to_get) \
            .first()

        return maybe_existing_chat

    @staticmethod
    def new_chat_version_from_tdlib_chat(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_chat:tdlib_generated.chat) -> db_model.ChatVersion:
        '''
        returns a new ChatVersion from a `tdlib_generated.chat`

        @param tdlib_chat - the chat to copy the information from
        @return the new ChatVersion object
        '''

        # see if the photo set exists
        photo_set_result = None

        # some chats have no photo, handle them here
        if tdlib_chat.photo is not None:

            get_photo_set_result  = PhotoSetAide.get_photo_set_from_tdlib_chat_photo(
                sqla_session, tdlib_chat.photo)

            if get_photo_set_result is None:
                # if it doesn't exist in the database, then we need to create a new one
                photo_set_result = PhotoSetAide.new_photo_set_from_tdlib_chatphoto(
                    sqla_session, tdlib_chat.photo)
            else:
                # already exists in the database, don't create a new one
                photo_set_result = get_photo_set_result



        new_ver = db_model.ChatVersion(
            as_of=arrow.utcnow(),
            title=tdlib_chat.title,
            photo_set=photo_set_result,
            is_sponsored=tdlib_chat.is_sponsored)

        return new_ver

    @staticmethod
    def new_chat_from_tdlib_chat(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_chat:tdg.chat):
        '''
        returns a new `db_model.Chat` instance given a `tdlib_generated.chat` instance
        '''

        # parameters that fit all `chat` types, since this table is polymorphic
        chat_instance_parameters_dict = dict(
            tg_chat_id=tdlib_chat.id,
        )

        chat_type = tdlib_chat.type

        result_chat = None

        if isinstance(chat_type, tdg.chatTypeBasicGroup):

            chat_instance_parameters_dict["tg_basic_group_id"] = chat_type.basic_group_id

            result_chat = db_model.BasicGroupChat(**chat_instance_parameters_dict)


        elif isinstance(chat_type, tdg.chatTypePrivate):

            # TODO: MAKE THIS USE `UserAide` when done
            other_user = sqla_session.query(db_model.User) \
                .filter(db_model.User.tg_user_id == chat_type.user_id) \
                .one()

            chat_instance_parameters_dict["user"] = other_user

            result_chat = db_model.PrivateChat(**chat_instance_parameters_dict)

        elif isinstance(chat_type, tdg.chatTypeSecret):

            # TODO: MAKE THIS USE `UserAide` when done
            other_secret_user = sqla_session.query(db_model.User) \
                .filter(db_model.User.tg_user_id == chat_type.secret_user_id) \
                .one()

            chat_instance_parameters_dict["user"] = other_secret_user
            chat_instance_parameters_dict["tg_secret_chat_id"] = chat_type.secret_chat_id

            result_chat = db_model.SecretChat(**chat_instance_parameters_dict)

        elif isinstance(chat_type, tdg.chatTypeSupergroup):

            chat_instance_parameters_dict["tg_super_group_id"] = chat_type.supergroup_id
            chat_instance_parameters_dict["is_channel"] = chat_type.is_channel

            result_chat = db_model.SuperGroupChat(**chat_instance_parameters_dict)

        else:

            raise Exception(f"chat: Unrecognized chat type? we got: `{tdlib_chat}`")

        # create the chat_version and add it to whatever type of chat we get back from the
        # if/else statement
        tmp_chat_ver = ChatAide.new_chat_version_from_tdlib_chat(sqla_session, tdlib_chat)
        result_chat.versions.append(tmp_chat_ver)

        return result_chat

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

        if len(dbmodel_chat.versions) == 0:

            logger.debug("returning False because Chat exists but has no versions")
            return False

        # here we need to check the db_model.Chat subclasses
        # here is a list of booleans and we will check all of them to make the
        # final result
        base_chat_comparison_result_list = list()

        # base chat checks
        base_chat_comparison_result_list.append(isinstance(dbmodel_chat, db_model.Chat))
        base_chat_comparison_result_list.append(isinstance(tdlib_chat, tdg.chat))
        base_chat_comparison_result_list.append(dbmodel_chat.tg_chat_id == tdlib_chat.id)


        # chat subclass checks
        if isinstance(dbmodel_chat, db_model.PrivateChat):

            base_chat_comparison_result_list.append(dbmodel_chat.user_id == tdlib_chat.type.user_id)

        elif isinstance(dbmodel_chat, db_model.SecretChat):

            base_chat_comparison_result_list.append(dbmodel_chat.tg_secret_chat_id == tdlib_chat.type.secret_chat_id)
            base_chat_comparison_result_list.append(dbmodel_chat.user.tg_user_id == tdlib_chat.type.user_id)

        elif isinstance(dbmodel_chat, db_model.BasicGroupChat):

            base_chat_comparison_result_list.append(dbmodel_chat.tg_basic_group_id == tdlib_chat.type.basic_group_id)

        elif isinstance(dbmodel_chat, db_model.SuperGroupChat):

            base_chat_comparison_result_list.append(dbmodel_chat.tg_super_group_id == tdlib_chat.type.supergroup_id)
            base_chat_comparison_result_list.append(dbmodel_chat.is_channel == tdlib_chat.type.is_channel)

        else:
            raise Exception(
                f"tried to compare a `db_model.Chat` subclass that isn't supported! Chat: `{dbmodel_chat}`")

        # count the number of False booleans in the list, if there are any then the entire predicate
        # fails. basically a fancy way of iterating and doing a running `x and y` thing
        # note: If predicate is None, return the items that are false
        filterfalse_result_list = list(itertools.filterfalse(None, base_chat_comparison_result_list))
        base_chat_comparison = len(filterfalse_result_list) == 0

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

        chat_photo_result = PhotoSetAide.compare_dbmodel_photoset_and_tdlib_chatphoto(
            dbmodel_photoset=latest_version.photo_set,
            tdlib_chatphoto=tdlib_chat.photo)

        # get final result
        final_result =  base_chat_comparison and chat_version_comparison and chat_photo_result

        logger.debug("final result: `%s`", final_result)

        return final_result


    @staticmethod
    def get_dbmodel_chat_by_telegram_chat_id(
        sqla_session:sqlalchemy.orm.session.Session,
        tg_chat_id:int) -> typing.Optional[db_model.Chat]:

        maybe_existing_chat = session.query(db_model.Chat) \
            .filter(db_model.Chat.tg_chat_id == object_to_handle.id) \
            .first()

        return maybe_existing_chat


    @staticmethod
    def get_latest_dbmodel_chat_version_by_telegram_chat_id():
        pass
