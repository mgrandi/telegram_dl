from __future__ import annotations
import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg

logger = logging.getLogger(__name__)

class FileAide:

    @staticmethod
    def new_file_from_tdlib_file(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_file:tdg.file):
        '''
        returns a new `db_model.File` instance created from a
        `tdlib_generated.file` instance
        '''

        new_file = db_model.File(
            tg_file_id=tdlib_file.id,
            size=tdlib_file.size,
            expected_size=tdlib_file.expected_size,
            remote_file_id=tdlib_file.remote.id,
            remote_unique_id=tdlib_file.remote.unique_id if tdlib_file.remote.unique_id else None)

        return new_file

    @staticmethod
    def get_file_by_tdlib_file(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_file:tdg.file) -> typing.Optional[db_model.File]:
        '''
        method that returns a `db_model.File` given the the `tdlib_generated.file`
        if it exists, or returns None (see the documentation for `Query.first()` )
        '''

        return FileAide.get_file_by_remote_file_id(sqla_session, tdlib_file.remote.id)

    @staticmethod
    def get_file_by_remote_file_id(
        sqla_session:sqlalchemy.orm.session.Session,
        remote_file_id:str) -> typing.Optional[db_model.File]:
        '''
        method that returns a `db_model.File` given the file's remote file id,
        if it exists, or returns None (see the documentation for `Query.first()` )

        '''

        maybe_existing = sqla_session.query(db_model.File) \
            .filter(db_model.File.remote_file_id == remote_file_id) \
            .first()

        return maybe_existing


    @staticmethod
    def compare_dbmodel_file_and_tdlib_file(
        dbmodel_file:typing.Optional[db_model.File],
        tdlib_file:typing.Optional[tdg.file]) -> bool:
        '''
        method that compares a `db_model.File` to a `tdlib_generated.file`
        '''

        # here we are just going to check the remote file id and the remote unique id

        if dbmodel_file is None or tdlib_file is None:
            logger.debug("one of the args is None, doing fast comparison")

            fast_result =  dbmodel_file == tdlib_file

            logger.debug("fast result: `%s`", fast_result)

            return fast_result


        logger.debug("comparing `%s` and `%s`", dbmodel_file, tdlib_file)

        result_remote_file_id = dbmodel_file.remote_file_id == tdlib_file.remote.id
        result_remote_unique_id = dbmodel_file.remote_unique_id == tdlib_file.remote.unique_id

        logger.debug("remote id: `%s`, remote unique id: `%s`",
            result_remote_file_id, result_remote_unique_id)

        final_result = result_remote_unique_id and result_remote_file_id

        logger.debug("final result: `%s`", final_result)

        return final_result
