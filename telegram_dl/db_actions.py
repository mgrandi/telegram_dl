
import functools
import logging
import typing

from telegram_dl import tdlib_generated
from telegram_dl import db_model
from telegram_dl import db_model_enums as dbe
from telegram_dl import utils
from telegram_dl import db_model_equality

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

        def _create_text_entities_for_text_message(tdl_message_ver:db_model.MessageVersion, tdlib_message:tdlib_generated.message) -> typing.Sequence[db_model.TextEntity]:

            if not isinstance(tdlib_message.content, tdlib_generated.messageText):
                raise Exception(utils.strip_margin('''_create_text_entities_for_text_message called with a message that
                    |doesn't have a messageText as its `content`! message: `%s`'''), tdlib_message)

            result_list = []

            for iter_te in tdlib_message.content.text.entities:

                new_entity = db_model.TextEntity(
                    message=tdl_message_ver,
                    offset=iter_te.offset,
                    length=iter_te.length,
                    text_entity_type=dbe.TextEntityTypeEnum.parse_from_tdg_text_entity_type(iter_te.type))

                result_list.append(new_entity)

            insert_or_update_logger.debug("text entities created: `%s`", result_list)

            return result_list



        def _new_message_version_from_tdlib_message(tdl_message:db_model.Message, tdlib_message:tdlib_generated.message) -> db_model.Message:
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

                type_of_message_version = db_model.MessageVersionText

                # add extra arguments
                param_dict["text"] = tdlib_message.content.text.text
                param_dict["web_page_id"] = None

                new_version = type_of_message_version(**param_dict)

                text_entities =  _create_text_entities_for_text_message(new_version, tdlib_message)

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

            #### TEMPORARY REMOVE LATER

            if not new_message_version:
                return None
            ############################

            new_message.versions.append(new_message_version)

            insert_or_update_logger.info("message: adding db_model.MessageVersion (`%s) `  `%s`  and db_model.Message  `%s` to session with change: `%s`",
                new_message_version, type(new_message_version), new_message, change)

            session.add(new_message)

            return InsertOrUpdateResult(obj=new_message, change=change)


        else:

            # Message column DOES exist, see if it is equal and if we need to
            # add a new MessageVersion

            # TODO IMPLEMENT
            return None





    @handle_insert_or_update.register
    async def chat(self, object_to_handle:tdlib_generated.chat, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        # chats are versioned


        async def _new_chat_version_from_tdlib_chat(tdlib_chat:tdlib_generated.chat) -> db_model.ChatVersion:
            ''' helper function to create a new ChatVersion from a `tdlib_generated.chat`

            @param tdlib_chat - the chat to copy the information from
            @return the new ChatVersion object
            '''

            profile_photo_set_result = await self.handle_insert_or_update(object_to_handle.photo, params)

            new_ver = db_model.ChatVersion(
                as_of=arrow.utcnow(),
                title=tdlib_chat.title,
                photo_set=profile_photo_set_result.obj if profile_photo_set_result else None,
                is_sponsored=tdlib_chat.is_sponsored)

            return new_ver


        session = params.session

        # so here, we are seeing if we have the chat already saved
        # it seems that in telegram's ongoing effort to be forward compatable, the IDs for all chats are
        # within the same namespace even though their 'specific' id (for that chat type) is different
        # see `ID notes` in `chat notes.md`
        maybe_existing_chat = session.query(db_model.Chat) \
            .filter(db_model.Chat.tg_chat_id == object_to_handle.id) \
            .first()

        change = None

        if not maybe_existing_chat:

            change = dbe.DatabaseChangeEnum.NEW

            # chat doesn't exist, add a new Chat and one ChatVersion

            # parameters that fit all `chat` types, since this table is polymorphic
            chat_instance_parameters_dict = dict(
                tg_chat_id=object_to_handle.id,
            )

            chat_type = object_to_handle.type

            result_chat = None

            if isinstance(chat_type, tdlib_generated.chatTypeBasicGroup):

                chat_instance_parameters_dict["tg_basic_group_id"] = chat_type.basic_group_id

                result_chat = db_model.BasicGroupChat(**chat_instance_parameters_dict)


            elif isinstance(chat_type, tdlib_generated.chatTypePrivate):

                other_user = session.query(db_model.User) \
                    .filter(db_model.User.tg_user_id == chat_type.user_id) \
                    .one()

                chat_instance_parameters_dict["user"] = other_user

                result_chat = db_model.PrivateChat(**chat_instance_parameters_dict)

            elif isinstance(chat_type, tdlib_generated.chatTypeSecret):

                other_secret_user = session.query(db_model.User) \
                    .filter(db_model.User.tg_user_id == chat_type.secret_user_id) \
                    .one()

                chat_instance_parameters_dict["user"] = other_secret_user
                chat_instance_parameters_dict["tg_secret_chat_id"] = chat_type.secret_chat_id

                result_chat = db_model.SecretChat(**chat_instance_parameters_dict)

            elif isinstance(chat_type, tdlib_generated.chatTypeSupergroup):

                chat_instance_parameters_dict["tg_super_group_id"] = chat_type.supergroup_id
                chat_instance_parameters_dict["is_channel"] = chat_type.is_channel

                result_chat = db_model.SuperGroupChat(**chat_instance_parameters_dict)

            else:

                insert_or_update_logger.error("chat: Unrecognized chat type? we got: `%s`", object_to_handle)

                return InsertOrUpdateResult(obj=None, change=dbe.DatabaseChangeEnum.NO_CHANGE)

            # create the chat_version and add it to whatever type of chat we get back from the
            # if/else statement
            tmp_chat_ver = await _new_chat_version_from_tdlib_chat(object_to_handle)
            result_chat.versions.append(tmp_chat_ver)

            insert_or_update_logger.info("chat: adding db_model.ChatVersion `%s` object to `%s` db_model.Chat `%s` to session with change: `%s`",
                tmp_chat_ver, type(result_chat), result_chat, change)

            session.add(result_chat)

            return InsertOrUpdateResult(obj=result_chat, change=change)


        # see if the latest version matches the chat we got from telegram
        chat_equality_args = db_model_equality.EqualityArgumentChat(
            tdl_chat=maybe_existing_chat, tdg_chat=object_to_handle)

        is_equal = equality_tester.is_equal(chat_equality_args)

        if not is_equal:

            # chat already exists, but we need to add a new version

            new_version = await _new_chat_version_from_tdlib_chat(object_to_handle)

            change = dbe.DatabaseChangeEnum.UPDATED

            maybe_existing_chat.versions.append(new_version)

            insert_or_update_logger.info("chat: adding db_model.ChatVersion `%s` object to `%s` db_model.Chat `%s` to session with change: `%s`",
                new_version, type(maybe_existing_chat), maybe_existing_chat, change)

            session.add(maybe_existing_chat)

            return InsertOrUpdateResult(obj=maybe_existing_chat, change=change)

        else:

            # chat already exists
            insert_or_update_logger.debug("chat: not adding db_model.ChatVersion object to db_model.Chat `%s` because it already exists and hasn't changed",
                 maybe_existing_chat)

            return InsertOrUpdateResult(obj=maybe_existing_chat, change=dbe.DatabaseChangeEnum.NO_CHANGE)



    @handle_insert_or_update.register
    async def file(self, object_to_handle:tdlib_generated.file, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        # Files should only have one entry per file, we don't do versioning

        session = params.session

        # # see if it exists
        maybe_existing = session.query(db_model.File).filter(db_model.File.remote_file_id == object_to_handle.remote.id).first()

        file_args = db_model_equality.EqualityArgumentFile(
            tdl_file=maybe_existing,
            tdg_file=object_to_handle)

        is_equal = equality_tester.is_equal(file_args)

        # either doesn't exist or it does exist but has changed
        if not maybe_existing or not is_equal:

            new_file = db_model.File(tg_file_id=object_to_handle.id,
                size=object_to_handle.size,
                expected_size=object_to_handle.expected_size,
                remote_file_id=object_to_handle.remote.id,
                remote_unique_id=object_to_handle.remote.unique_id if object_to_handle.remote.unique_id else None)

            change = dbe.DatabaseChangeEnum.NEW if maybe_existing == None else dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.info("file: adding db_model.File object `%s` to session with change: `%s`", new_file, change)

            session.add(new_file)

            return InsertOrUpdateResult(obj=new_file, change=change)

        else:

            insert_or_update_logger.debug("file: not adding db_model.File object `%s` because it already exists and hasn't changed",
                 object_to_handle)

            return InsertOrUpdateResult(obj=maybe_existing, change=dbe.DatabaseChangeEnum.NO_CHANGE)


    @handle_insert_or_update.register
    async def chat_photo(self, incoming_profile_photo:tdlib_generated.chatPhoto, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:
        '''
        basically copied from `profile_photo`, except chatPhoto does not have an `id`

        chat photos should be unique

        '''

        session = params.session

        # see if it exists

        # see if the big and small files exist
        big_photo_file_result = await self.handle_insert_or_update(incoming_profile_photo.big, params)
        small_photo_file_result = await self.handle_insert_or_update(incoming_profile_photo.small, params)

        if big_photo_file_result.change == dbe.DatabaseChangeEnum.NO_CHANGE and \
            small_photo_file_result.change == dbe.DatabaseChangeEnum.NO_CHANGE:

            # files already exist, return the profile_photo_set that already exists

            existing_photo_set = session.query(db_model.PhotoSet) \
                .join(db_model.Photo) \
                .filter(db_model.Photo.file_id == big_photo_file_result.obj.file_id) \
                .first()

            insert_or_update_logger.debug("chat_photo: not adding db_model.PhotoSet object `%s` because it already exists or hasn't changed",
                existing_photo_set)

            return InsertOrUpdateResult(obj=existing_photo_set, change=dbe.DatabaseChangeEnum.NO_CHANGE)

        else:

            # files are new, so we need to create a Photo for each and then a PhotoSet,
            # then return the ProfilePhotoSet
            new_photo_set = db_model.PhotoSet()

            big_photo = db_model.Photo(
                thumbnail_type=dbe.PhotoSizeThumbnailType.PHOTO_BIG,
                width=-1,
                height=-1,
                has_stickers=False,
                file=big_photo_file_result.obj)

            small_photo = db_model.Photo(
                thumbnail_type=dbe.PhotoSizeThumbnailType.PHOTO_SMALL,
                width=-1,
                height=-1,
                has_stickers=False,
                file=small_photo_file_result.obj)

            new_photo_set.photos.append(big_photo)
            new_photo_set.photos.append(small_photo)

            insert_or_update_logger.info("chat_photo: adding db_model.PhotoSet object `%s` to session with change: `%s`",
                new_photo_set, dbe.DatabaseChangeEnum.NEW)

            return InsertOrUpdateResult(obj=new_photo_set, change=dbe.DatabaseChangeEnum.NEW)


    @handle_insert_or_update.register
    async def profile_photo(self, incoming_profile_photo:tdlib_generated.profilePhoto, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        session = params.session

        # profile photos should be unique

        # see if it exists

        # see if the big and small files exist
        big_photo_file_result = await self.handle_insert_or_update(incoming_profile_photo.big, params)
        small_photo_file_result = await self.handle_insert_or_update(incoming_profile_photo.small, params)

        if big_photo_file_result.change == dbe.DatabaseChangeEnum.NO_CHANGE and \
            small_photo_file_result.change == dbe.DatabaseChangeEnum.NO_CHANGE:

            # files already exist, return the profile_photo_set that already exists

            existing_profile_photo_set = session.query(db_model.ProfilePhotoSet) \
                .join(db_model.Photo) \
                .filter(db_model.Photo.file_id == big_photo_file_result.obj.file_id) \
                .first()

            insert_or_update_logger.debug("profile_photo: not adding db_model.ProfilePhotoSet object `%s` because it already exists or hasn't changed",
                existing_profile_photo_set)

            return InsertOrUpdateResult(obj=existing_profile_photo_set, change=dbe.DatabaseChangeEnum.NO_CHANGE)

        else:

            # files are new, so we need to create a Photo for each and then a ProfilePhotoSet,
            # then return the ProfilePhotoSet
            new_photo_set = db_model.ProfilePhotoSet(
                tg_id=incoming_profile_photo.id)

            big_photo = db_model.Photo(
                thumbnail_type=dbe.PhotoSizeThumbnailType.PHOTO_BIG,
                width=-1,
                height=-1,
                has_stickers=False,
                file=big_photo_file_result.obj)

            small_photo = db_model.Photo(
                thumbnail_type=dbe.PhotoSizeThumbnailType.PHOTO_SMALL,
                width=-1,
                height=-1,
                has_stickers=False,
                file=small_photo_file_result.obj)

            new_photo_set.photos.append(big_photo)
            new_photo_set.photos.append(small_photo)

            insert_or_update_logger.info("profile_photo: adding db_model.ProfilePhotoSet object `%s` to session with change: `%s`",
                new_photo_set, dbe.DatabaseChangeEnum.NEW)

            return InsertOrUpdateResult(obj=new_photo_set, change=dbe.DatabaseChangeEnum.NEW)


    @handle_insert_or_update.register
    async def user(self, incoming_user:tdlib_generated.user, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        session = params.session

        # users are versioned

        async def _new_version_from_tdlib_user(tdlib_user:tdlib_generated.user) -> db_model.UserVersion:
            ''' helper function to create a UserVersion

            @param tdlib_user the tdlib user to copy info from
            @return the UserVersion model object
            '''

            # add the + sign so it parses correctly
            fixed_phone_number = utils.fix_phone_number(tdlib_user.phone_number) if tdlib_user.phone_number else ""

            profile_photo_set_result = await self.handle_insert_or_update(tdlib_user.profile_photo, params)

            new_version = db_model.UserVersion(
                as_of=arrow.utcnow(),
                first_name=tdlib_user.first_name,
                last_name=tdlib_user.last_name,
                user_name=tdlib_user.username,
                phone_number=fixed_phone_number,
                is_contact=True if tdlib_user.is_contact == 1 else False,
                is_mutual_contact=True if tdlib_user.is_mutual_contact == 1 else False,
                profile_photo_set=profile_photo_set_result.obj if profile_photo_set_result is not None else None,
                is_verified=tdlib_user.is_verified,
                is_support=tdlib_user.is_support,
                restriction_reason=tdlib_user.restriction_reason,
                is_scam=tdlib_user.is_scam,
                have_access=tdlib_user.have_access,
                user_type=dbe.UserTypeEnum.parse_from_tdg_usertype(tdlib_user.type),
                language_code=tdlib_user.language_code)

            return new_version

        # see if this user version exists
        maybe_existing_user = session.query(db_model.User) \
            .filter(db_model.User.tg_user_id == incoming_user.id) \
            .first()

        change = None

        if not maybe_existing_user:

            # create a new user
            new_user = db_model.User(tg_user_id=incoming_user.id)

            new_version = await _new_version_from_tdlib_user(incoming_user)

            new_user.versions.append(new_version)

            change = dbe.DatabaseChangeEnum.NEW

            insert_or_update_logger.info("user:adding new db_model.User object `%s` and new db_model.UserVersion `%s` to session with change: `%s`",
                new_user, new_version, change)
            session.add(new_user)

            return InsertOrUpdateResult(obj=new_user, change=change)


        # see if we need a new version?

        user_args = db_model_equality.EqualityArgumentUser(
            tdl_user=maybe_existing_user,
            tdg_user=incoming_user)

        is_equal = equality_tester.is_equal(user_args)

        if not is_equal:

            # user exists but we need a new version
            new_version = await _new_version_from_tdlib_user(incoming_user)

            maybe_existing_user.versions.append(new_version)

            change =  dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.info("user: adding new db_model.UserVersion object `%s`  to existing db_model.User `%s`, to session with change: `%s`",
                new_version, maybe_existing_user, change)

            session.add(maybe_existing_user)

            return InsertOrUpdateResult(obj=maybe_existing_user, change=change)

        else:

            # don't create a new user, old and new one match

            insert_or_update_logger.debug("user: not adding new db_model.UserVersion object for db_model.User `%s` because the latest version hasn't changed",
                maybe_existing_user)

            change = dbe.DatabaseChangeEnum.NO_CHANGE

            return InsertOrUpdateResult(obj=maybe_existing_user, change=change)
