import logging
import typing

from telegram_dl import db_model
from telegram_dl import tdlib_generated as tdg
from telegram_dl.aides import file_aide

logger = logging.getLogger(__name__)

class PhotoSetAide:

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

        big_photo_comparison = file_aide.compare_dbmodel_file_and_tdlib_file(
            dbmodel_file=big_photo_dbmodel_photo.file,
            tdlib_file=big_photo_tdlib_file)

        logger.debug("comparing small file")

        # small_photo_file_args = EqualityArgumentFile(
        #     tdl_file=chat_photo_arg.tdl_photo_set.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_SMALL)[0].file,
        #     tdg_file=chat_photo_arg.tdg_chat_photo.small)

        # small_photo_comparison = self.is_equal(small_photo_file_args)

        small_photo_dbmodel_photo_list:typing.Sequence[Photo] = \
            dbmodel_photoset.get_photos_by_thumnail_type(dbme.PhotoSizeThumbnailType.PHOTO_SMALL)

        small_photo_dbmodel_photo:typing.Optional[db_model.Photo] = small_photo_dbmodel_photo[0] if len(small_photo_dbmodel_photo) >= 1 else None
        small_photo_tdlib_file:tdg.file = tdlib_chatphoto.small

        small_photo_comparison = file_aide.compare_dbmodel_file_and_tdlib_file(
            dbmodel_file=small_photo_dbmodel_photo.file,
            tdlib_file=small_photo_tdlib_file)

        logger.debug("big photo comparison: `%s`, small photo comparison: `%s`",
            big_photo_comparison, small_photo_comparison)

        # get final result
        final_result = big_photo_comparison and small_photo_comparison

        logger.debug("final result: `%s`", final_result)

        return final_result
