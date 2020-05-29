from __future__ import annotations

import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
import telegram_dl.db_model_enums as dbme
from telegram_dl.aides.file_aide import FileAide


logger = logging.getLogger(__name__)

class PhotoSetAide:


    @staticmethod
    def new_photo_set_from_tdlib_chatphoto(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_chat_photo:tdg.chatPhoto) -> db_model.PhotoSet:
        '''
        method that returns a new db_model.PhotoSet from a `tdlib_generated.chatPhoto`
        '''

        new_small_photo_file = FileAide.new_file_from_tdlib_file(tdlib_chat_photo.small)
        new_big_photo_file = FileAide.new_file_from_tdlib_file(tdlib_chat_photo.big)

        new_photo_set = db_model.PhotoSet()

        small_photo = db_model.Photo(
            thumbnail_type=dbme.PhotoSizeThumbnailType.PHOTO_SMALL,
            width=-1,
            height=-1,
            has_stickers=False,
            file=new_small_photo_file)

        big_photo = db_model.Photo(
            thumbnail_type=dbme.PhotoSizeThumbnailType.PHOTO_BIG,
            width=-1,
            height=-1,
            has_stickers=False,
            file=new_big_photo_file)

        new_photo_set.photos.append(big_photo)
        new_photo_set.photos.append(small_photo)

        return new_photo_set

    @staticmethod
    def get_photo_set_from_tdlib_chat_photo(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_chat_photo:typing.Optional[tdlib_generated.chatPhoto]) -> typing.Optional[db_model.PhotoSet]:

        # sometimes chats have no photo, handle this
        if tdlib_chat_photo is None:
            return None

        big_photo_file_result = FileAide.get_file_by_tdlib_file(sqla_session, tdlib_chat_photo.big)
        small_photo_file_result = FileAide.get_file_by_tdlib_file(sqla_session, tdlib_chat_photo.small)

        if big_photo_file_result is not None and \
            small_photo_file_result is not None:

            return PhotoSetAide.get_photo_set_from_file(sqla_session, big_photo_file_result)

        else:

            return None




    @staticmethod
    def get_photo_set_from_file(
        sqla_session:sqlalchemy.orm.session.Session,
        file_in_photoset:db_model.File) -> typing.Optional[db_model.PhotoSet]:
        '''
        returns a `db_model.PhotoSet` that has a `db_model.Photo` / `db_model.File`
        that matches the one passed in as an argument, if it exists, or
        returns None (see the documentation for `Query.first()` )

        '''

        existing_photo_set = sqla_session.query(db_model.PhotoSet) \
                .join(db_model.Photo) \
                .filter(db_model.Photo.file_id == file_in_photoset.file_id) \
                .first()

        return existing_photo_set

    @staticmethod
    def compare_dbmodel_photoset_and_tdlib_chatphoto(
        dbmodel_photoset:typing.Optional[db_model.PhotoSet],
        tdlib_chatphoto:typing.Optional[tdg.chatPhoto]) -> bool:
        '''
        Testing to see if a `db_model.Chat`s `db_model.PhotoSet` 'matches'
        tdlib's 'chatPhoto' class

        since we are abstracting a `tdg.chatPhoto` as a `db_model.PhotoSet ,
        its slightly more complicated
        '''

        # a `tdg.chatPhoto` has 2 fields, 'big` (file), `small` (file),
        #
        # a db_model.PhotoSet has a collection of db_model.Photo objects,
        # each with a reference to a db_model.File

        # do fast check for None, some users don't have a profile photo or have removed it
        # since we last checked

        if dbmodel_photoset is None or \
            tdlib_chatphoto is None:

            logger.debug("one of the args is None, doing fast comparison")

            fast_result = dbmodel_photoset == tdlib_chatphoto

            logger.debug("fast result: `%s`", fast_result)

            return fast_result

        logger.debug("comparing `%s` and `%s`", dbmodel_photoset, tdlib_chatphoto)

        # check files
        logger.debug("comparing big file")

        # big_photo_file_args = EqualityArgumentFile(
        #     tdl_file=chat_photo_arg.tdl_photo_set.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_BIG)[0].file,
        #     tdg_file=chat_photo_arg.tdg_chat_photo.big)

        # big_photo_comparison = self.is_equal(big_photo_file_args)

        big_photo_dbmodel_photo_list:typing.Sequence[Photo] = \
            dbmodel_photoset.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_BIG)

        big_photo_dbmodel_photo:typing.Optional[db_model.Photo] = big_photo_dbmodel_photo_list[0] if len(big_photo_dbmodel_photo_list) >= 1 else None
        big_photo_tdlib_file:tdg.file = tdlib_chatphoto.big

        big_photo_comparison = FileAide.compare_dbmodel_file_and_tdlib_file(
            dbmodel_file=big_photo_dbmodel_photo.file,
            tdlib_file=big_photo_tdlib_file)

        logger.debug("comparing small file")

        # small_photo_file_args = EqualityArgumentFile(
        #     tdl_file=chat_photo_arg.tdl_photo_set.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_SMALL)[0].file,
        #     tdg_file=chat_photo_arg.tdg_chat_photo.small)

        # small_photo_comparison = self.is_equal(small_photo_file_args)

        small_photo_dbmodel_photo_list:typing.Sequence[Photo] = \
            dbmodel_photoset.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_SMALL)

        small_photo_dbmodel_photo:typing.Optional[db_model.Photo] = small_photo_dbmodel_photo_list[0] if len(small_photo_dbmodel_photo_list) >= 1 else None
        small_photo_tdlib_file:tdg.file = tdlib_chatphoto.small

        small_photo_comparison = FileAide.compare_dbmodel_file_and_tdlib_file(
            dbmodel_file=small_photo_dbmodel_photo.file,
            tdlib_file=small_photo_tdlib_file)

        logger.debug("big photo comparison: `%s`, small photo comparison: `%s`",
            big_photo_comparison, small_photo_comparison)

        # get final result
        final_result = big_photo_comparison and small_photo_comparison

        logger.debug("final result: `%s`", final_result)

        return final_result
