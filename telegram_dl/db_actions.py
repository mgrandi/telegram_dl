
import functools
import logging
import typing

from telegram_dl import tdlib_generated
from telegram_dl import db_model
from telegram_dl import db_model_enums as dbe

import attr
import arrow
import phonenumbers
from sqlalchemy.orm.session import Session

logger = logging.getLogger(__name__)

insert_or_update_logger = logger.getChild("insert_update")
dbaction_handler_logger = logger.getChild("handler")


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
    async def handle_insert_or_update(self, obj_to_handle:tdlib_generated.RootObject, params:InsertOrUpdateParameter) -> typing.Optional[db_model.CustomDeclarativeBase]:

        insert_or_update_logger.error("handle_insert_or_update got object: `%s` UNHANDLED", obj_to_handle)

        return None

    @handle_insert_or_update.register
    async def file(self, object_to_handle:tdlib_generated.file, params:InsertOrUpdateParameter) -> typing.Optional[db_model.CustomDeclarativeBase]:


        # Files should only have one entry per file, we don't do versioning

        session = params.session

        # # see if it exists
        maybe_existing = session.query(db_model.File).filter(db_model.File.remote_file_id == object_to_handle.remote.id).first()

        if not maybe_existing:

            new_file = db_model.File(tg_file_id=object_to_handle.id,
                size=object_to_handle.size,
                expected_size=object_to_handle.expected_size,
                remote_file_id=object_to_handle.remote.id)

            insert_or_update_logger.debug("file: adding db_model.File object `%s` to session", new_file)
            session.add(new_file)

            return new_file

        else:

            insert_or_update_logger.debug("file: not adding db_model.File object `%s` because it already exists", object_to_handle)

            return None

    @handle_insert_or_update.register
    async def profile_photo(self, incoming_profile_photo:tdlib_generated.profilePhoto, params:InsertOrUpdateParameter) -> typing.Optional[db_model.CustomDeclarativeBase]:

        session = params.session

        # profile photos should be unique

        # see if it exists
        maybe_existing = session.query(db_model.ProfilePhoto).filter(db_model.ProfilePhoto.tg_profile_photo_id == incoming_profile_photo.id).first()


        if not maybe_existing:


            big_photo_file = await self.handle_insert_or_update(incoming_profile_photo.big, params)
            small_photo_file = await self.handle_insert_or_update(incoming_profile_photo.small, params)

            new_profile_photo = db_model.ProfilePhoto(
                tg_profile_photo_id=incoming_profile_photo.id,
                big=big_photo_file,
                small=small_photo_file)

            insert_or_update_logger.debug("profile_photo: adding db_model.ProfilePhoto object `%s` to session", new_profile_photo)
            session.add(new_profile_photo)

            return new_profile_photo

        else:

            insert_or_update_logger.debug("profile_photo: not adding db_model.ProfilePhoto object `%s` because it already exists", incoming_profile_photo)

            return None


    @handle_insert_or_update.register
    async def user(self, incoming_user:tdlib_generated.user, params:InsertOrUpdateParameter) -> typing.Optional[db_model.CustomDeclarativeBase]:


        session = params.session


        # users are versioned

        # see if this user version exists
        # TODO ACTUALLY IMPLEMENT VERSIONING
        maybe_existing = session.query(db_model.User).filter(db_model.User.tg_user_id == incoming_user.id).first()


        # add the + sign so it parses correctly
        phone_number = incoming_user.phone_number
        if not phone_number.startswith("+"):
            phone_number = f"+{phone_number}"

        if not maybe_existing:

            profile_photo = await self.handle_insert_or_update(incoming_user.profile_photo, params)

            new_user = db_model.User(
                as_of=arrow.utcnow(),
                tg_user_id=incoming_user.id,
                first_name=incoming_user.first_name,
                last_name=incoming_user.last_name,
                user_name=incoming_user.username,
                phone_number=incoming_user.phone_number,
                outgoing_link=dbe.LinkStateEnum.parse_from_tdg_linkstate(incoming_user.outgoing_link),
                incoming_link=dbe.LinkStateEnum.parse_from_tdg_linkstate(incoming_user.incoming_link),
                profile_photo=profile_photo,
                is_verified=incoming_user.is_verified,
                is_support=incoming_user.is_support,
                restriction_reason=incoming_user.restriction_reason,
                is_scam=incoming_user.is_scam,
                have_access=incoming_user.have_access,
                user_type=dbe.UserTypeEnum.parse_from_tdg_usertype(incoming_user.type),
                language_code=incoming_user.language_code)


            insert_or_update_logger.debug("user: adding db_model.User object `%s` to session", new_user)

            session.add(new_user)
            return new_user

        else:

            insert_or_update_logger.debug("user: not adding db_model.User object `%s` because it already exists", incoming_user)
            return None