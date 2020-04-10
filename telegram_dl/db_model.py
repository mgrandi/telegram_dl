import logging

from sqlalchemy import Column, Index, Integer, Unicode, Boolean, ForeignKey, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

from sqlalchemy_utils import PhoneNumberType, ChoiceType, ArrowType

import phonenumbers

import telegram_dl.db_model_enums as dbme
import telegram_dl.tdlib_generated as tdg
from telegram_dl import utils
from telegram_dl import constants

CustomDeclarativeBase = declarative_base(cls=RepresentableBase, name="CustomDeclarativeBase")

logger = logging.getLogger(__name__)

class User(CustomDeclarativeBase):

    __tablename__ = "user"

    # primary key column
    user_id = Column(Integer)

    as_of = Column(ArrowType)

    # telegram fields
    tg_user_id = Column(Integer)
    first_name = Column(Unicode(length=100))
    last_name = Column(Unicode(length=100))
    user_name = Column(Unicode(length=100))

    # from https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#sqlalchemy_utils.types.phone_number.PhoneNumberType:
    #
    # Changes PhoneNumber objects to a string representation on the way in and changes them back to PhoneNumber
    # objects on the way out. If E164 is used as storing format, no country code is needed for parsing the database
    # value to PhoneNumber object.
    phone_number = Column(PhoneNumberType(
        region=constants.PHONE_NUMBER_DEFAULT_REGION,
        max_length=constants.PHONE_NUMBER_MAX_LENGTH))

    # i don't really care about the status so i won't store it, or have a UserStatus type really
    # status = Column()

    profile_photo_id = Column(Unicode(100),
        ForeignKey("profile_photo.profile_photo_id",
            name="FK-user-profile_photo_id-profile_photo-profile_photo_id"))

    is_contact = Column(Boolean)
    is_mutual_contact = Column(Boolean)
    is_verified = Column(Boolean)
    is_support = Column(Boolean)
    restriction_reason = Column(Unicode(length=255))
    is_scam = Column(Boolean)
    have_access = Column(Boolean)

    user_type = Column(ChoiceType(dbme.UserTypeEnum, impl=Integer()))

    language_code = Column(Unicode(length=20))


    profile_photo = relationship("ProfilePhoto")

    __table_args__ = (
        PrimaryKeyConstraint("user_id", name="PK-user-user_id"),
        Index("IX-user-tg_user_id", "tg_user_id"),
        Index("IXUQ-user-tg_user_id-as_of", "tg_user_id", "as_of", unique=True),
        Index("IX-user-phone_number", "phone_number"),
        Index("IX-user-user_type", "user_type"),
    )


    def equals_tdg(self, other:tdg.user):
        ''' basically overloading __eq__ because sqlalchemy takes over that to
        test by identity for its ORM stuff
        '''

        result = other is not None \
            and isinstance(other, tdg.user) \
            and self.tg_user_id == other.id \
            and self.first_name == other.first_name \
            and self.last_name == other.last_name \
            and self.user_name == other.username \
            and self.is_contact == other.is_contact \
            and self.is_mutual_contact == other.is_mutual_contact \
            and self.is_verified == other.is_verified \
            and self.is_support == other.is_support \
            and self.restriction_reason == other.restriction_reason \
            and self.is_scam == other.is_scam \
            and self.have_access == other.have_access \
            and self.user_type == dbme.UserTypeEnum.parse_from_tdg_usertype(other.type) \
            and self.language_code == other.language_code

        profilephoto_result = False

        # haandle where the user might not have a profile photo
        if self.profile_photo is None:
            profilephoto_result = self.profile_photo == other.profile_photo
        else:
            profilephoto_result = self.profile_photo.equals_tdg(other.profile_photo)

        # handle where we get a str from telegram but a Phonenumber object from the database
        # or the user has no phone number at all
        phoneno_result = False

        if not self.phone_number:

            if not other.phone_number:
                # both phone numbers are empty, just mark as unchanged right
                phoneno_result = True
            else:
                # old phone number doesn't exist but the new one does exist, mark as different
                phoneno_result = False
        else:
            if not other.phone_number:
                # old phone exists but new one doesn't, mark as different
                phoneno_result = False
            else:
                # both old and new phone numbers exist, compare
                phoneno_result = self.phone_number == utils.parse_phone_number_from_str(utils.fix_phone_number(other.phone_number))


        final = result and profilephoto_result and phoneno_result

        if not final:
            logger.debug("equals_tdg: user result: `%s`, profile photo result: `%s`, phone # result: `%s`",
                result, profilephoto_result, phoneno_result)

        return final



class File(CustomDeclarativeBase):

    __tablename__ = "file"

    # this is combining `file`, `localFile` and `remoteFile`


    # our unique identifier, primary key column
    file_id = Column(Integer)

    # seems to be local to the user and a very low number, like `27`
    tg_file_id = Column(Integer)
    size = Column(Integer)
    expected_size = Column(Integer)

    ##########################
    # `localFile` fields
    ##########################

    # i don't think i really need anything from this object?

    ##########################
    # `remoteFile` fields
    ##########################

    # seems to be the unique identifier across all of telegram for the file. Example:
    # `AQADAQADRbYxG4UzzgIACFG4CjAABAIAA4UzzgIABJJVDmJhXyVcVUQAAhYE`
    # only seems to be 60 characters in practice, but lets be safe
    remote_file_id = Column(Unicode(100))


    __table_args__ = (
        PrimaryKeyConstraint("file_id", name="PK-file-file_id"),
        Index("IXUQ-file-remote_file_id", "remote_file_id", unique=True),
    )

    def equals_tdg(self, other:tdg.file):

        return other is not None \
            and isinstance(other, tdg.file) \
            and self.remote_file_id == other.remote.id


class ProfilePhoto(CustomDeclarativeBase):

    __tablename__ = "profile_photo"

    # primary key column
    profile_photo_id = Column(Integer)

    # unlike User.tg_file_id, this isn't a super low number, not sure if it it can change
    # if the tdlib working copy gets regenerated?
    tg_profile_photo_id = Column(Integer)

    big_id = Column(Integer,
        ForeignKey("file.file_id",
            name="FK-profile_photo-big_id-file-file_id"))
    small_id = Column(Integer,
        ForeignKey("file.file_id",
            name="FK-profile_photo-small_id-file-file_id"))

    # see https://docs.sqlalchemy.org/en/14/orm/join_conditions.html#handling-multiple-join-paths
    big = relationship("File", foreign_keys=[big_id])
    small = relationship("File", foreign_keys=[small_id])

    __table_args__ = (
        PrimaryKeyConstraint("profile_photo_id", name="PK-profile_photo-profile_photo_id"),
    )


    def equals_tdg(self, other:tdg.profilePhoto):

        return other is not None \
            and isinstance(other, tdg.profilePhoto) \
            and self.big.equals_tdg(other.big) \
            and self.small.equals_tdg(other.small)



# class TEMPLATE(CustomDeclarativeBase):

#         __tablename__ = "SOMETHING"
#         __table_args__ = ( )