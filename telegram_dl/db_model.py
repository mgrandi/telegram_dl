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

    profile_photo_set = relationship("ProfilePhotoSet", back_populates="user")

    is_contact = Column(Boolean, nullable=False)
    is_mutual_contact = Column(Boolean, nullable=False)
    is_verified = Column(Boolean, nullable=False)
    is_support = Column(Boolean, nullable=False)
    restriction_reason = Column(Unicode(length=255))
    is_scam = Column(Boolean, nullable=False)
    have_access = Column(Boolean, nullable=False)

    user_type = Column(ChoiceType(dbme.UserTypeEnum, impl=Integer()))

    language_code = Column(Unicode(length=20))

    __table_args__ = (
        PrimaryKeyConstraint("user_id", name="PK-user-user_id"),
        Index("IX-user-tg_user_id", "tg_user_id"),
        Index("IXUQ-user-tg_user_id-as_of", "tg_user_id", "as_of", unique=True),
        Index("IX-user-phone_number", "phone_number"),
        Index("IX-user-user_type", "user_type"),
    )


class File(CustomDeclarativeBase):

    __tablename__ = "file"

    # this is combining `file`, `localFile` and `remoteFile`


    # our unique identifier, primary key column
    file_id = Column(Integer, nullable=False)

    # this is corresponding to `file.id`
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
    #
    # from the docs:
    #
    # Remote file identifier; may be empty. Can be used across application restarts
    # or even from other devices for the current user. Uniquely identifies a file,
    # but a file can have a lot of different valid identifiers. If the ID starts with
    # "http://" or "https://", it represents the HTTP URL of the file. TDLib is
    # currently unable to download files if only their URL is known. If downloadFile
    # is called on such a file or if it is sent to a secret chat, TDLib starts a file
    # generation process by sending updateFileGenerationStart to the client with
    # the HTTP URL in the original_path and "#url#" as the conversion string.
    # Clients should generate the file by downloading it to the specified location.
    remote_file_id = Column(Unicode(), nullable=False)

    # from the docs:
    #
    # Unique file identifier; may be empty if unknown. The unique file identifier
    # which is the same for the same file even for different users and is persistent over time.
    remote_unique_id = Column(Unicode(), nullable=True)


    __table_args__ = (
        PrimaryKeyConstraint("file_id", name="PK-file-file_id"),
        Index("IXUQ-file-remote_file_id", "remote_file_id", unique=True),
    )


class PhotoSet(CustomDeclarativeBase):
    ''' this table is using joined table inheritance

    see https://docs.sqlalchemy.org/en/13/orm/inheritance.html

    '''

    __tablename__ = 'photo_set'

    # our unique identifier, primary key column
    photo_set_id = Column(Integer, nullable=False)

    # the polymorphic descriminator for the joined table inheritance
    polytype = Column(Unicode(100), nullable=False)

    photos = relationship("Photo", back_populates="photo_set")

    __table_args__ = (
        PrimaryKeyConstraint("photo_set_id", name="PK-photo_set-photo_set_id"),
    )
    __mapper_args__ = {
        'polymorphic_identity': constants.POLYMORPHIC_IDENTITY_PHOTOSET_BASE,
        'polymorphic_on': polytype
    }


class ProfilePhotoSet(PhotoSet):

    __tablename__ = 'profile_photo_set'

    # our unique identifier, primary key column
    profile_photo_set_id = Column(Integer,
        ForeignKey("photo_set.photo_set_id", name="FK-profile_photo_set-profile_photo_set_id-photo_set-photo_set_id"),
        nullable=False)

    # this is the id of the profile photo within telegram, used to access to the profile photo later
    tg_id = Column(Integer, nullable=False)

    user = relationship("User", back_populates="profile_photo_set")

    # using `uselist` here becuase it is returning a list instead of a single item
    # i believe this is because technically this is a one to many (one photo set -> many photos) but
    # here on `big` and `small`, we want a 1 to 1 relationship
    big = relationship("Photo",
        primaryjoin=f"and_(ProfilePhotoSet.photo_set_id == Photo.photo_set_id, Photo.thumbnail_type == '{dbme.PhotoSizeThumbnailType.PROFILE_PHOTO_BIG.value}' )",
        uselist=False)

    small = relationship("Photo",
        primaryjoin=f"and_(ProfilePhotoSet.photo_set_id == Photo.photo_set_id, Photo.thumbnail_type == '{dbme.PhotoSizeThumbnailType.PROFILE_PHOTO_SMALL.value}' )",
        uselist=False)


    __table_args__ = (
        PrimaryKeyConstraint("profile_photo_set_id", name="PK-profile_photo_set-profile_photo_set_id"),
    )
    __mapper_args__ = {
        'polymorphic_identity': constants.POLYMORPHIC_IDENTITY_PHOTOSET_PROFILE_PHOTO,
    }



class Photo(CustomDeclarativeBase):

    __tablename__ = 'photo'

    # our unique identifier, primary key column
    photo_id = Column(Integer, nullable=False)

    photo_set_id = Column(Integer,
        ForeignKey("photo_set.photo_set_id", name="FK-photo-photo_set_id-photo_set-photo_set_id"),
        nullable=False)

    thumbnail_type = Column(ChoiceType(dbme.PhotoSizeThumbnailType, impl=Unicode(10)), nullable=False)

    width = Column(Integer, nullable=False)

    height = Column(Integer, nullable=False)

    has_stickers = Column(Boolean, nullable=False)

    file_id = Column(Integer,
        ForeignKey("file.file_id",
            name="FK-photo-file_id-file-file_id"), nullable=False)

    photo_set = relationship("PhotoSet", back_populates="photos")
    file = relationship("File")

    __table_args__ = (
        PrimaryKeyConstraint("photo_id", name="PK-photo-photo_id"),
        Index("IXUQ-photo-file_id", "file_id", unique=True),
        Index("IX-photo-photo_set_id", "photo_set_id")
    )

