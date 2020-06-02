from __future__ import annotations

import logging
import typing

from telegram_dl import db_model
from telegram_dl import db_model_enums as dbme
from telegram_dl import tdlib_generated as tdg
from telegram_dl import utils
from telegram_dl.aides.photo_set_aide import PhotoSetAide
from telegram_dl.aides.phone_number_aide import PhoneNumberAide

import arrow

logger = logging.getLogger(__name__)

class UserAide:

    @staticmethod
    def get_user_by_tg_user_id(
        sqla_session:sqlalchemy.orm.session.Session,
        tg_user_id:int) -> typing.Optional[db_model.User]:
        '''
        queries the database for a db_model.Chat given the tg_chat_id, or
        returns None (see the documentation for `Query.first()` )
        '''

        maybe_existing_user = sqla_session.query(db_model.User) \
            .filter(db_model.User.tg_user_id == tg_user_id) \
            .first()

        return maybe_existing_user

    @staticmethod
    def new_user_from_tdlib_user(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_user:tdg.user) -> db_model.User:
        '''
        creates a new `db_model.User` from the provided `tdlib_generated.user`
        '''


        new_user = db_model.User(tg_user_id=tdlib_user.id)

        new_user_version = UserAide.new_user_version_from_tdlib_user(sqla_session, tdlib_user)

        new_user.versions.append(new_user_version)

        return new_user

    @staticmethod
    def new_user_version_from_tdlib_user(
        sqla_session:sqlalchemy.orm.session.Session,
        tdlib_user:tdg.user) -> db_model.UserVersion:
        '''
        creates a new `db_model.UserVersion` from the provided `tdlib_generated.user`
        '''

        # we insert a string into the database and we get back a
        phone_number_to_insert = ""
        if tdlib_user.phone_number:
            # add the + sign so it parses correctly
            phone_number_to_insert = PhoneNumberAide.fix_phone_number_from_string(tdlib_user.phone_number)

        profile_photo_set_result = PhotoSetAide.get_profile_photo_set_from_tdlib_profile_photo(
            sqla_session, tdlib_user.profile_photo)

        if profile_photo_set_result is None:

            profile_photo_set_result = PhotoSetAide.new_profile_photo_set_from_tdlib_profilephoto(
                sqla_session, tdlib_user.profile_photo)

        new_version = db_model.UserVersion(
            as_of=arrow.utcnow(),
            first_name=tdlib_user.first_name,
            last_name=tdlib_user.last_name,
            user_name=tdlib_user.username,
            phone_number=phone_number_to_insert,
            is_contact=True if tdlib_user.is_contact == 1 else False,
            is_mutual_contact=True if tdlib_user.is_mutual_contact == 1 else False,
            profile_photo_set=profile_photo_set_result if profile_photo_set_result is not None else None,
            is_verified=tdlib_user.is_verified,
            is_support=tdlib_user.is_support,
            restriction_reason=tdlib_user.restriction_reason,
            is_scam=tdlib_user.is_scam,
            have_access=tdlib_user.have_access,
            user_type=dbme.UserTypeEnum.parse_from_tdg_usertype(tdlib_user.type),
            language_code=tdlib_user.language_code)

        return new_version


    @staticmethod
    def compare_dbmodel_and_tdlib_user(
        dbmodel_user:db_model.User,
        tdlib_user:tdg.user) -> bool:
        '''
        method chat compares a `db_model.User` and a
        `tdlib_generated.User` instance
        '''

        if dbmodel_user is None or tdlib_user is None:
            logger.debug("one of the args is None, doing fast comparison")

            fast_result = dbmodel_user == tdlib_user

            logger.debug("fast result: `%s`", fast_result)

            return fast_result

        if len(dbmodel_user.versions) == 0:
            logger.debug("returning False because User exists but has no versions")
            return False

        # get the latest version

        # should be sorted by ascending so the LAST index is the latest

        latest_version = dbmodel_user.versions[-1]


        user_version_comparison = tdlib_user is not None \
            and isinstance(tdlib_user, tdg.user) \
            and dbmodel_user.tg_user_id == tdlib_user.id \
            and latest_version.first_name == tdlib_user.first_name \
            and latest_version.last_name == tdlib_user.last_name \
            and latest_version.user_name == tdlib_user.username \
            and latest_version.is_contact == tdlib_user.is_contact \
            and latest_version.is_mutual_contact ==tdlib_user.is_mutual_contact \
            and latest_version.is_verified == tdlib_user.is_verified \
            and latest_version.is_support == tdlib_user.is_support \
            and latest_version.restriction_reason == tdlib_user.restriction_reason \
            and latest_version.is_scam == tdlib_user.is_scam \
            and latest_version.have_access == tdlib_user.have_access \
            and latest_version.user_type == dbme.UserTypeEnum.parse_from_tdg_usertype(tdlib_user.type) \
            and latest_version.language_code == tdlib_user.language_code

        # check to see if there

        profilephoto_result = PhotoSetAide \
            .compare_dbmodel_profile_photoset_and_tdlib_profilephoto(
                latest_version.profile_photo_set,
                tdlib_user.profile_photo)

        phoneno_result = PhoneNumberAide \
            .compare_phonenumberslite_to_tdlib_phonenumber(latest_version.phone_number, tdlib_user.phone_number)

        final = user_version_comparison and profilephoto_result and phoneno_result

        logger.debug("user result: `%s`, profile photo result: `%s`, phone # result: `%s`",
                user_version_comparison, profilephoto_result, phoneno_result)

        return final