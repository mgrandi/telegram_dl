from __future__ import annotations

import enum

from telegram_dl import tdlib_generated as tdg

# NOTE:
# i am not sure if it matters too much, but i am going to refrain from using
# enum.auto() here because it makes it harder to reference the source code
# to see what enum value goes to what


class DatabaseChangeEnum(enum.Enum):
    NO_CHANGE = 0
    NEW = 1
    UPDATED = 2

class ChatPolymorphicTableEnum(enum.Enum):
    CHAT = "chat"
    BASIC_GROUP_CHAT = "basic_group_chat"
    PRIVATE_CHAT = "private_chat"
    SUPER_GROUP_CHAT = "super_group_chat"
    SECRET_CHAT = "secret_chat"

class PhotoSetPolymorphicTableEnum(enum.Enum):
    '''
    enum representing the available types for the polymorphic identity of the
    `photo_set` table
    '''

    PHOTO_SET = "photoset"
    PROFILE_PHOTO_SET = "profile_photo_photoset"


class MessageVersionPolymorphicTableEnum(enum.Enum):
    '''
    enum representing the available types for the polymorphic identity of the
    `message_version` table
    '''

    # the base shouldn't ever be used, but I need to have it to
    # provide a value for the base `MessageVersion` class
    BASE = "message_version_base"
    MESSAGE_TEXT = "message_text"


class PhotoSizeThumbnailType(enum.Enum):

    def __new__(cls, value, width, height, image_filter):
        '''
        NOTE:
        I want to attach additional data to the enum like it is done in java:
        https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html

        the python 3 docs have an example:
        https://docs.python.org/3/library/enum.html?highlight=enum#when-to-use-new-vs-init

        there is also another (better) example here since we aren't subclassing bytes as well as Enum:
        http://xion.io/post/code/python-enums-are-ok.html#fnref:3

        ##################

        this is a enum class representing the photoSize "thumbnail type"

        see https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html
        and https://core.telegram.org/constructor/photoSize
        '''

        obj = object.__new__(cls)
        obj._value_ = value
        obj.width = width
        obj.height = height
        obj.image_filter = image_filter

        return obj


    S = ("s", 100, 100, "box")
    M = ("m", 320, 320, "box")
    X = ("x", 800, 800, "box")
    Y = ("y", 1280, 1280, "box")
    W = ("w", 2560, 2560, "box")
    A = ("a", 160, 160, "crop")
    B = ("b", 320, 320, "crop")
    C = ("c", 640, 640, "crop")
    D = ("d", 1280, 1280, "crop")

    # so both 'profile photo' and 'chat photo' both have big/small fields,
    # so since they don't have any other size info, we will just have a generic
    # big / small thumbnail type to mark them
    PHOTO_BIG = ("pbig", -1, -1, "photo_big")
    PHOTO_SMALL = ("psmall", -1, -1, "photo_big")




class UserTypeEnum(enum.Enum):

    # TODO: if the user is USER_TYPE_BOT, there are extra fields
    # that telegram sends us, do we need to expose these?
    # class def:
    #
    # @attr.s(auto_attribs=True, frozen=True, kw_only=True)
    # class userTypeBot(UserType):
    #     __tdlib_type__ = "userTypeBot"
    #     can_join_groups:bool = attr.ib()
    #     can_read_all_group_messages:bool = attr.ib()
    #     is_inline:bool = attr.ib()
    #     inline_query_placeholder:str = attr.ib()
    #     need_location:bool = attr.ib()

    USER_TYPE_UNKNOWN = "UT_unknown"
    USER_TYPE_REGULAR = "UT_regular"
    USER_TYPE_DELETED = "UT_deleted"
    USER_TYPE_BOT = "UT_bot"


    @staticmethod
    def parse_from_tdg_usertype(tdg_usertype:UserType) -> UserTypeEnum:

        if isinstance(tdg_usertype, tdg.userTypeUnknown):
            return UserTypeEnum.USER_TYPE_UNKNOWN

        elif isinstance(tdg_usertype, tdg.userTypeRegular):
            return UserTypeEnum.USER_TYPE_REGULAR

        elif isinstance(tdg_usertype, tdg.userTypeDeleted):
            return UserTypeEnum.USER_TYPE_DELETED

        elif isinstance(tdg_usertype, tdg.userTypeBot):
            return UserTypeEnum.USER_TYPE_BOT

        else:
            raise Exception("Unknown user type: `%s`", tdg_usertype)


class TextEntityTypeEnum(enum.Enum):

    TEXT_ENTITY_TYPE_BOLD = "TET_bold"
    TEXT_ENTITY_TYPE_BOT_COMMAND = "TET_bot_command"
    TEXT_ENTITY_TYPE_CASHTAG = "TET_cashtag"
    TEXT_ENTITY_TYPE_CODE = "TET_code"
    TEXT_ENTITY_TYPE_EMAIL_ADDRESS = "TET_email_address"
    TEXT_ENTITY_TYPE_HASHTAG = "TET_hashtag"
    TEXT_ENTITY_TYPE_ITALIC = "TET_italic"
    TEXT_ENTITY_TYPE_MENTION = "TET_mention"
    TEXT_ENTITY_TYPE_MENTION_NAME = "TET_mention_name"
    TEXT_ENTITY_TYPE_PHONE_NUMBER = "TET_phone_number"
    TEXT_ENTITY_TYPE_PRE = "TET_pre"
    TEXT_ENTITY_TYPE_PRE_CODE = "TET_pre_code"
    TEXT_ENTITY_TYPE_STRIKETHROUGH = "TET_strikethrough"
    TEXT_ENTITY_TYPE_TEXT_URL = "TET_text_url"
    TEXT_ENTITY_TYPE_UNDERLINE = "TET_underline"
    TEXT_ENTITY_TYPE_URL = "TET_url"


    @staticmethod
    def parse_from_tdg_text_entity_type(tdg_text_entity_type:TextEntityType) -> TextEntityTypeEnum:

        if isinstance(tdg_text_entity_type, tdg.textEntityTypeBold):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_BOLD

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeBotCommand):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_BOT_COMMAND

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeCashtag):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_CASHTAG

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeCode):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_CODE

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeEmailAddress):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_EMAIL_ADDRESS

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeHashtag):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_HASHTAG

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeItalic):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_ITALIC

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeMention):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_MENTION

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeMentionName):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_MENTION_NAME

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypePhoneNumber):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_PHONE_NUMBER

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypePre):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_PRE

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypePreCode):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_PRE_CODE

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeStrikethrough):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_STRIKETHROUGH

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeTextUrl):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_TEXT_URL

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeUnderline):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_UNDERLINE

        elif isinstance(tdg_text_entity_type, tdg.textEntityTypeUrl):
            return TextEntityTypeEnum.TEXT_ENTITY_TYPE_URL

        else:
            raise Exception("Unknown text entity type: `%s`", tdg_text_entity_type)
