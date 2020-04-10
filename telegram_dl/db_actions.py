
import functools
import logging
import typing

from telegram_dl import tdlib_generated
from telegram_dl import db_model
from telegram_dl import db_model_enums as dbe
from telegram_dl import utils

import attr
import arrow
import phonenumbers
from sqlalchemy.orm.session import Session
from sqlalchemy import desc

logger = logging.getLogger(__name__)

insert_or_update_logger = logger.getChild("insert_update")
dbaction_handler_logger = logger.getChild("handler")


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

    @functools.singledispatchmethod
    async def handle_insert_or_update(self, obj_to_handle:None, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        # noop
        return

    @handle_insert_or_update.register
    async def file(self, object_to_handle:tdlib_generated.file, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        # Files should only have one entry per file, we don't do versioning

        session = params.session

        # # see if it exists
        maybe_existing = session.query(db_model.File).filter(db_model.File.remote_file_id == object_to_handle.remote.id).first()

        is_equal = maybe_existing.equals_tdg(object_to_handle) if maybe_existing else False

        # either doesn't exist or it does exist but has changed
        if not maybe_existing or not is_equal:

            new_file = db_model.File(tg_file_id=object_to_handle.id,
                size=object_to_handle.size,
                expected_size=object_to_handle.expected_size,
                remote_file_id=object_to_handle.remote.id)

            change = dbe.DatabaseChangeEnum.NEW if maybe_existing == None else dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.info("file: adding db_model.File object `%s` to session with change: `%s`", new_file, change)

            session.add(new_file)

            return InsertOrUpdateResult(obj=new_file, change=change)

        else:

            insert_or_update_logger.debug("file: not adding db_model.File object `%s` because it already exists and hasn't changed",
                 object_to_handle)

            return InsertOrUpdateResult(obj=maybe_existing, change=dbe.DatabaseChangeEnum.NO_CHANGE)

    @handle_insert_or_update.register
    async def profile_photo(self, incoming_profile_photo:tdlib_generated.profilePhoto, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:

        session = params.session

        # profile photos should be unique

        # see if it exists
        maybe_existing = session.query(db_model.ProfilePhoto).filter(db_model.ProfilePhoto.tg_profile_photo_id == incoming_profile_photo.id).first()

        is_equal = maybe_existing.equals_tdg(incoming_profile_photo) if maybe_existing else False

        if not maybe_existing or not is_equal:

            big_photo_file = await self.handle_insert_or_update(incoming_profile_photo.big, params)
            small_photo_file = await self.handle_insert_or_update(incoming_profile_photo.small, params)

            new_profile_photo = db_model.ProfilePhoto(
                tg_profile_photo_id=incoming_profile_photo.id,
                big=big_photo_file.obj,
                small=small_photo_file.obj)

            change = dbe.DatabaseChangeEnum.NEW if maybe_existing == None else dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.info("profile_photo: adding db_model.ProfilePhoto object `%s` to session with change: `%s`",
                new_profile_photo, change)

            session.add(new_profile_photo)

            return InsertOrUpdateResult(obj=new_profile_photo, change=change)

        else:

            insert_or_update_logger.debug("profile_photo: not adding db_model.ProfilePhoto object `%s` because it already exists or hasn't changed",
                incoming_profile_photo)

            return InsertOrUpdateResult(obj=maybe_existing, change=dbe.DatabaseChangeEnum.NO_CHANGE)


    @handle_insert_or_update.register
    async def user(self, incoming_user:tdlib_generated.user, params:InsertOrUpdateParameter) -> InsertOrUpdateResult:


        session = params.session

        # users are versioned

        # see if this user version exists
        # TODO ACTUALLY IMPLEMENT VERSIONING
        maybe_existing = session.query(db_model.User) \
            .filter(db_model.User.tg_user_id == incoming_user.id) \
            .order_by(desc(db_model.User.as_of)) \
            .first()

        is_equal = maybe_existing.equals_tdg(incoming_user) if maybe_existing else False

        if not maybe_existing or not is_equal:

            # add the + sign so it parses correctly
            fixed_phone_number = utils.fix_phone_number(incoming_user.phone_number) if incoming_user.phone_number else ""

            profile_photo = await self.handle_insert_or_update(incoming_user.profile_photo, params)

            new_user = db_model.User(
                as_of=arrow.utcnow(),
                tg_user_id=incoming_user.id,
                first_name=incoming_user.first_name,
                last_name=incoming_user.last_name,
                user_name=incoming_user.username,
                phone_number=fixed_phone_number,
                is_contact=True if incoming_user.is_contact == 1 else False,
                is_mutual_contact=True if incoming_user.is_mutual_contact == 1 else False,
                profile_photo=profile_photo.obj if profile_photo is not None else None,
                is_verified=incoming_user.is_verified,
                is_support=incoming_user.is_support,
                restriction_reason=incoming_user.restriction_reason,
                is_scam=incoming_user.is_scam,
                have_access=incoming_user.have_access,
                user_type=dbe.UserTypeEnum.parse_from_tdg_usertype(incoming_user.type),
                language_code=incoming_user.language_code)


            change = dbe.DatabaseChangeEnum.NEW if maybe_existing == None else dbe.DatabaseChangeEnum.UPDATED

            insert_or_update_logger.info("user: adding db_model.User object `%s` to session with change: `%s`", new_user, change)
            session.add(new_user)

            return InsertOrUpdateResult(obj=new_user, change=change)

        else:

            # see if the old version matches the new one

            insert_or_update_logger.debug("user: not adding db_model.User object `%s` because it already exists or hasn't changed",
                incoming_user)
            return InsertOrUpdateResult(obj=maybe_existing, change=dbe.DatabaseChangeEnum.NO_CHANGE)
