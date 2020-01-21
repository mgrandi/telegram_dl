import enum

# NOTE:
# i am not sure if it matters too much, but i am going to refrain from using
# enum.auto() here because it makes it harder to reference the source code
# to see what enum value goes to what

class LinkStateEnum(enum.Enum):

    LINK_STATE_NONE = 0
    LINK_STATE_IS_CONTACT = 1
    LINK_STATE_KNOWS_PHONE_NUMBER = 2

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

    USER_TYPE_UNKNOWN = 0
    USER_TYPE_REGULAR = 1
    USER_TYPE_DELETED = 2
    USER_TYPE_BOT = 3
