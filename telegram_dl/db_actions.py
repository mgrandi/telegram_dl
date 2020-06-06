
import functools
import logging
import typing

from telegram_dl import tdlib_generated
from telegram_dl import db_model
from telegram_dl import db_model_enums as dbe
from telegram_dl import utils
from telegram_dl import db_model_equality
from telegram_dl.aides.chat_aide import ChatAide
from telegram_dl.aides.file_aide import FileAide
from telegram_dl.aides.photo_set_aide import PhotoSetAide
from telegram_dl.aides.user_aide import UserAide
from telegram_dl.aides.text_entity_aide import TextEntityAide

import attr
import arrow
import phonenumbers
from sqlalchemy.orm.session import Session
from sqlalchemy import desc

logger = logging.getLogger(__name__)

insert_or_update_logger = logger.getChild("insert_update")
dbaction_handler_logger = logger.getChild("handler")

equality_tester = db_model_equality.DbModelEqualityTester()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InsertOrUpdateResult:
    obj:tdlib_generated.RootObject = attr.ib()
    change:dbe.DatabaseChangeEnum = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BaseDatabaseAction():

    pass

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InsertDatabaseAction(BaseDatabaseAction):

    object_to_insert:tdlib_generated.RootObject = attr.ib()

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InsertOrUpdateParameter:
    '''
    used as a parameter for handler functions in InsertOrUpdateHandler
    so updates to what we pass in don't require mass refactoring
    '''

    session:Session = attr.ib()

class DbActionHandler:

    def __init__(self):

        self.insert_or_update_handler = InsertOrUpdateHandler()

    @functools.singledispatchmethod
    async def handle_database_action(self, obj_to_handle:BaseDatabaseAction, session):

        dbaction_handler_logger.error("handle_database_action: got object: `%s`, UNHANDLED", obj_to_handle)


    @handle_database_action.register
    async def handle_insert_database_action(self, obj_to_handle:InsertDatabaseAction, session):

        dbaction_handler_logger.debug("handle_insert_database_action got object: `%s`", obj_to_handle)

        await self.insert_or_update_handler.handle_insert_or_update(obj_to_handle.object_to_insert,
            InsertOrUpdateParameter(session=session))



class InsertOrUpdateHandler:

    @functools.singledispatchmethod
    async def handle_insert_or_update(self, obj_to_handle:tdlib_generated.RootObject, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        insert_or_update_logger.error("handle_insert_or_update got object: `%s` UNHANDLED", obj_to_handle)

        return None

    @handle_insert_or_update.register
    async def none(self, obj_to_handle:None, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        # noop
        return None


    @handle_insert_or_update.register
    async def message(self, obj_to_handle:tdlib_generated.message, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        # messages are versioned

        session = params.session


        maybe_existing_message = session.query(db_model.Message) \
            .filter(db_model.Message.tg_message_id == obj_to_handle.id) \
            .first()

        change = None

        def _new_message_version_from_tdlib_message(tdl_message:db_model.Message,
            tdlib_message:tdlib_generated.message) -> db_model.Message:
            ''' helper function to create a new MessageVersion from a `tdlib_generated.message`

            @param tdlib_chat - the chat to copy the information from
            @return the new ChatVersion object
            '''

            type_of_message_version = None

            param_dict = {
                "message": tdl_message,
                "as_of": arrow.utcnow(),
                "date": arrow.get(tdlib_message.date),
                "edit_date": arrow.get(tdlib_message.edit_date) if tdlib_message.edit_date != 0 else None,
                "author_signature": tdlib_message.author_signature,
                "ttl": tdlib_message.ttl,
            }

            # handle the different `MessageContent` subclasses to figure out what type
            # we are going to actually create

            if isinstance(tdlib_message.content, tdlib_generated.messageText):

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
                insert_or_update_logger.debug("unhandled MessageContent: `%a`", type(tdlib_message.content))
                return None




        # see if we need to add a Message column or just a MessageVersion
        if not maybe_existing_message:

            change = dbe.DatabaseChangeEnum.NEW

            # Message column doesn't exist, need to add a Message and a MessageVersion

            # this should always exist, except it seems that channel posts have
            # `sender_user_id` set to 0 (aka nothing)
            sender_user = None
            if obj_to_handle.sender_user_id != 0:
                sender_user = session.query(db_model.User) \
                    .filter(db_model.User.tg_user_id == obj_to_handle.sender_user_id) \
                    .first()

            message_chat = session.query(db_model.Chat) \
                .filter(db_model.Chat.tg_chat_id == obj_to_handle.chat_id) \
                .first()

            # see if this message was a reply to another message
            # it seems that if `reply_to_message_id` is 0, that means
            # it was NOT a reply to another message
            reply_to_message = None
            if obj_to_handle.reply_to_message_id != 0:
                reply_to_message = session.query(db_model.Message) \
                    .filter(db_model.Message.tg_message_id == obj_to_handle.reply_to_message_id) \
                    .first()

            # see if this was via a bot
            # it seems that if `via_bot_user_id` is 0, that means a
            # bot did NOT send this message
            bot_user = None
            if obj_to_handle.via_bot_user_id != 0:
                bot_user = session.query(db_model.User) \
                    .filter(db_model.User.tg_user_id == obj_to_handle.via_bot_user_id) \
                    .first()


            new_message = db_model.Message(
                tg_message_id=obj_to_handle.id,
                sender_user=sender_user,
                chat=message_chat,
                reply_to_message=reply_to_message,
                via_bot_user=bot_user,
                is_outgoing=obj_to_handle.is_outgoing,
                is_channel_post=obj_to_handle.is_channel_post,
                can_edit=obj_to_handle.can_be_edited,
                can_forward=obj_to_handle.can_be_forwarded,
                can_be_deleted_only_for_self=obj_to_handle.can_be_deleted_only_for_self,
                can_be_deleted_for_all_users=obj_to_handle.can_be_deleted_for_all_users,
                restriction_reason=obj_to_handle.restriction_reason)

            # now get the


            # create the chat_version and add it to whatever type of chat we get back from the
            # if/else statement
            new_message_version = _new_message_version_from_tdlib_message(new_message, obj_to_handle)

            #### TEMPORARY REMOVE LATER, if we don't have a supported message version just bail entirely

            if not new_message_version:
                return None
            ############################

            new_message.versions.append(new_message_version)

            insert_or_update_logger.debug(
                utils.strip_margin('''message: adding db_model.MessageVersion (`%s) `  `%s`
                |and db_model.Message  `%s` to session with change: `%s`'''),
                    new_message_version, type(new_message_version), new_message, change)

            session.add(new_message)

            return InsertOrUpdateResult(obj=new_message, change=change)


        else:

            # Message column DOES exist, see if it is equal and if we need to
            # add a new MessageVersion

            msg_equality_args = db_model_equality.EqualityArgumentMessage(
                tdl_message=maybe_existing_message, tdg_message=obj_to_handle)
            is_equal = equality_tester.is_equal(msg_equality_args)

            if not is_equal:

                change = dbe.DatabaseChangeEnum.UPDATED

                new_message_version = _new_message_version_from_tdlib_message(maybe_existing_message, obj_to_handle)

                #### TEMPORARY REMOVE LATER,  if we don't have a supported message version just bail entirely

                if not new_message_version:
                    return None
                ############################

                maybe_existing_message.versions.append(new_message_version)

                insert_or_update_logger.debug(
                    utils.strip_margin('''message: adding db_model.MessageVersion (`%s) `  `%s`
                    |to existing db_model.Message  `%s` to session with change: `%s`'''),
                        new_message_version, type(new_message_version), maybe_existing_message, change)

                # TODO: do i need this or does just appending it above add it to the session
                session.add(maybe_existing_message)

                return InsertOrUpdateResult(obj=maybe_existing_message, change=change)


            else:

                # Message / MessageVersion hasn't changed

                insert_or_update_logger.debug(
                    utils.strip_margin('''not adding new db_model.MessageVersion for
                    |db_model.Message `%s`, it already exists and hasn't changed'''),
                        maybe_existing_message)

                return InsertOrUpdateResult(obj=maybe_existing_message, change=dbe.DatabaseChangeEnum.NO_CHANGE)



    @handle_insert_or_update.register
    async def chat(self, object_to_handle:tdlib_generated.chat, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        # chats are versioned

        session = params.session

        # so here, we are seeing if we have the chat already saved
        # it seems that in telegram's ongoing effort to be forward compatable, the IDs for all chats are
        # within the same namespace even though their 'specific' id (for that chat type) is different
        # see `ID notes` in `chat notes.md`
        maybe_existing_chat = ChatAide.get_chat_by_tg_chat_id(session, object_to_handle.id)


        change = None

        if not maybe_existing_chat:

            change = dbe.DatabaseChangeEnum.NEW

            # chat doesn't exist, add a new Chat and one ChatVersion
            result_chat = ChatAide.new_chat_from_tdlib_chat(session, object_to_handle)

            insert_or_update_logger.debug("chat: adding db_model.Chat `%s` to session with change: `%s`",
                result_chat, change)

            session.add(result_chat)

            return InsertOrUpdateResult(obj=result_chat, change=change)


        # see if the latest version matches the chat we got from telegram
        # chat_equality_args = db_model_equality.EqualityArgumentChat(
        #     tdl_chat=maybe_existing_chat, tdg_chat=object_to_handle)

        # is_equal = equality_tester.is_equal(chat_equality_args)

        is_equal = ChatAide.compare_tdlib_and_dbmodel_chat(maybe_existing_chat, object_to_handle)

        if not is_equal:

            # chat already exists, but we need to add a new version

            # new_version = await _new_chat_version_from_tdlib_chat(object_to_handle)
            new_version = ChatAide.new_chat_version_from_tdlib_chat(session, object_to_handle)

            change = dbe.DatabaseChangeEnum.UPDATED

            maybe_existing_chat.versions.append(new_version)

            insert_or_update_logger.debug("chat: adding db_model.ChatVersion `%s` object to `%s` db_model.Chat `%s` to session with change: `%s`",
                new_version, type(maybe_existing_chat), maybe_existing_chat, change)

            session.add(maybe_existing_chat)

            return InsertOrUpdateResult(obj=maybe_existing_chat, change=change)

        else:

            # chat already exists and hasn't changed
            insert_or_update_logger.debug("chat: not adding db_model.ChatVersion object to db_model.Chat `%s` because it already exists and hasn't changed",
                 maybe_existing_chat)

            return InsertOrUpdateResult(obj=maybe_existing_chat, change=dbe.DatabaseChangeEnum.NO_CHANGE)



    @handle_insert_or_update.register
    async def file(self, object_to_handle:tdlib_generated.file, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        # Files should only have one entry per file, we don't do versioning

        session = params.session

        # # see if it exists
        maybe_existing = FileAide.get_file_by_remote_file_id(session, object_to_handle.remote.id)

        file_args = db_model_equality.EqualityArgumentFile(
            tdl_file=maybe_existing,
            tdg_file=object_to_handle)

        is_equal = equality_tester.is_equal(file_args)

        # either doesn't exist or it does exist but has changed
        if not maybe_existing or not is_equal:

            new_file = FileAide.new_file_from_tdlib_file(session, object_to_handle)

            change = dbe.DatabaseChangeEnum.NEW if maybe_existing == None else dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.debug("file: adding db_model.File object `%s` to session with change: `%s`", new_file, change)

            session.add(new_file)

            return InsertOrUpdateResult(obj=new_file, change=change)

        else:

            insert_or_update_logger.debug("file: not adding db_model.File object `%s` because it already exists and hasn't changed",
                 object_to_handle)

            return InsertOrUpdateResult(obj=maybe_existing, change=dbe.DatabaseChangeEnum.NO_CHANGE)


    @handle_insert_or_update.register
    async def chat_photo(self, incoming_chat_photo:tdlib_generated.chatPhoto, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:
        '''
        basically copied from `profile_photo`, except chatPhoto does not have an `id`

        chat photos should be unique

        '''

        session = params.session

        chat_photo_set_result = PhotoSetAide.get_photo_set_from_tdlib_chat_photo(incoming_chat_photo)

        if chat_photo_set_result is None:

            # files are new, so we need to create a Photo for each and then a PhotoSet,
            # then return the ProfilePhotoSet
            new_photo_set = FileAide.new_photo_set_from_tdlib_chatphoto(incoming_profile_photo)

            insert_or_update_logger.debug("chat_photo: adding db_model.PhotoSet object `%s` to session with change: `%s`",
                new_photo_set, dbe.DatabaseChangeEnum.NEW)

            return InsertOrUpdateResult(obj=new_photo_set, change=dbe.DatabaseChangeEnum.NEW)

        else:

            return InsertOrUpdateResult(obj=chat_photo_set_result, change=dbe.DatabaseChangeEnum.NO_CHANGE)



    @handle_insert_or_update.register
    async def user(self, incoming_user:tdlib_generated.user, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        session = params.session

        # users are versioned


        # see if this user version exists
        maybe_existing_user = UserAide.get_user_by_tg_user_id(session, incoming_user.id)

        change = None

        if not maybe_existing_user:

            # create a new user
            new_user = UserAide.new_user_from_tdlib_user(session, incoming_user)

            change = dbe.DatabaseChangeEnum.NEW

            insert_or_update_logger.debug("user:adding new db_model.User object `%s` to session with change: `%s`",
                new_user, change)

            session.add(new_user)

            return InsertOrUpdateResult(obj=new_user, change=change)


        # see if we need a new version?

        is_equal = UserAide.compare_dbmodel_and_tdlib_user(maybe_existing_user, incoming_user)

        if not is_equal:

            # user exists but we need a new version
            new_version = UserAide.new_user_version_from_tdlib_user(session, incoming_user)

            maybe_existing_user.versions.append(new_version)

            change =  dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.debug("user: adding new db_model.UserVersion object `%s`  to existing db_model.User `%s`, to session with change: `%s`",
                new_version, maybe_existing_user, change)

            session.add(maybe_existing_user)

            return InsertOrUpdateResult(obj=maybe_existing_user, change=change)

        else:

            # don't create a new user, old and new one match

            insert_or_update_logger.debug("user: not adding new db_model.UserVersion object for db_model.User `%s` because the latest version hasn't changed",
                maybe_existing_user)

            change = dbe.DatabaseChangeEnum.NO_CHANGE

            return InsertOrUpdateResult(obj=maybe_existing_user, change=change)
