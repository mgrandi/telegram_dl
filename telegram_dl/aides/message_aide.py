from __future__ import annotations
import logging
import typing
import functools

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
from telegram_dl.aides.text_entity_aide import TextEntityAide
from telegram_dl.aides.chat_aide import ChatAide
from telegram_dl.aides.user_aide import UserAide

import arrow

logger = logging.getLogger(__name__)

logger_message_content = logger.getChild("message_content_comparison")

class MessageAide:


    @staticmethod
    def get_message_by_tg_message_and_tg_chat_id(
        sqla_session:sqlalchemy.orm.session.Session,
        tg_message_id:int,
        tg_chat_id:int) -> typing.Optional[tdg.message]:
        '''
        queries the database for a db_model.Message given the tg_message_id,
        and tg_chat_id, or returns None (see the documentation for `Query.first()` )

        # TODO: have a version that can take in a dbmodel.Chat to save us one sql lookup
        if we already have a dbmodel.Chat?
        '''


        chat_result = sqla_session.query(db_model.Chat) \
            .filter(db_model.Chat.tg_chat_id == tg_chat_id) \
            .first()

        if chat_result is None:

            logger.debug("no chat found for tg_chat_id `%s`, returning None", tg_chat_id)
            return None

        result = sqla_session.query(db_model.Message) \
            .filter(db_model.Message.tg_message_id == tg_message_id) \
            .filter(db_model.Message.chat_id == chat_result.chat_id) \
            .first()

        return result


    @staticmethod
    def new_message_from_tdlib_message(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_message:tdg.message) -> db_model.Message:
        '''
        creates a new `db_model.Message` from the provided `tdlib_generated.message`
        '''

        # this should always exist, except it seems that channel posts have
        # `sender_user_id` set to 0 (aka nothing)
        sender_user = None
        if tdlib_message.sender_user_id != 0:
            sender_user = UserAide.get_user_by_tg_user_id(sqla_session, tdlib_message.sender_user_id)

        message_chat = ChatAide.get_chat_by_tg_chat_id(sqla_session, tdlib_message.chat_id)

        # see if this message was a reply to another message
        # it seems that if `reply_to_message_id` is 0, that means
        # it was NOT a reply to another message
        reply_to_message = None
        if tdlib_message.reply_to_message_id != 0:
            reply_to_message = MessageAide.get_message_by_tg_message_and_tg_chat_id(
                sqla_session, tdlib_message.reply_to_message_id, tdlib_message.chat_id)

        # see if this was via a bot
        # it seems that if `via_bot_user_id` is 0, that means a
        # bot did NOT send this message
        bot_user = None
        if tdlib_message.via_bot_user_id != 0:
            bot_user = UserAide.get_user_by_tg_user_id(sqla_session, tdlib_message.via_bot_user_id)

        new_message = db_model.Message(
            tg_message_id=tdlib_message.id,
            sender_user=sender_user,
            chat=message_chat,
            reply_to_message=reply_to_message,
            via_bot_user=bot_user,
            is_outgoing=tdlib_message.is_outgoing,
            is_channel_post=tdlib_message.is_channel_post,
            can_edit=tdlib_message.can_be_edited,
            can_forward=tdlib_message.can_be_forwarded,
            can_be_deleted_only_for_self=tdlib_message.can_be_deleted_only_for_self,
            can_be_deleted_for_all_users=tdlib_message.can_be_deleted_for_all_users,
            restriction_reason=tdlib_message.restriction_reason)

        # create the MessageVersion
        new_message_version = MessageAide.new_message_version_from_tdlib_message(
            sqla_session, new_message, tdlib_message)

        #### TEMPORARY REMOVE LATER, if we don't have a supported message version just bail entirely

        if not new_message_version:
            return None
        ############################

        new_message.versions.append(new_message_version)

        return new_message


    @staticmethod
    def new_message_version_from_tdlib_message(
        sqla_session:sqlalchemy.orm.session.Session,
        dbmodel_message:db_model.Message,
        tdlib_message:tdg.message) -> db_model.MessageVersion:
        ''' helper function to create a new MessageVersion from a `tdlib_generated.message`

        @param tdlib_chat - the chat to copy the information from
        @return the new db_model.MessageVersion object
        '''

        type_of_message_version = None

        # common parameters for all `tdlib_generated.MessageContent` subclasses
        # do NOT set 'message' here as the caller is expected to do that
        param_dict = {
            "as_of": arrow.utcnow(),
            "date": arrow.get(tdlib_message.date),
            "edit_date": arrow.get(tdlib_message.edit_date) if tdlib_message.edit_date != 0 else None,
            "author_signature": tdlib_message.author_signature,
            "ttl": tdlib_message.ttl,
        }

        # handle the different `MessageContent` subclasses to figure out what type
        # we are going to actually create

        # TODO: once i start implemtning more messags i should probably extract this out to
        # different functions
        if isinstance(tdlib_message.content, tdg.messageText):

            message_text_content = tdlib_message.content

            type_of_message_version = db_model.MessageVersionText

            # add extra arguments
            param_dict["text"] = message_text_content.text.text
            param_dict["web_page_id"] = None

            new_version = type_of_message_version(**param_dict)

            text_entities =  TextEntityAide.get_text_entities_from_tdlib_text_entity_sequence(
                new_version, message_text_content.text.entities)

            # can i just assign rather than iterating here?
            for iter_te in text_entities:
                new_version.text_entities.append(iter_te)

            return new_version

        else:

            # unhandled message type
            logger.debug("unhandled MessageContent: `%a`", type(tdlib_message.content))
            return None

    @staticmethod
    def compare_dbmodel_and_tdlib_message(
        dbmodel_message:db_model.Message,
        tdlib_message:tdg.message) -> bool:
        '''
        method that compares a `db_model.Message` and a
        `tdlib_generated.message` instance

        note: this just compares the `tdlib_generated.message` part of the
        object, there is also the 'content' that is compared separately
        '''

        if dbmodel_message == None or tdlib_message == None:
            logger.debug("one of the args is None, doing fast comparison")

            fast_result = dbmodel_message == tdlib_message

            logger.debug("fast result: `%s`", fast_result)

            return fast_result

        logger.debug("comparing `%s` and `%s`", dbmodel_message, tdlib_message)


        # check stuff for the base message

        tdl_sender_id = dbmodel_message.sender_user.tg_user_id if dbmodel_message.sender_user else None
        tdg_sender_id = tdlib_message.sender_user_id if tdlib_message.sender_user_id != 0 else None

        tdl_chat_id = dbmodel_message.chat.tg_chat_id if dbmodel_message.chat else None
        tdg_chat_id = tdlib_message.chat_id if tdlib_message.chat_id != 0 else None

        tdl_reply_msg_id = dbmodel_message.reply_to_message.tg_message_id if dbmodel_message.reply_to_message else None
        tdg_reply_msg_id = tdlib_message.reply_to_message_id if tdlib_message.reply_to_message_id != 0 else None

        tdl_via_bot_id = dbmodel_message.via_bot_user.tg_user_id if dbmodel_message.via_bot_user else None
        tdg_via_bot_id = tdlib_message.via_bot_user_id if tdlib_message.via_bot_user_id != 0 else None

        base_message_result = isinstance(dbmodel_message, db_model.Message) \
            and isinstance(tdlib_message, tdg.message) \
            and dbmodel_message.tg_message_id == tdlib_message.id \
            and tdl_sender_id == tdg_sender_id \
            and tdl_chat_id == tdg_chat_id \
            and tdl_reply_msg_id == tdg_reply_msg_id \
            and tdl_via_bot_id == tdg_via_bot_id \
            and dbmodel_message.is_outgoing == tdlib_message.is_outgoing \
            and dbmodel_message.is_channel_post == tdlib_message.is_channel_post \
            and dbmodel_message.can_edit == tdlib_message.can_be_edited \
            and dbmodel_message.can_forward == tdlib_message.can_be_forwarded \
            and dbmodel_message.can_be_deleted_only_for_self == tdlib_message.can_be_deleted_only_for_self \
            and dbmodel_message.can_be_deleted_for_all_users  == tdlib_message.can_be_deleted_for_all_users \
            and dbmodel_message.restriction_reason == tdlib_message.restriction_reason

        # now check the versions

        if len(dbmodel_message.versions) == 0:
            logger.debug("returning False because Chat exists but has no versions")
            return False

        latest_msg_version = dbmodel_message.versions[-1]

        # so messages are fun, since they have a base `MessageVersion` which has the common
        # shared info among all of the `messageContent` subclasses and then there are
        # subclasses of `MessageVersion` that have extra fields based on the `MessageContent`
        # type, so we call the equality methods for those types
        msg_ver_result = MessageContentComparisonMethodDispatcher.compare_dbmodel_message_ver_and_tdlib_message_content(
            latest_msg_version, tdlib_message)

        final_result = base_message_result and msg_ver_result

        logger.debug("final result: base: `%s` , msgver: `%s`, final: `%s`",
            base_message_result, msg_ver_result, final_result)

        return final_result


class MessageContentComparisonMethodDispatcher:
    '''
    class that just holds the methods for comparing the different subclasses
    of tdlib_generated.MessageContent

    every method will return a true or a false for if the passed in db_model.MessageVersion
    differs from the passed in tdlib_generated.message instance's `content`

    '''

    @functools.singledispatchmethod
    @staticmethod
    def compare_dbmodel_message_ver_and_tdlib_message_content(
        dbmodel_message_version:db_model.MessageVersion,
        tdlib_message:tdg.message) -> bool:
        '''
        the 'default' single dispatch method that gets called if nothing else matches

        we return None here and log it, since reaching here means we don't support the given
        tdlib_generated.MessageContent yet
        '''

        logger_message_content.debug("unhandled MessageContent! dbmodel_message: `%s`, tdlib_message: `%s`",
            dbmodel_message, tdlib_message)

        return False

    @compare_dbmodel_message_ver_and_tdlib_message_content.register
    def compare_message_text(
        dbmodel_message_version_text:db_model.MessageVersionText,
        tdlib_message:tdg.message) -> bool:

        if dbmodel_message_version_text is None or \
            tdlib_message is None:

            logger_message_content.debug("one of the args is None, doing fast comparison")

            fast_result = dbmodel_message_version_text == tdlib_message

            logger_message_content.debug("fast result: `%s`", fast_result)

            return fast_result

        logger_message_content.debug("comparing: `%s` and `%s`", dbmodel_message_version_text, tdlib_message)

        # TODO HANDLE THE `web_page` argument
        logger_message_content.debug("TODO `tdg.messageText.web_page` parameter is unchecked")

        message_ver_text_result = isinstance(dbmodel_message_version_text, db_model.MessageVersionText) \
            and isinstance(tdlib_message, tdg.message) \
            and dbmodel_message_version_text.text == tdlib_message.content.text.text

        # check the text entities
        text_entity_result = TextEntityAide.compare_dbmodel_and_tdlib_text_entities(
            dbmodel_text_entities=dbmodel_message_version_text.text_entities,
            tdlib_message=tdlib_message)

        final_result = message_ver_text_result and text_entity_result

        logger_message_content.debug("final result: message_version_text: `%s` , text_entities: `%s`, final: `%s`",
            message_ver_text_result, text_entity_result, final_result)

        return final_result
