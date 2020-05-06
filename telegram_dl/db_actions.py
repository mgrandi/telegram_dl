
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
    async def chat(self, object_to_handle:tdlib_generated.chat, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        # chats are versioned

        session = params.session

        # so here, we are seeing if we have the chat already saved
        # it seems that in telegram's ongoing effort to be forward compatable, the IDs for all chats are
        # within the same namespace even though their 'specific' id (for that chat type) is different
        # see `ID notes` in `chat notes.md`
        maybe_existing_chat = session.query(db_model.Chat) \
            .filter(db_model.Chat.tg_chat_id == object_to_handle.id) \
            .first()


        # get the latest ChatVersion and see if that matches what we are getting from
        # the `tdlib_generated.chat` we get passed in
        # TODO: IMPLEMENT
        is_equal = True

        change = dbe.DatabaseChangeEnum.NEW if maybe_existing_chat == None else dbe.DatabaseChangeEnum.UPDATED

        if not maybe_existing_chat or not is_equal:

            # chat doesn't exist add it

            profile_photo_set_result = await self.handle_insert_or_update(object_to_handle.photo, params)

            # parameters that fit all `chat` types, since this table is polymorphic
            chat_instance_parameters_dict = dict(
                tg_chat_id=object_to_handle.id,
            )

            chat_version_instance_parameters_dict = dict(
                as_of=arrow.utcnow(),
                title=object_to_handle.title,
                photo_set=profile_photo_set_result.obj if profile_photo_set_result else None,
                is_sponsored=object_to_handle.is_sponsored,
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
            tmp_chat_ver = db_model.ChatVersion(**chat_version_instance_parameters_dict)
            result_chat.versions.append(tmp_chat_ver)

            insert_or_update_logger.info("chat: adding `%s` object `%s` to session with change: `%s`",
                type(result_chat), result_chat, change)

            session.add(result_chat)

            return InsertOrUpdateResult(obj=result_chat, change=change)

        else:

            # chat already exists
            insert_or_update_logger.debug("chat: not adding db_model.Chat object `%s` because it already exists and hasn't changed",
                 object_to_handle)

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
                thumbnail_type=dbe.PhotoSizeThumbnailType.PROFILE_PHOTO_BIG,
                width=-1,
                height=-1,
                has_stickers=False,
                file=big_photo_file_result.obj)

            small_photo = db_model.Photo(
                thumbnail_type=dbe.PhotoSizeThumbnailType.PROFILE_PHOTO_SMALL,
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
                thumbnail_type=dbe.PhotoSizeThumbnailType.PROFILE_PHOTO_BIG,
                width=-1,
                height=-1,
                has_stickers=False,
                file=big_photo_file_result.obj)

            small_photo = db_model.Photo(
                thumbnail_type=dbe.PhotoSizeThumbnailType.PROFILE_PHOTO_SMALL,
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

            change = dbe.DatabaseChangeEnum.NEW if maybe_existing_user == None else dbe.DatabaseChangeEnum.UPDATED

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
