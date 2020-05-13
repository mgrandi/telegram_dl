from __future__ import annotations

import logging
import typing

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

class UserVersion(CustomDeclarativeBase):
    __tablename__ = "user_version"

    # primary key column
    user_version_id = Column(Integer, nullable=False)

    user_id = Column(Integer,
        ForeignKey("user.user_id",
            name="FK-user_version-user_id-user-user_id"),
        nullable=False)

    as_of = Column(ArrowType, nullable=False)

    first_name = Column(Unicode(length=100), nullable=True)
    last_name = Column(Unicode(length=100), nullable=True)
    user_name = Column(Unicode(length=100), nullable=False)

    # from https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#sqlalchemy_utils.types.phone_number.PhoneNumberType:
    #
    # Changes PhoneNumber objects to a string representation on the way in and changes them back to PhoneNumber
    # objects on the way out. If E164 is used as storing format, no country code is needed for parsing the database
    # value to PhoneNumber object.
    phone_number = Column(PhoneNumberType(
        region=constants.PHONE_NUMBER_DEFAULT_REGION,
        max_length=constants.PHONE_NUMBER_MAX_LENGTH), nullable=True)

    profile_photo_set_id= Column(Integer,
        ForeignKey("photo_set.photo_set_id",
            name="FK-user_version-profile_photo_set_id-photo_set-photo_set_id"), nullable=True)

    profile_photo_set = relationship("ProfilePhotoSet", back_populates="user_version")

    is_contact = Column(Boolean, nullable=False)
    is_mutual_contact = Column(Boolean, nullable=False)
    is_verified = Column(Boolean, nullable=False)
    is_support = Column(Boolean, nullable=False)
    restriction_reason = Column(Unicode(length=255))
    is_scam = Column(Boolean, nullable=False)
    have_access = Column(Boolean, nullable=False)

    user_type = Column(ChoiceType(dbme.UserTypeEnum, impl=Unicode(length=50)), nullable=False)

    language_code = Column(Unicode(length=20), nullable=True)

    user = relationship("User", back_populates="versions")

    __table_args__ = (
        PrimaryKeyConstraint("user_version_id", name="PK-user_version-user_version_id"),

        Index("IXUQ-user_version-user_id-as_of", "user_id", "as_of", unique=True),
        Index("IX-user_version-phone_number", "phone_number"),
        Index("IX-user_version-user_type", "user_type"),
    )


class User(CustomDeclarativeBase):

    __tablename__ = "user"

    # primary key column
    user_id = Column(Integer, nullable=False)

    tg_user_id = Column(Integer, nullable=False)

    # has an ascending orderby on 'UserVersion.as_of', so the earliest versions are first,
    # latest are last
    versions = relationship("UserVersion", order_by="asc(UserVersion.as_of)", back_populates="user")

    __table_args__ = (
        PrimaryKeyConstraint("user_id", name="PK-user-user_id"),
        Index("IX-user-tg_user_id", "tg_user_id"),
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
        'polymorphic_identity':  dbme.PhotoSetPolymorphicTableEnum.PHOTO_SET.value,
        'polymorphic_on': polytype
    }


    def get_photos_by_thumnail_type(self, thumbnail_type:dbme.PhotoSizeThumbnailType) -> typing.Sequence[Photo]:
        ''' helper method for getting the Photo object that has the
        specifiedthumbnail_type of

        @param thumbnail_type a dbme.PhotoSizeThumbnailType to match the photos against

        @return a list of Photo objects, or an empty list if nothing matched

        '''

        result_list = []

        for iter_photo in self.photos:
            if iter_photo.thumbnail_type == thumbnail_type:
                result_list.append(iter_photo)

        return result_list


class ProfilePhotoSet(PhotoSet):

    __tablename__ = 'profile_photo_set'

    # our unique identifier, primary key column
    # has to be a FK to `photo_set`'s primary key' because of the polymorphic table
    profile_photo_set_id = Column(Integer,
        ForeignKey("photo_set.photo_set_id",
            name="FK-profile_photo_set-profile_photo_set_id-photo_set-photo_set_id"),
        nullable=False)

    # this is the id of the profile photo within telegram, used to access to the profile photo later
    tg_id = Column(Integer, nullable=False)

    user_version = relationship("UserVersion", back_populates="profile_photo_set")

    # using `uselist` here becuase it is returning a list instead of a single item
    # i believe this is because technically this is a one to many (one photo set -> many photos) but
    # here on `big` and `small`, we want a 1 to 1 relationship
    big = relationship("Photo",
        primaryjoin=f"and_(ProfilePhotoSet.photo_set_id == Photo.photo_set_id, Photo.thumbnail_type == '{dbme.PhotoSizeThumbnailType.PHOTO_BIG.value}' )",
        uselist=False)

    small = relationship("Photo",
        primaryjoin=f"and_(ProfilePhotoSet.photo_set_id == Photo.photo_set_id, Photo.thumbnail_type == '{dbme.PhotoSizeThumbnailType.PHOTO_SMALL.value}' )",
        uselist=False)


    __table_args__ = (
        PrimaryKeyConstraint("profile_photo_set_id", name="PK-profile_photo_set-profile_photo_set_id"),
    )
    __mapper_args__ = {
        'polymorphic_identity': dbme.PhotoSetPolymorphicTableEnum.PROFILE_PHOTO_SET.value,
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

class ChatVersion(CustomDeclarativeBase):
    '''
    represents a 'version' of a chat, with all of the stuff that can change about
    a chat
    '''

    __tablename__ = 'chat_version'

    # primary key column
    chat_version_id = Column(Integer, nullable=False)

    chat_id = Column(Integer,
        ForeignKey("chat.chat_id",
            name="FK-chat_version-chat_id-chat_chat_id"),
        nullable=False)

    as_of = Column(ArrowType, nullable=False)

    title = Column(Unicode, nullable=False)

    photo_set_id = Column(Integer,
        ForeignKey("photo_set.photo_set_id",
            name="FK-chat_version-photo_set_id-photo_set-photo_set_id"),
        nullable=True)

    photo_set = relationship("PhotoSet")

    is_sponsored = Column(Boolean, nullable=False)

    chat = relationship("Chat", back_populates="versions")

    __table_args__ = (
        PrimaryKeyConstraint("chat_version_id",name="PK-chat_version-chat_version_id"),
        Index("IXUQ-chat_version-chat_id-as_of", "chat_id", "as_of", unique=True),
    )


class Chat(CustomDeclarativeBase):

    __tablename__ = 'chat'

    # our unique identifier, primary key column
    chat_id = Column(Integer, nullable=False)

    # the polymorphic descriminator for the joined table inheritance
    polytype = Column(Unicode, nullable=False)

    tg_chat_id = Column(Integer, nullable=False)

    versions = relationship("ChatVersion", order_by="asc(ChatVersion.as_of)", back_populates="chat")

    __table_args__ = (
        PrimaryKeyConstraint("chat_id",name="PK-chat-chat_id"),
        Index("IXUQ-chat-tg_chat_id", "tg_chat_id", unique=True),
    )
    __mapper_args__ = {
        'polymorphic_identity': dbme.ChatPolymorphicTableEnum.CHAT.value,
        'polymorphic_on': polytype
    }

class BasicGroupChat(Chat):
    __tablename__ = 'basic_group_chat'

    # our unique identifier, primary key column
    # has to be a FK to `chat`'s primary key' because of the polymorphic table
    basic_group_chat_id = Column(Integer,
        ForeignKey("chat.chat_id",
            name="FK-basic_group_chat-basic_group_chat_id-chat-chat_id"),
        nullable=False)

    # telegram's ID for this 'basic group'
    # this seems to be the same as the `chat.chat_id` except it is
    # `tg_basic_group_id * -1`
    tg_basic_group_id = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': dbme.ChatPolymorphicTableEnum.BASIC_GROUP_CHAT.value,
    }

    __table_args__ = (
        PrimaryKeyConstraint("basic_group_chat_id",
            name="PK-basic_group_chat-basic_group_chat_id"),
        Index("IXUQ-basic_group_chat-tg_basic_group_id", "tg_basic_group_id", unique=True),
    )

class PrivateChat(Chat):
    __tablename__ = 'private_chat'

    # our unique identifier, primary key column
    # has to be a FK to `chat`'s primary key' because of the polymorphic table
    private_chat_id = Column(Integer,
         ForeignKey("chat.chat_id",
            name="FK-private_chat-private_chat_id-chat-chat_id"),
        nullable=False)

    # the "other" user this private chat is with
    user_id = Column(Integer,
        ForeignKey("user.user_id",
            name="FK-private_chat-user_id-user-user_id"),
        nullable=False)

    user = relationship("User")

    __mapper_args__ = {
            'polymorphic_identity': dbme.ChatPolymorphicTableEnum.PRIVATE_CHAT.value,
    }

    __table_args__ = (
        PrimaryKeyConstraint("private_chat_id",
            name="PK-private_chat-private_chat_id"),
        Index("IXUQ-private_chat-user_id", "user_id", unique=True)

    )

class SuperGroupChat(Chat):
    __tablename__ = 'super_group_chat'

    # our unique identifier, primary key column
    # has to be a FK to `chat`'s primary key' because of the polymorphic table
    super_group_chat_id = Column(Integer,
         ForeignKey("chat.chat_id",
            name="FK-super_group_chat-super_group_chat_id-chat-chat_id"),
        nullable=False)

    # telegram's ID for this 'super group'
    # this seems to be the same as the `chat.chat_id` except it is
    # `(tg_super_group_id  * -1 ) - 10000`
    tg_super_group_id = Column(Integer, nullable=False)

    is_channel = Column(Boolean, nullable=False)

    __mapper_args__ = {
            'polymorphic_identity': dbme.ChatPolymorphicTableEnum.SUPER_GROUP_CHAT.value,
    }

    __table_args__ = (
        PrimaryKeyConstraint("super_group_chat_id",
            name="PK-super_group_chat-super_group_chat_id"),
        Index("IXUQ-super_group_chat-tg_super_group_id", "tg_super_group_id", unique=True),
    )

class SecretChat(Chat):
    __tablename__ = 'secret_chat'

    # our unique identifier, primary key column
    # has to be a FK to `chat`'s primary key' because of the polymorphic table
    secret_chat_id = Column(Integer,
         ForeignKey("chat.chat_id",
            name="FK-secret_chat-secret_chat_id-chat-chat_id"),
        nullable=False)

    tg_secret_chat_id = Column(Integer, nullable=False)

    # the "other" user this secret chat is with
    user_id = Column(Integer,
        ForeignKey("user.user_id",
            name="FK-secret_chat-user_id-user-user_id"),
        nullable=False)

    user = relationship("User")


    __mapper_args__ = {
            'polymorphic_identity': dbme.ChatPolymorphicTableEnum.SECRET_CHAT.value,
    }

    __table_args__ = (
        PrimaryKeyConstraint("secret_chat_id",
            name="PK-secret_chat-secret_chat_id"),
        Index("IXUQ-secret_chat-tg_secret_chat_id", "tg_secret_chat_id", unique=True)
    )


class TextEntity(CustomDeclarativeBase):
    '''
    class that represents the text entities that telegram has parsed out of the
    message

    see `notes/text entity notes.md` for more information


    this is a many to one relationship, where there can be many text entities
    per 1 'message_version` column
    '''

    __tablename__ = 'text_entity'

    # our unique identifier, primary key column
    text_entity_id = Column( Integer, nullable=False)

    message_version_id = Column(
        Integer,
        ForeignKey("message_version.message_version_id",
            name="FK-text_entity-message_version_id-message_version-message_version_id"),
        nullable=False)

    offset = Column(Integer, nullable=False)

    length = Column(Integer, nullable=False)

    text_entity_type = Column(
        ChoiceType(dbme.TextEntityTypeEnum,
            impl=Unicode(length=50)),
        nullable=False)

    #############################
    # SQLAlchemy Relationships
    #############################

    message = relationship("MessageVersionText", back_populates="text_entities")

    #############################
    # Table and Mapper Arguments
    #############################

    __mapper_args__ = {

    }

    __table_args__ = (
       PrimaryKeyConstraint("text_entity_id",
            name="PK-text_entity-text_entity_id"),
       Index("IX-text_entity-message_version_id", "message_version_id", unique=False)
    )



class MessageVersion(CustomDeclarativeBase):
    __tablename__ = 'message_version'

    # our unique identifier, primary key column
    message_version_id = Column(Integer, nullable=False)

    # the polymorphic descriminator for the joined table inheritance
    polytype = Column(Unicode, nullable=False)

    message_id = Column(
        Integer,
        ForeignKey("message.message_id",
            name="FK-message_version-message_id-message-message_id"),
        nullable=False)

    as_of = Column(ArrowType, nullable=False)

    date = Column(ArrowType, nullable=False)

    edit_date = Column(ArrowType, nullable=True)

    # sending_state = False

    # scheduling_state = False

    author_signature = Column(Unicode, nullable=True)

    ttl = Column(Integer, nullable=True)

    #############################
    # SQLAlchemy Relationships
    #############################


    #############################
    # Table and Mapper Arguments
    #############################

    __mapper_args__ = {
        'polymorphic_identity': dbme.MessageVersionPolymorphicTableEnum.BASE.value,
        'polymorphic_on': polytype
    }

    __table_args__ = (
        PrimaryKeyConstraint("message_version_id",
            name="PK-message_version-message_version_id"),
        Index("IX-message_version-as_of", "as_of", unique=False)
    )

class MessageVersionText(MessageVersion):

    __tablename__ = 'message_version_text'

    # our unique identifier, primary key column
    # has to be a FK to `message_version`'s primary key' because of the polymorphic table
    message_version_text_id = Column(
        Integer,
        ForeignKey("message_version.message_version_id",
            name="FK-message_version_text.message_version_text_id-message_version-message_version_id"),
        nullable=True)

    # pretty sure this can't ever be null
    text = Column(Unicode, nullable=False)

    # will be null for now, until i implement
    # storing this in the database
    web_page_id = Column(Integer, nullable=True)

    #############################
    # SQLAlchemy Relationships
    #############################

    # the text entities that go to this message
    text_entities = relationship("TextEntity", back_populates="message")

    #############################
    # Table and Mapper Arguments
    #############################

    __mapper_args__ = {
        'polymorphic_identity': dbme.MessageVersionPolymorphicTableEnum.MESSAGE_TEXT.value,
    }

    __table_args__ = (
        PrimaryKeyConstraint("message_version_text_id",
            name="PK-message_version_text-message_version_text_id"),
    )


class Message(CustomDeclarativeBase):

    __tablename__ = 'message'

    # our unique identifier, primary key column
    message_id = Column(Integer, nullable=False)

    sender_user_id = Column(Integer,
        ForeignKey("user.user_id",
            name="FK-message-sender_user_id-user-user_id"),
        nullable=False)

    chat_id = Column(Integer,
        ForeignKey("chat.chat_id",
            name="FK-message-chat_id-chat-chat_id"),
        nullable=False)

    reply_to_message_id = Column(Integer, nullable=True)

    via_bot_user_id = Column(Integer, nullable=True)

    is_outgoing = Column(Boolean, nullable=False)

    is_channel_post = Column(Boolean, nullable=False)

    can_edit = Column(Boolean, nullable=False)

    can_forward = Column(Boolean, nullable=False)

    can_be_deleted_only_for_self = Column(Boolean, nullable=False)

    can_be_deleted_for_all_users = Column(Boolean, nullable=False)

    restriction_reason = Column(Unicode, nullable=True)

    #############################
    # SQLAlchemy Relationships
    #############################

    #############################
    # Table and Mapper Arguments
    #############################

    __mapper_args__ = {
    }

    __table_args__ = (
        PrimaryKeyConstraint("message_id",
            name="PK-message-message_id"),
        Index("IX-message-sender_user_id", "sender_user_id", unique=False),
        Index("IX-message-chat_id", "chat_id", unique=False),

    )
