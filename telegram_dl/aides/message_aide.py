from __future__ import annotations
import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
from telegram_dl.aides.text_entity_aide import TextEntityAide
from telegram_dl.aides.chat_aide import ChatAide

import arrow

logger = logging.getLogger(__name__)

class MessageAide:


    def get_message_by_tg_message_id(
        sqla_session:sqlalchemy.orm.session.Session,
        tg_message_id:int) -> typing.Optional[tdg.message]:
        '''
        queries the database for a db_model.Message given the tg_message_id, or
        returns None (see the documentation for `Query.first()` )
        '''

        result = sqla_session.query(db_model.Message) \
            .filter(db_model.Message.tg_message_id == obj_to_handle.id) \
            .first()

        return result


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
            reply_to_message = MessageAide.get_message_by_tg_message_id(
                sqla_session, tdlib_message.reply_to_message_id)

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