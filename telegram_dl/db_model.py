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
    user_id = Column(Integer, nullable=False)

    as_of = Column(ArrowType, nullable=False)

    # telegram fields
    tg_user_id = Column(Integer, nullable=False)
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

    profile_photo_set_id= Column(Integer,
        ForeignKey("photo_set.photo_set_id",
            name="FK-user-profile_photo_set_id-photo_set-photo_set_id"))

    is_contact = Column(Boolean, nullable=False)
    is_mutual_contact = Column(Boolean, nullable=False)
    is_verified = Column(Boolean, nullable=False)
    is_support = Column(Boolean, nullable=False)
    restriction_reason = Column(Unicode(length=255))
    is_scam = Column(Boolean, nullable=False)
    have_access = Column(Boolean, nullable=False)

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
    file_id = Column(Integer, nullable=False)

    # seems to be local to the user and a very low number, like `27`
    tg_file_id = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    expected_size = Column(Integer, nullable=False)

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
    remote_file_id = Column(Unicode(100), nullable=False)


    __table_args__ = (
        PrimaryKeyConstraint("file_id", name="PK-file-file_id"),
        Index("IXUQ-file-remote_file_id", "remote_file_id", unique=True),
    )

    def equals_tdg(self, other:tdg.file):

        return other is not None \
            and isinstance(other, tdg.file) \
            and self.remote_file_id == other.remote.id



class PhotoSet(CustomDeclarativeBase):
    ''' this table is using joined table inheritance

    see https://docs.sqlalchemy.org/en/13/orm/inheritance.html

    '''

    __tablename__ = 'photo_set'

    # our unique identifier, primary key column
    photo_set_id = Column(Integer, nullable=False)

    # the polymorphic descriminator for the joined table inheritance
    polytype = Column(Unicode(100), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("photo_set_id", name="PK-photo_set-photo_set_id"),
    )
    __mapper_args__ = {
        'polymorphic_identity': constants.POLYMORPHIC_IDENTITY_PHOTOSET_BASE,
        'polymorphic_on': polytype
    }

    def equals_tdg(self, other:tdg.file):
        pass

class ProfilePhotoSet(PhotoSet):

    __tablename__ = 'profile_photo_set'

    # our unique identifier, primary key column
    profile_photo_photo_set_id = Column(Integer,
        ForeignKey("photo_set.photo_set_id", name="FK-profile_photo_set-profile_photo_set_id-photo_set-photo_set_id"),
        nullable=False)

    # this is the id of the profile photo within telegram, used to access to the profile photo later
    tg_id = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("profile_photo_photo_set_id", name="PK-profile_photo_set-profile_photo_photo_set_id"),
    )
    __mapper_args__ = {
        'polymorphic_identity': constants.POLYMORPHIC_IDENTITY_PHOTOSET_PROFILE_PHOTO,
    }

    def equals_tdg(self, other:tdg.file):
        pass

class Photo(CustomDeclarativeBase):

    __tablename__ = 'photo'

    # our unique identifier, primary key column
    profile_photo_photo_set_id = Column(Integer, nullable=False)

    photo_set_id = Column(Integer,
        ForeignKey("photo_set.photo_set_id", name="FK-photo-photo_set_id-photo_set-photo_set_id"),
        nullable=False)

    thumbnail_type = Column(ChoiceType(dbme.PhotoSizeThumbnailType, impl=Unicode()), nullable=False)

    width = Column(Integer, nullable=False)

    height = Column(Integer, nullable=False)

    has_stickers = Column(Boolean, nullable=False)

    file_id = Column(Integer,
        ForeignKey("file.file_id",
            name="FK-photo-file_id-file-file_id"), nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("profile_photo_photo_set_id", name="PK-profile_photo_set-profile_photo_photo_set_id"),
    )

    def equals_tdg(self, other:tdg.file):
        pass
