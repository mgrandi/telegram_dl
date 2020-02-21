

from telegram_dl import tdlib_generated

import attr

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class BaseDatabaseAction():

    pass

@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class InsertDatabaseAction(BaseDatabaseAction):

    object_to_insert:tdlib_generated.RootObject = attr.ib()



