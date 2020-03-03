
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

    @functools.singledispatchmethod
    async def handle_database_action(self, obj_to_handle:BaseDatabaseAction, session):

        dbaction_handler_logger.error("handle_database_action: got object: `%s`, UNHANDLED", obj_to_handle)


    @handle_database_action.register
    async def handle_insert_database_action(self, obj_to_handle:InsertDatabaseAction, session):

        dbaction_handler_logger.debug("handle_insert_database_action got object: `%s`", obj_to_handle)


        session.add(obj_to_handle.object_to_insert)



class InsertOrUpdateHandler:

    @functools.singledispatchmethod
    async def handle_insert_or_update(self, obj_to_handle:db_model.CustomDeclarativeBase, session):

        insert_or_update_logger.error("handle_insert_or_update got object: `%s` UNHANDLED", obj_to_handle)


    # @handle_insert_or_update.register
    # async def handle_insert_or_update_user(self, object_to_handle, session):
    #     pass