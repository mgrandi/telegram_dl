
import functools
import logging

from telegram_dl import tdlib_generated
from telegram_dl import db_model

import attr

logger = logging.getLogger(__name__)

insert_or_update_logger = logger.getChild("insert_update")
dbaction_handler_logger = logger.getChild("handler")


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BaseDatabaseAction():

    pass

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InsertDatabaseAction(BaseDatabaseAction):

    object_to_insert:tdlib_generated.RootObject = attr.ib()


class DbActionHandler:

    def __init__(self):

        self.insert_or_update_handler = InsertOrUpdateHandler()

    @functools.singledispatchmethod
    async def handle_database_action(self, obj_to_handle:BaseDatabaseAction, session):

        dbaction_handler_logger.error("handle_database_action: got object: `%s`, UNHANDLED", obj_to_handle)


    @handle_database_action.register
    async def handle_insert_database_action(self, obj_to_handle:InsertDatabaseAction, session):

        dbaction_handler_logger.debug("handle_insert_database_action got object: `%s`", obj_to_handle)

        await self.insert_or_update_handler.handle_insert_or_update(obj_to_handle.object_to_insert, session)



class InsertOrUpdateHandler:

    @functools.singledispatchmethod
    async def handle_insert_or_update(self, obj_to_handle:db_model.CustomDeclarativeBase, session):

        insert_or_update_logger.error("handle_insert_or_update got object: `%s` UNHANDLED", obj_to_handle)


    @handle_insert_or_update.register
    async def file(self, object_to_handle:db_model.File, session):


        # Files should only have one entry per file, we don't do versioning

        # see if it exists
        maybe_existing = session.query(db_model.File).filter(db_model.File.remote_file_id == object_to_handle.remote_file_id).first()

        if not maybe_existing:

            insert_or_update_logger.debug("adding db_model.File object `%s` to session", object_to_handle)
            session.add(object_to_handle)

        else:

            insert_or_update_logger.debug("not adding db_model.File object `%s` because it already exists", object_to_handle)
