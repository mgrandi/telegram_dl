import typing
import decimal
import json

import attr


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_RootObject:
    __tdlib_type__ = "RootObject"
    _extra:str = attr.ib(default="")
    def as_tdlib_json(self) -> str:
        asdict_result = attr.asdict(self, filter=attr.filters.exclude(attr.fields(RootObject)._extra))
        asdict_result["@type"] = self.__tdlib_type__
        if self._extra:
            asdict_result["@extra"] = self._extra
        return json.dumps(asdict_result)


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_AccountTtl(RootObject):
    __tdlib_type__ = "AccountTtl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Address(RootObject):
    __tdlib_type__ = "Address"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Animation(RootObject):
    __tdlib_type__ = "Animation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Animations(RootObject):
    __tdlib_type__ = "Animations"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Audio(RootObject):
    __tdlib_type__ = "Audio"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_AuthenticationCodeInfo(RootObject):
    __tdlib_type__ = "AuthenticationCodeInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_AuthenticationCodeType(RootObject):
    __tdlib_type__ = "AuthenticationCodeType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_AuthorizationState(RootObject):
    __tdlib_type__ = "AuthorizationState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_AutoDownloadSettings(RootObject):
    __tdlib_type__ = "AutoDownloadSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_AutoDownloadSettingsPresets(RootObject):
    __tdlib_type__ = "AutoDownloadSettingsPresets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Background(RootObject):
    __tdlib_type__ = "Background"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_BackgroundType(RootObject):
    __tdlib_type__ = "BackgroundType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Backgrounds(RootObject):
    __tdlib_type__ = "Backgrounds"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_BasicGroup(RootObject):
    __tdlib_type__ = "BasicGroup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_BasicGroupFullInfo(RootObject):
    __tdlib_type__ = "BasicGroupFullInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_BotCommand(RootObject):
    __tdlib_type__ = "BotCommand"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_BotInfo(RootObject):
    __tdlib_type__ = "BotInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Call(RootObject):
    __tdlib_type__ = "Call"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallConnection(RootObject):
    __tdlib_type__ = "CallConnection"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallDiscardReason(RootObject):
    __tdlib_type__ = "CallDiscardReason"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallId(RootObject):
    __tdlib_type__ = "CallId"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallProblem(RootObject):
    __tdlib_type__ = "CallProblem"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallProtocol(RootObject):
    __tdlib_type__ = "CallProtocol"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallState(RootObject):
    __tdlib_type__ = "CallState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallbackQueryAnswer(RootObject):
    __tdlib_type__ = "CallbackQueryAnswer"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CallbackQueryPayload(RootObject):
    __tdlib_type__ = "CallbackQueryPayload"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Chat(RootObject):
    __tdlib_type__ = "Chat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatAction(RootObject):
    __tdlib_type__ = "ChatAction"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatEvent(RootObject):
    __tdlib_type__ = "ChatEvent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatEventAction(RootObject):
    __tdlib_type__ = "ChatEventAction"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatEventLogFilters(RootObject):
    __tdlib_type__ = "ChatEventLogFilters"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatEvents(RootObject):
    __tdlib_type__ = "ChatEvents"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatInviteLink(RootObject):
    __tdlib_type__ = "ChatInviteLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatInviteLinkInfo(RootObject):
    __tdlib_type__ = "ChatInviteLinkInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatMember(RootObject):
    __tdlib_type__ = "ChatMember"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatMemberStatus(RootObject):
    __tdlib_type__ = "ChatMemberStatus"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatMembers(RootObject):
    __tdlib_type__ = "ChatMembers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatMembersFilter(RootObject):
    __tdlib_type__ = "ChatMembersFilter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatNotificationSettings(RootObject):
    __tdlib_type__ = "ChatNotificationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatPermissions(RootObject):
    __tdlib_type__ = "ChatPermissions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatPhoto(RootObject):
    __tdlib_type__ = "ChatPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatReportReason(RootObject):
    __tdlib_type__ = "ChatReportReason"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatReportSpamState(RootObject):
    __tdlib_type__ = "ChatReportSpamState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ChatType(RootObject):
    __tdlib_type__ = "ChatType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Chats(RootObject):
    __tdlib_type__ = "Chats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CheckChatUsernameResult(RootObject):
    __tdlib_type__ = "CheckChatUsernameResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ConnectedWebsite(RootObject):
    __tdlib_type__ = "ConnectedWebsite"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ConnectedWebsites(RootObject):
    __tdlib_type__ = "ConnectedWebsites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ConnectionState(RootObject):
    __tdlib_type__ = "ConnectionState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Contact(RootObject):
    __tdlib_type__ = "Contact"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Count(RootObject):
    __tdlib_type__ = "Count"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_CustomRequestResult(RootObject):
    __tdlib_type__ = "CustomRequestResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_DatabaseStatistics(RootObject):
    __tdlib_type__ = "DatabaseStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Date(RootObject):
    __tdlib_type__ = "Date"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_DatedFile(RootObject):
    __tdlib_type__ = "DatedFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_DeepLinkInfo(RootObject):
    __tdlib_type__ = "DeepLinkInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_DeviceToken(RootObject):
    __tdlib_type__ = "DeviceToken"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Document(RootObject):
    __tdlib_type__ = "Document"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_DraftMessage(RootObject):
    __tdlib_type__ = "DraftMessage"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_EmailAddressAuthenticationCodeInfo(RootObject):
    __tdlib_type__ = "EmailAddressAuthenticationCodeInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Emojis(RootObject):
    __tdlib_type__ = "Emojis"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_EncryptedCredentials(RootObject):
    __tdlib_type__ = "EncryptedCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_EncryptedPassportElement(RootObject):
    __tdlib_type__ = "EncryptedPassportElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Error(RootObject):
    __tdlib_type__ = "Error"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_File(RootObject):
    __tdlib_type__ = "File"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_FilePart(RootObject):
    __tdlib_type__ = "FilePart"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_FileType(RootObject):
    __tdlib_type__ = "FileType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_FormattedText(RootObject):
    __tdlib_type__ = "FormattedText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_FoundMessages(RootObject):
    __tdlib_type__ = "FoundMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Game(RootObject):
    __tdlib_type__ = "Game"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_GameHighScore(RootObject):
    __tdlib_type__ = "GameHighScore"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_GameHighScores(RootObject):
    __tdlib_type__ = "GameHighScores"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Hashtags(RootObject):
    __tdlib_type__ = "Hashtags"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_HttpUrl(RootObject):
    __tdlib_type__ = "HttpUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_IdentityDocument(RootObject):
    __tdlib_type__ = "IdentityDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ImportedContacts(RootObject):
    __tdlib_type__ = "ImportedContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InlineKeyboardButton(RootObject):
    __tdlib_type__ = "InlineKeyboardButton"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InlineKeyboardButtonType(RootObject):
    __tdlib_type__ = "InlineKeyboardButtonType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InlineQueryResult(RootObject):
    __tdlib_type__ = "InlineQueryResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InlineQueryResults(RootObject):
    __tdlib_type__ = "InlineQueryResults"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputBackground(RootObject):
    __tdlib_type__ = "InputBackground"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputCredentials(RootObject):
    __tdlib_type__ = "InputCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputFile(RootObject):
    __tdlib_type__ = "InputFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputIdentityDocument(RootObject):
    __tdlib_type__ = "InputIdentityDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputInlineQueryResult(RootObject):
    __tdlib_type__ = "InputInlineQueryResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputMessageContent(RootObject):
    __tdlib_type__ = "InputMessageContent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputPassportElement(RootObject):
    __tdlib_type__ = "InputPassportElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputPassportElementError(RootObject):
    __tdlib_type__ = "InputPassportElementError"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputPassportElementErrorSource(RootObject):
    __tdlib_type__ = "InputPassportElementErrorSource"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputPersonalDocument(RootObject):
    __tdlib_type__ = "InputPersonalDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputSticker(RootObject):
    __tdlib_type__ = "InputSticker"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_InputThumbnail(RootObject):
    __tdlib_type__ = "InputThumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Invoice(RootObject):
    __tdlib_type__ = "Invoice"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_JsonObjectMember(RootObject):
    __tdlib_type__ = "JsonObjectMember"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_JsonValue(RootObject):
    __tdlib_type__ = "JsonValue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_KeyboardButton(RootObject):
    __tdlib_type__ = "KeyboardButton"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_KeyboardButtonType(RootObject):
    __tdlib_type__ = "KeyboardButtonType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LabeledPricePart(RootObject):
    __tdlib_type__ = "LabeledPricePart"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LanguagePackInfo(RootObject):
    __tdlib_type__ = "LanguagePackInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LanguagePackString(RootObject):
    __tdlib_type__ = "LanguagePackString"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LanguagePackStringValue(RootObject):
    __tdlib_type__ = "LanguagePackStringValue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LanguagePackStrings(RootObject):
    __tdlib_type__ = "LanguagePackStrings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LinkState(RootObject):
    __tdlib_type__ = "LinkState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LocalFile(RootObject):
    __tdlib_type__ = "LocalFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LocalizationTargetInfo(RootObject):
    __tdlib_type__ = "LocalizationTargetInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Location(RootObject):
    __tdlib_type__ = "Location"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LogStream(RootObject):
    __tdlib_type__ = "LogStream"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LogTags(RootObject):
    __tdlib_type__ = "LogTags"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_LogVerbosityLevel(RootObject):
    __tdlib_type__ = "LogVerbosityLevel"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MaskPoint(RootObject):
    __tdlib_type__ = "MaskPoint"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MaskPosition(RootObject):
    __tdlib_type__ = "MaskPosition"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Message(RootObject):
    __tdlib_type__ = "Message"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MessageContent(RootObject):
    __tdlib_type__ = "MessageContent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MessageForwardInfo(RootObject):
    __tdlib_type__ = "MessageForwardInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MessageForwardOrigin(RootObject):
    __tdlib_type__ = "MessageForwardOrigin"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MessageLinkInfo(RootObject):
    __tdlib_type__ = "MessageLinkInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_MessageSendingState(RootObject):
    __tdlib_type__ = "MessageSendingState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Messages(RootObject):
    __tdlib_type__ = "Messages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Minithumbnail(RootObject):
    __tdlib_type__ = "Minithumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NetworkStatistics(RootObject):
    __tdlib_type__ = "NetworkStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NetworkStatisticsEntry(RootObject):
    __tdlib_type__ = "NetworkStatisticsEntry"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NetworkType(RootObject):
    __tdlib_type__ = "NetworkType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Notification(RootObject):
    __tdlib_type__ = "Notification"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NotificationGroup(RootObject):
    __tdlib_type__ = "NotificationGroup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NotificationGroupType(RootObject):
    __tdlib_type__ = "NotificationGroupType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NotificationSettingsScope(RootObject):
    __tdlib_type__ = "NotificationSettingsScope"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_NotificationType(RootObject):
    __tdlib_type__ = "NotificationType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Ok(RootObject):
    __tdlib_type__ = "Ok"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_OptionValue(RootObject):
    __tdlib_type__ = "OptionValue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_OrderInfo(RootObject):
    __tdlib_type__ = "OrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlock(RootObject):
    __tdlib_type__ = "PageBlock"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlockCaption(RootObject):
    __tdlib_type__ = "PageBlockCaption"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlockHorizontalAlignment(RootObject):
    __tdlib_type__ = "PageBlockHorizontalAlignment"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlockListItem(RootObject):
    __tdlib_type__ = "PageBlockListItem"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlockRelatedArticle(RootObject):
    __tdlib_type__ = "PageBlockRelatedArticle"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlockTableCell(RootObject):
    __tdlib_type__ = "PageBlockTableCell"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PageBlockVerticalAlignment(RootObject):
    __tdlib_type__ = "PageBlockVerticalAlignment"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportAuthorizationForm(RootObject):
    __tdlib_type__ = "PassportAuthorizationForm"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportElement(RootObject):
    __tdlib_type__ = "PassportElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportElementError(RootObject):
    __tdlib_type__ = "PassportElementError"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportElementErrorSource(RootObject):
    __tdlib_type__ = "PassportElementErrorSource"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportElementType(RootObject):
    __tdlib_type__ = "PassportElementType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportElements(RootObject):
    __tdlib_type__ = "PassportElements"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportElementsWithErrors(RootObject):
    __tdlib_type__ = "PassportElementsWithErrors"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportRequiredElement(RootObject):
    __tdlib_type__ = "PassportRequiredElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PassportSuitableElement(RootObject):
    __tdlib_type__ = "PassportSuitableElement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PasswordState(RootObject):
    __tdlib_type__ = "PasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PaymentForm(RootObject):
    __tdlib_type__ = "PaymentForm"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PaymentReceipt(RootObject):
    __tdlib_type__ = "PaymentReceipt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PaymentResult(RootObject):
    __tdlib_type__ = "PaymentResult"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PaymentsProviderStripe(RootObject):
    __tdlib_type__ = "PaymentsProviderStripe"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PersonalDetails(RootObject):
    __tdlib_type__ = "PersonalDetails"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PersonalDocument(RootObject):
    __tdlib_type__ = "PersonalDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PhoneNumberAuthenticationSettings(RootObject):
    __tdlib_type__ = "PhoneNumberAuthenticationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Photo(RootObject):
    __tdlib_type__ = "Photo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PhotoSize(RootObject):
    __tdlib_type__ = "PhotoSize"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Poll(RootObject):
    __tdlib_type__ = "Poll"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PollOption(RootObject):
    __tdlib_type__ = "PollOption"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ProfilePhoto(RootObject):
    __tdlib_type__ = "ProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Proxies(RootObject):
    __tdlib_type__ = "Proxies"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Proxy(RootObject):
    __tdlib_type__ = "Proxy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ProxyType(RootObject):
    __tdlib_type__ = "ProxyType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PublicMessageLink(RootObject):
    __tdlib_type__ = "PublicMessageLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PushMessageContent(RootObject):
    __tdlib_type__ = "PushMessageContent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_PushReceiverId(RootObject):
    __tdlib_type__ = "PushReceiverId"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_RecoveryEmailAddress(RootObject):
    __tdlib_type__ = "RecoveryEmailAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_RemoteFile(RootObject):
    __tdlib_type__ = "RemoteFile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ReplyMarkup(RootObject):
    __tdlib_type__ = "ReplyMarkup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_RichText(RootObject):
    __tdlib_type__ = "RichText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_SavedCredentials(RootObject):
    __tdlib_type__ = "SavedCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ScopeNotificationSettings(RootObject):
    __tdlib_type__ = "ScopeNotificationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_SearchMessagesFilter(RootObject):
    __tdlib_type__ = "SearchMessagesFilter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Seconds(RootObject):
    __tdlib_type__ = "Seconds"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_SecretChat(RootObject):
    __tdlib_type__ = "SecretChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_SecretChatState(RootObject):
    __tdlib_type__ = "SecretChatState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Session(RootObject):
    __tdlib_type__ = "Session"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Sessions(RootObject):
    __tdlib_type__ = "Sessions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ShippingOption(RootObject):
    __tdlib_type__ = "ShippingOption"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Sticker(RootObject):
    __tdlib_type__ = "Sticker"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StickerSet(RootObject):
    __tdlib_type__ = "StickerSet"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StickerSetInfo(RootObject):
    __tdlib_type__ = "StickerSetInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StickerSets(RootObject):
    __tdlib_type__ = "StickerSets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Stickers(RootObject):
    __tdlib_type__ = "Stickers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StorageStatistics(RootObject):
    __tdlib_type__ = "StorageStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StorageStatisticsByChat(RootObject):
    __tdlib_type__ = "StorageStatisticsByChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StorageStatisticsByFileType(RootObject):
    __tdlib_type__ = "StorageStatisticsByFileType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_StorageStatisticsFast(RootObject):
    __tdlib_type__ = "StorageStatisticsFast"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Supergroup(RootObject):
    __tdlib_type__ = "Supergroup"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_SupergroupFullInfo(RootObject):
    __tdlib_type__ = "SupergroupFullInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_SupergroupMembersFilter(RootObject):
    __tdlib_type__ = "SupergroupMembersFilter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TMeUrl(RootObject):
    __tdlib_type__ = "TMeUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TMeUrlType(RootObject):
    __tdlib_type__ = "TMeUrlType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TMeUrls(RootObject):
    __tdlib_type__ = "TMeUrls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TdlibParameters(RootObject):
    __tdlib_type__ = "TdlibParameters"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TemporaryPasswordState(RootObject):
    __tdlib_type__ = "TemporaryPasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TermsOfService(RootObject):
    __tdlib_type__ = "TermsOfService"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestBytes(RootObject):
    __tdlib_type__ = "TestBytes"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestInt(RootObject):
    __tdlib_type__ = "TestInt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestString(RootObject):
    __tdlib_type__ = "TestString"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestVectorInt(RootObject):
    __tdlib_type__ = "TestVectorInt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestVectorIntObject(RootObject):
    __tdlib_type__ = "TestVectorIntObject"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestVectorString(RootObject):
    __tdlib_type__ = "TestVectorString"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TestVectorStringObject(RootObject):
    __tdlib_type__ = "TestVectorStringObject"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Text(RootObject):
    __tdlib_type__ = "Text"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TextEntities(RootObject):
    __tdlib_type__ = "TextEntities"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TextEntity(RootObject):
    __tdlib_type__ = "TextEntity"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TextEntityType(RootObject):
    __tdlib_type__ = "TextEntityType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TextParseMode(RootObject):
    __tdlib_type__ = "TextParseMode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TonLiteServerResponse(RootObject):
    __tdlib_type__ = "TonLiteServerResponse"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TonWalletPasswordSalt(RootObject):
    __tdlib_type__ = "TonWalletPasswordSalt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_TopChatCategory(RootObject):
    __tdlib_type__ = "TopChatCategory"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Update(RootObject):
    __tdlib_type__ = "Update"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Updates(RootObject):
    __tdlib_type__ = "Updates"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_User(RootObject):
    __tdlib_type__ = "User"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserFullInfo(RootObject):
    __tdlib_type__ = "UserFullInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserPrivacySetting(RootObject):
    __tdlib_type__ = "UserPrivacySetting"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserPrivacySettingRule(RootObject):
    __tdlib_type__ = "UserPrivacySettingRule"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserPrivacySettingRules(RootObject):
    __tdlib_type__ = "UserPrivacySettingRules"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserProfilePhoto(RootObject):
    __tdlib_type__ = "UserProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserProfilePhotos(RootObject):
    __tdlib_type__ = "UserProfilePhotos"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserStatus(RootObject):
    __tdlib_type__ = "UserStatus"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_UserType(RootObject):
    __tdlib_type__ = "UserType"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Users(RootObject):
    __tdlib_type__ = "Users"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ValidatedOrderInfo(RootObject):
    __tdlib_type__ = "ValidatedOrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Venue(RootObject):
    __tdlib_type__ = "Venue"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_Video(RootObject):
    __tdlib_type__ = "Video"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_VideoNote(RootObject):
    __tdlib_type__ = "VideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_VoiceNote(RootObject):
    __tdlib_type__ = "VoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_WebPage(RootObject):
    __tdlib_type__ = "WebPage"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_WebPageInstantView(RootObject):
    __tdlib_type__ = "WebPageInstantView"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_accountTtl(AccountTtl):
    __tdlib_type__ = "accountTtl"
    days:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_address(Address):
    __tdlib_type__ = "address"
    country_code:str = attr.ib()
    state:str = attr.ib()
    city:str = attr.ib()
    street_line1:str = attr.ib()
    street_line2:str = attr.ib()
    postal_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_animation(Animation):
    __tdlib_type__ = "animation"
    duration:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    file_name:str = attr.ib()
    mime_type:str = attr.ib()
    minithumbnail:minithumbnail = attr.ib()
    thumbnail:photoSize = attr.ib()
    animation:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_animations(Animations):
    __tdlib_type__ = "animations"
    animations:typing.Sequence[animation] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_audio(Audio):
    __tdlib_type__ = "audio"
    duration:int = attr.ib()
    title:str = attr.ib()
    performer:str = attr.ib()
    file_name:str = attr.ib()
    mime_type:str = attr.ib()
    album_cover_minithumbnail:minithumbnail = attr.ib()
    album_cover_thumbnail:photoSize = attr.ib()
    audio:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authenticationCodeInfo(AuthenticationCodeInfo):
    __tdlib_type__ = "authenticationCodeInfo"
    phone_number:str = attr.ib()
    type:AuthenticationCodeType = attr.ib()
    next_type:AuthenticationCodeType = attr.ib()
    timeout:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authenticationCodeTypeCall(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeCall"
    length:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authenticationCodeTypeFlashCall(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeFlashCall"
    pattern:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authenticationCodeTypeSms(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeSms"
    length:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authenticationCodeTypeTelegramMessage(AuthenticationCodeType):
    __tdlib_type__ = "authenticationCodeTypeTelegramMessage"
    length:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateClosed(AuthorizationState):
    __tdlib_type__ = "authorizationStateClosed"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateClosing(AuthorizationState):
    __tdlib_type__ = "authorizationStateClosing"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateLoggingOut(AuthorizationState):
    __tdlib_type__ = "authorizationStateLoggingOut"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateReady(AuthorizationState):
    __tdlib_type__ = "authorizationStateReady"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateWaitCode(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitCode"
    code_info:authenticationCodeInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateWaitEncryptionKey(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitEncryptionKey"
    is_encrypted:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateWaitPassword(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitPassword"
    password_hint:str = attr.ib()
    has_recovery_email_address:bool = attr.ib()
    recovery_email_address_pattern:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateWaitPhoneNumber(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateWaitRegistration(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitRegistration"
    terms_of_service:termsOfService = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_authorizationStateWaitTdlibParameters(AuthorizationState):
    __tdlib_type__ = "authorizationStateWaitTdlibParameters"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_autoDownloadSettings(AutoDownloadSettings):
    __tdlib_type__ = "autoDownloadSettings"
    is_auto_download_enabled:bool = attr.ib()
    max_photo_file_size:int = attr.ib()
    max_video_file_size:int = attr.ib()
    max_other_file_size:int = attr.ib()
    preload_large_videos:bool = attr.ib()
    preload_next_audio:bool = attr.ib()
    use_less_data_for_calls:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_autoDownloadSettingsPresets(AutoDownloadSettingsPresets):
    __tdlib_type__ = "autoDownloadSettingsPresets"
    low:autoDownloadSettings = attr.ib()
    medium:autoDownloadSettings = attr.ib()
    high:autoDownloadSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_background(Background):
    __tdlib_type__ = "background"
    id:int = attr.ib()
    is_default:bool = attr.ib()
    is_dark:bool = attr.ib()
    name:str = attr.ib()
    document:document = attr.ib()
    type:BackgroundType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_backgroundTypePattern(BackgroundType):
    __tdlib_type__ = "backgroundTypePattern"
    is_moving:bool = attr.ib()
    color:int = attr.ib()
    intensity:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_backgroundTypeSolid(BackgroundType):
    __tdlib_type__ = "backgroundTypeSolid"
    color:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_backgroundTypeWallpaper(BackgroundType):
    __tdlib_type__ = "backgroundTypeWallpaper"
    is_blurred:bool = attr.ib()
    is_moving:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_backgrounds(Backgrounds):
    __tdlib_type__ = "backgrounds"
    backgrounds:typing.Sequence[background] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_basicGroup(BasicGroup):
    __tdlib_type__ = "basicGroup"
    id:int = attr.ib()
    member_count:int = attr.ib()
    status:ChatMemberStatus = attr.ib()
    is_active:bool = attr.ib()
    upgraded_to_supergroup_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_basicGroupFullInfo(BasicGroupFullInfo):
    __tdlib_type__ = "basicGroupFullInfo"
    description:str = attr.ib()
    creator_user_id:int = attr.ib()
    members:typing.Sequence[chatMember] = attr.ib()
    invite_link:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_botCommand(BotCommand):
    __tdlib_type__ = "botCommand"
    command:str = attr.ib()
    description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_botInfo(BotInfo):
    __tdlib_type__ = "botInfo"
    description:str = attr.ib()
    commands:typing.Sequence[botCommand] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_call(Call):
    __tdlib_type__ = "call"
    id:int = attr.ib()
    user_id:int = attr.ib()
    is_outgoing:bool = attr.ib()
    state:CallState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callConnection(CallConnection):
    __tdlib_type__ = "callConnection"
    id:int = attr.ib()
    ip:str = attr.ib()
    ipv6:str = attr.ib()
    port:int = attr.ib()
    peer_tag:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callDiscardReasonDeclined(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonDeclined"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callDiscardReasonDisconnected(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonDisconnected"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callDiscardReasonEmpty(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callDiscardReasonHungUp(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonHungUp"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callDiscardReasonMissed(CallDiscardReason):
    __tdlib_type__ = "callDiscardReasonMissed"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callId(CallId):
    __tdlib_type__ = "callId"
    id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemDistortedSpeech(CallProblem):
    __tdlib_type__ = "callProblemDistortedSpeech"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemDropped(CallProblem):
    __tdlib_type__ = "callProblemDropped"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemEcho(CallProblem):
    __tdlib_type__ = "callProblemEcho"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemInterruptions(CallProblem):
    __tdlib_type__ = "callProblemInterruptions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemNoise(CallProblem):
    __tdlib_type__ = "callProblemNoise"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemSilentLocal(CallProblem):
    __tdlib_type__ = "callProblemSilentLocal"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProblemSilentRemote(CallProblem):
    __tdlib_type__ = "callProblemSilentRemote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callProtocol(CallProtocol):
    __tdlib_type__ = "callProtocol"
    udp_p2p:bool = attr.ib()
    udp_reflector:bool = attr.ib()
    min_layer:int = attr.ib()
    max_layer:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callStateDiscarded(CallState):
    __tdlib_type__ = "callStateDiscarded"
    reason:CallDiscardReason = attr.ib()
    need_rating:bool = attr.ib()
    need_debug_information:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callStateError(CallState):
    __tdlib_type__ = "callStateError"
    error:error = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callStateExchangingKeys(CallState):
    __tdlib_type__ = "callStateExchangingKeys"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callStateHangingUp(CallState):
    __tdlib_type__ = "callStateHangingUp"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callStatePending(CallState):
    __tdlib_type__ = "callStatePending"
    is_created:bool = attr.ib()
    is_received:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callStateReady(CallState):
    __tdlib_type__ = "callStateReady"
    protocol:callProtocol = attr.ib()
    connections:typing.Sequence[callConnection] = attr.ib()
    config:str = attr.ib()
    encryption_key:bytes = attr.ib()
    emojis:typing.Sequence[str] = attr.ib()
    allow_p2p:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callbackQueryAnswer(CallbackQueryAnswer):
    __tdlib_type__ = "callbackQueryAnswer"
    text:str = attr.ib()
    show_alert:bool = attr.ib()
    url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callbackQueryPayloadData(CallbackQueryPayload):
    __tdlib_type__ = "callbackQueryPayloadData"
    data:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_callbackQueryPayloadGame(CallbackQueryPayload):
    __tdlib_type__ = "callbackQueryPayloadGame"
    game_short_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chat(Chat):
    __tdlib_type__ = "chat"
    id:int = attr.ib()
    type:ChatType = attr.ib()
    title:str = attr.ib()
    photo:chatPhoto = attr.ib()
    permissions:chatPermissions = attr.ib()
    last_message:message = attr.ib()
    order:int = attr.ib()
    is_pinned:bool = attr.ib()
    is_marked_as_unread:bool = attr.ib()
    is_sponsored:bool = attr.ib()
    can_be_deleted_only_for_self:bool = attr.ib()
    can_be_deleted_for_all_users:bool = attr.ib()
    can_be_reported:bool = attr.ib()
    default_disable_notification:bool = attr.ib()
    unread_count:int = attr.ib()
    last_read_inbox_message_id:int = attr.ib()
    last_read_outbox_message_id:int = attr.ib()
    unread_mention_count:int = attr.ib()
    notification_settings:chatNotificationSettings = attr.ib()
    pinned_message_id:int = attr.ib()
    reply_markup_message_id:int = attr.ib()
    draft_message:draftMessage = attr.ib()
    client_data:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionCancel(ChatAction):
    __tdlib_type__ = "chatActionCancel"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionChoosingContact(ChatAction):
    __tdlib_type__ = "chatActionChoosingContact"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionChoosingLocation(ChatAction):
    __tdlib_type__ = "chatActionChoosingLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionRecordingVideo(ChatAction):
    __tdlib_type__ = "chatActionRecordingVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionRecordingVideoNote(ChatAction):
    __tdlib_type__ = "chatActionRecordingVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionRecordingVoiceNote(ChatAction):
    __tdlib_type__ = "chatActionRecordingVoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionStartPlayingGame(ChatAction):
    __tdlib_type__ = "chatActionStartPlayingGame"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionTyping(ChatAction):
    __tdlib_type__ = "chatActionTyping"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionUploadingDocument(ChatAction):
    __tdlib_type__ = "chatActionUploadingDocument"
    progress:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionUploadingPhoto(ChatAction):
    __tdlib_type__ = "chatActionUploadingPhoto"
    progress:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionUploadingVideo(ChatAction):
    __tdlib_type__ = "chatActionUploadingVideo"
    progress:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionUploadingVideoNote(ChatAction):
    __tdlib_type__ = "chatActionUploadingVideoNote"
    progress:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatActionUploadingVoiceNote(ChatAction):
    __tdlib_type__ = "chatActionUploadingVoiceNote"
    progress:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEvent(ChatEvent):
    __tdlib_type__ = "chatEvent"
    id:int = attr.ib()
    date:int = attr.ib()
    user_id:int = attr.ib()
    action:ChatEventAction = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventDescriptionChanged(ChatEventAction):
    __tdlib_type__ = "chatEventDescriptionChanged"
    old_description:str = attr.ib()
    new_description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventInvitesToggled(ChatEventAction):
    __tdlib_type__ = "chatEventInvitesToggled"
    can_invite_users:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventIsAllHistoryAvailableToggled(ChatEventAction):
    __tdlib_type__ = "chatEventIsAllHistoryAvailableToggled"
    is_all_history_available:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventLogFilters(ChatEventLogFilters):
    __tdlib_type__ = "chatEventLogFilters"
    message_edits:bool = attr.ib()
    message_deletions:bool = attr.ib()
    message_pins:bool = attr.ib()
    member_joins:bool = attr.ib()
    member_leaves:bool = attr.ib()
    member_invites:bool = attr.ib()
    member_promotions:bool = attr.ib()
    member_restrictions:bool = attr.ib()
    info_changes:bool = attr.ib()
    setting_changes:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMemberInvited(ChatEventAction):
    __tdlib_type__ = "chatEventMemberInvited"
    user_id:int = attr.ib()
    status:ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMemberJoined(ChatEventAction):
    __tdlib_type__ = "chatEventMemberJoined"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMemberLeft(ChatEventAction):
    __tdlib_type__ = "chatEventMemberLeft"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMemberPromoted(ChatEventAction):
    __tdlib_type__ = "chatEventMemberPromoted"
    user_id:int = attr.ib()
    old_status:ChatMemberStatus = attr.ib()
    new_status:ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMemberRestricted(ChatEventAction):
    __tdlib_type__ = "chatEventMemberRestricted"
    user_id:int = attr.ib()
    old_status:ChatMemberStatus = attr.ib()
    new_status:ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMessageDeleted(ChatEventAction):
    __tdlib_type__ = "chatEventMessageDeleted"
    message:message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMessageEdited(ChatEventAction):
    __tdlib_type__ = "chatEventMessageEdited"
    old_message:message = attr.ib()
    new_message:message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMessagePinned(ChatEventAction):
    __tdlib_type__ = "chatEventMessagePinned"
    message:message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventMessageUnpinned(ChatEventAction):
    __tdlib_type__ = "chatEventMessageUnpinned"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventPermissionsChanged(ChatEventAction):
    __tdlib_type__ = "chatEventPermissionsChanged"
    old_permissions:chatPermissions = attr.ib()
    new_permissions:chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventPhotoChanged(ChatEventAction):
    __tdlib_type__ = "chatEventPhotoChanged"
    old_photo:photo = attr.ib()
    new_photo:photo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventPollStopped(ChatEventAction):
    __tdlib_type__ = "chatEventPollStopped"
    message:message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventSignMessagesToggled(ChatEventAction):
    __tdlib_type__ = "chatEventSignMessagesToggled"
    sign_messages:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventStickerSetChanged(ChatEventAction):
    __tdlib_type__ = "chatEventStickerSetChanged"
    old_sticker_set_id:int = attr.ib()
    new_sticker_set_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventTitleChanged(ChatEventAction):
    __tdlib_type__ = "chatEventTitleChanged"
    old_title:str = attr.ib()
    new_title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEventUsernameChanged(ChatEventAction):
    __tdlib_type__ = "chatEventUsernameChanged"
    old_username:str = attr.ib()
    new_username:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatEvents(ChatEvents):
    __tdlib_type__ = "chatEvents"
    events:typing.Sequence[chatEvent] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatInviteLink(ChatInviteLink):
    __tdlib_type__ = "chatInviteLink"
    invite_link:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatInviteLinkInfo(ChatInviteLinkInfo):
    __tdlib_type__ = "chatInviteLinkInfo"
    chat_id:int = attr.ib()
    type:ChatType = attr.ib()
    title:str = attr.ib()
    photo:chatPhoto = attr.ib()
    member_count:int = attr.ib()
    member_user_ids:typing.Sequence[int] = attr.ib()
    is_public:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMember(ChatMember):
    __tdlib_type__ = "chatMember"
    user_id:int = attr.ib()
    inviter_user_id:int = attr.ib()
    joined_chat_date:int = attr.ib()
    status:ChatMemberStatus = attr.ib()
    bot_info:botInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMemberStatusAdministrator(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusAdministrator"
    can_be_edited:bool = attr.ib()
    can_change_info:bool = attr.ib()
    can_post_messages:bool = attr.ib()
    can_edit_messages:bool = attr.ib()
    can_delete_messages:bool = attr.ib()
    can_invite_users:bool = attr.ib()
    can_restrict_members:bool = attr.ib()
    can_pin_messages:bool = attr.ib()
    can_promote_members:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMemberStatusBanned(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusBanned"
    banned_until_date:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMemberStatusCreator(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusCreator"
    is_member:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMemberStatusLeft(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusLeft"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMemberStatusMember(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusMember"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMemberStatusRestricted(ChatMemberStatus):
    __tdlib_type__ = "chatMemberStatusRestricted"
    is_member:bool = attr.ib()
    restricted_until_date:int = attr.ib()
    permissions:chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembers(ChatMembers):
    __tdlib_type__ = "chatMembers"
    total_count:int = attr.ib()
    members:typing.Sequence[chatMember] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembersFilterAdministrators(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterAdministrators"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembersFilterBanned(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterBanned"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembersFilterBots(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembersFilterContacts(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembersFilterMembers(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterMembers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatMembersFilterRestricted(ChatMembersFilter):
    __tdlib_type__ = "chatMembersFilterRestricted"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatNotificationSettings(ChatNotificationSettings):
    __tdlib_type__ = "chatNotificationSettings"
    use_default_mute_for:bool = attr.ib()
    mute_for:int = attr.ib()
    use_default_sound:bool = attr.ib()
    sound:str = attr.ib()
    use_default_show_preview:bool = attr.ib()
    show_preview:bool = attr.ib()
    use_default_disable_pinned_message_notifications:bool = attr.ib()
    disable_pinned_message_notifications:bool = attr.ib()
    use_default_disable_mention_notifications:bool = attr.ib()
    disable_mention_notifications:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatPermissions(ChatPermissions):
    __tdlib_type__ = "chatPermissions"
    can_send_messages:bool = attr.ib()
    can_send_media_messages:bool = attr.ib()
    can_send_polls:bool = attr.ib()
    can_send_other_messages:bool = attr.ib()
    can_add_web_page_previews:bool = attr.ib()
    can_change_info:bool = attr.ib()
    can_invite_users:bool = attr.ib()
    can_pin_messages:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatPhoto(ChatPhoto):
    __tdlib_type__ = "chatPhoto"
    small:file = attr.ib()
    big:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportReasonChildAbuse(ChatReportReason):
    __tdlib_type__ = "chatReportReasonChildAbuse"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportReasonCopyright(ChatReportReason):
    __tdlib_type__ = "chatReportReasonCopyright"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportReasonCustom(ChatReportReason):
    __tdlib_type__ = "chatReportReasonCustom"
    text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportReasonPornography(ChatReportReason):
    __tdlib_type__ = "chatReportReasonPornography"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportReasonSpam(ChatReportReason):
    __tdlib_type__ = "chatReportReasonSpam"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportReasonViolence(ChatReportReason):
    __tdlib_type__ = "chatReportReasonViolence"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatReportSpamState(ChatReportSpamState):
    __tdlib_type__ = "chatReportSpamState"
    can_report_spam:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatTypeBasicGroup(ChatType):
    __tdlib_type__ = "chatTypeBasicGroup"
    basic_group_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatTypePrivate(ChatType):
    __tdlib_type__ = "chatTypePrivate"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatTypeSecret(ChatType):
    __tdlib_type__ = "chatTypeSecret"
    secret_chat_id:int = attr.ib()
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chatTypeSupergroup(ChatType):
    __tdlib_type__ = "chatTypeSupergroup"
    supergroup_id:int = attr.ib()
    is_channel:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_chats(Chats):
    __tdlib_type__ = "chats"
    chat_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_checkChatUsernameResultOk(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultOk"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_checkChatUsernameResultPublicChatsTooMuch(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultPublicChatsTooMuch"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_checkChatUsernameResultPublicGroupsUnavailable(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultPublicGroupsUnavailable"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_checkChatUsernameResultUsernameInvalid(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultUsernameInvalid"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_checkChatUsernameResultUsernameOccupied(CheckChatUsernameResult):
    __tdlib_type__ = "checkChatUsernameResultUsernameOccupied"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectedWebsite(ConnectedWebsite):
    __tdlib_type__ = "connectedWebsite"
    id:int = attr.ib()
    domain_name:str = attr.ib()
    bot_user_id:int = attr.ib()
    browser:str = attr.ib()
    platform:str = attr.ib()
    log_in_date:int = attr.ib()
    last_active_date:int = attr.ib()
    ip:str = attr.ib()
    location:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectedWebsites(ConnectedWebsites):
    __tdlib_type__ = "connectedWebsites"
    websites:typing.Sequence[connectedWebsite] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectionStateConnecting(ConnectionState):
    __tdlib_type__ = "connectionStateConnecting"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectionStateConnectingToProxy(ConnectionState):
    __tdlib_type__ = "connectionStateConnectingToProxy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectionStateReady(ConnectionState):
    __tdlib_type__ = "connectionStateReady"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectionStateUpdating(ConnectionState):
    __tdlib_type__ = "connectionStateUpdating"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_connectionStateWaitingForNetwork(ConnectionState):
    __tdlib_type__ = "connectionStateWaitingForNetwork"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_contact(Contact):
    __tdlib_type__ = "contact"
    phone_number:str = attr.ib()
    first_name:str = attr.ib()
    last_name:str = attr.ib()
    vcard:str = attr.ib()
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_count(Count):
    __tdlib_type__ = "count"
    count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_customRequestResult(CustomRequestResult):
    __tdlib_type__ = "customRequestResult"
    result:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_databaseStatistics(DatabaseStatistics):
    __tdlib_type__ = "databaseStatistics"
    statistics:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_date(Date):
    __tdlib_type__ = "date"
    day:int = attr.ib()
    month:int = attr.ib()
    year:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_datedFile(DatedFile):
    __tdlib_type__ = "datedFile"
    file:file = attr.ib()
    date:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deepLinkInfo(DeepLinkInfo):
    __tdlib_type__ = "deepLinkInfo"
    text:formattedText = attr.ib()
    need_update_application:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenApplePush(DeviceToken):
    __tdlib_type__ = "deviceTokenApplePush"
    device_token:str = attr.ib()
    is_app_sandbox:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenApplePushVoIP(DeviceToken):
    __tdlib_type__ = "deviceTokenApplePushVoIP"
    device_token:str = attr.ib()
    is_app_sandbox:bool = attr.ib()
    encrypt:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenBlackBerryPush(DeviceToken):
    __tdlib_type__ = "deviceTokenBlackBerryPush"
    token:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenFirebaseCloudMessaging(DeviceToken):
    __tdlib_type__ = "deviceTokenFirebaseCloudMessaging"
    token:str = attr.ib()
    encrypt:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenMicrosoftPush(DeviceToken):
    __tdlib_type__ = "deviceTokenMicrosoftPush"
    channel_uri:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenMicrosoftPushVoIP(DeviceToken):
    __tdlib_type__ = "deviceTokenMicrosoftPushVoIP"
    channel_uri:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenSimplePush(DeviceToken):
    __tdlib_type__ = "deviceTokenSimplePush"
    endpoint:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenTizenPush(DeviceToken):
    __tdlib_type__ = "deviceTokenTizenPush"
    reg_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenUbuntuPush(DeviceToken):
    __tdlib_type__ = "deviceTokenUbuntuPush"
    token:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenWebPush(DeviceToken):
    __tdlib_type__ = "deviceTokenWebPush"
    endpoint:str = attr.ib()
    p256dh_base64url:str = attr.ib()
    auth_base64url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_deviceTokenWindowsPush(DeviceToken):
    __tdlib_type__ = "deviceTokenWindowsPush"
    access_token:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_document(Document):
    __tdlib_type__ = "document"
    file_name:str = attr.ib()
    mime_type:str = attr.ib()
    minithumbnail:minithumbnail = attr.ib()
    thumbnail:photoSize = attr.ib()
    document:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_draftMessage(DraftMessage):
    __tdlib_type__ = "draftMessage"
    reply_to_message_id:int = attr.ib()
    input_message_text:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_emailAddressAuthenticationCodeInfo(EmailAddressAuthenticationCodeInfo):
    __tdlib_type__ = "emailAddressAuthenticationCodeInfo"
    email_address_pattern:str = attr.ib()
    length:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_emojis(Emojis):
    __tdlib_type__ = "emojis"
    emojis:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_encryptedCredentials(EncryptedCredentials):
    __tdlib_type__ = "encryptedCredentials"
    data:bytes = attr.ib()
    hash:bytes = attr.ib()
    secret:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_encryptedPassportElement(EncryptedPassportElement):
    __tdlib_type__ = "encryptedPassportElement"
    type:PassportElementType = attr.ib()
    data:bytes = attr.ib()
    front_side:datedFile = attr.ib()
    reverse_side:datedFile = attr.ib()
    selfie:datedFile = attr.ib()
    translation:typing.Sequence[datedFile] = attr.ib()
    files:typing.Sequence[datedFile] = attr.ib()
    value:str = attr.ib()
    hash:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_error(Error):
    __tdlib_type__ = "error"
    code:int = attr.ib()
    message:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_file(File):
    __tdlib_type__ = "file"
    id:int = attr.ib()
    size:int = attr.ib()
    expected_size:int = attr.ib()
    local:localFile = attr.ib()
    remote:remoteFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_filePart(FilePart):
    __tdlib_type__ = "filePart"
    data:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeAnimation(FileType):
    __tdlib_type__ = "fileTypeAnimation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeAudio(FileType):
    __tdlib_type__ = "fileTypeAudio"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeDocument(FileType):
    __tdlib_type__ = "fileTypeDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeNone(FileType):
    __tdlib_type__ = "fileTypeNone"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypePhoto(FileType):
    __tdlib_type__ = "fileTypePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeProfilePhoto(FileType):
    __tdlib_type__ = "fileTypeProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeSecret(FileType):
    __tdlib_type__ = "fileTypeSecret"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeSecretThumbnail(FileType):
    __tdlib_type__ = "fileTypeSecretThumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeSecure(FileType):
    __tdlib_type__ = "fileTypeSecure"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeSticker(FileType):
    __tdlib_type__ = "fileTypeSticker"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeThumbnail(FileType):
    __tdlib_type__ = "fileTypeThumbnail"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeUnknown(FileType):
    __tdlib_type__ = "fileTypeUnknown"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeVideo(FileType):
    __tdlib_type__ = "fileTypeVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeVideoNote(FileType):
    __tdlib_type__ = "fileTypeVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeVoiceNote(FileType):
    __tdlib_type__ = "fileTypeVoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_fileTypeWallpaper(FileType):
    __tdlib_type__ = "fileTypeWallpaper"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_formattedText(FormattedText):
    __tdlib_type__ = "formattedText"
    text:str = attr.ib()
    entities:typing.Sequence[textEntity] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_foundMessages(FoundMessages):
    __tdlib_type__ = "foundMessages"
    messages:typing.Sequence[message] = attr.ib()
    next_from_search_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_game(Game):
    __tdlib_type__ = "game"
    id:int = attr.ib()
    short_name:str = attr.ib()
    title:str = attr.ib()
    text:formattedText = attr.ib()
    description:str = attr.ib()
    photo:photo = attr.ib()
    animation:animation = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_gameHighScore(GameHighScore):
    __tdlib_type__ = "gameHighScore"
    position:int = attr.ib()
    user_id:int = attr.ib()
    score:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_gameHighScores(GameHighScores):
    __tdlib_type__ = "gameHighScores"
    scores:typing.Sequence[gameHighScore] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_hashtags(Hashtags):
    __tdlib_type__ = "hashtags"
    hashtags:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_httpUrl(HttpUrl):
    __tdlib_type__ = "httpUrl"
    url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_identityDocument(IdentityDocument):
    __tdlib_type__ = "identityDocument"
    number:str = attr.ib()
    expiry_date:date = attr.ib()
    front_side:datedFile = attr.ib()
    reverse_side:datedFile = attr.ib()
    selfie:datedFile = attr.ib()
    translation:typing.Sequence[datedFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_importedContacts(ImportedContacts):
    __tdlib_type__ = "importedContacts"
    user_ids:typing.Sequence[int] = attr.ib()
    importer_count:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButton(InlineKeyboardButton):
    __tdlib_type__ = "inlineKeyboardButton"
    text:str = attr.ib()
    type:InlineKeyboardButtonType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButtonTypeBuy(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeBuy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButtonTypeCallback(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeCallback"
    data:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButtonTypeCallbackGame(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeCallbackGame"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButtonTypeLoginUrl(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeLoginUrl"
    url:str = attr.ib()
    id:int = attr.ib()
    forward_text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButtonTypeSwitchInline(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeSwitchInline"
    query:str = attr.ib()
    in_current_chat:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineKeyboardButtonTypeUrl(InlineKeyboardButtonType):
    __tdlib_type__ = "inlineKeyboardButtonTypeUrl"
    url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultAnimation(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultAnimation"
    id:str = attr.ib()
    animation:animation = attr.ib()
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultArticle(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultArticle"
    id:str = attr.ib()
    url:str = attr.ib()
    hide_url:bool = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    thumbnail:photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultAudio(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultAudio"
    id:str = attr.ib()
    audio:audio = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultContact(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultContact"
    id:str = attr.ib()
    contact:contact = attr.ib()
    thumbnail:photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultDocument(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultDocument"
    id:str = attr.ib()
    document:document = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultGame(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultGame"
    id:str = attr.ib()
    game:game = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultLocation(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultLocation"
    id:str = attr.ib()
    location:location = attr.ib()
    title:str = attr.ib()
    thumbnail:photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultPhoto(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultPhoto"
    id:str = attr.ib()
    photo:photo = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultSticker(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultSticker"
    id:str = attr.ib()
    sticker:sticker = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultVenue(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultVenue"
    id:str = attr.ib()
    venue:venue = attr.ib()
    thumbnail:photoSize = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultVideo(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultVideo"
    id:str = attr.ib()
    video:video = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResultVoiceNote(InlineQueryResult):
    __tdlib_type__ = "inlineQueryResultVoiceNote"
    id:str = attr.ib()
    voice_note:voiceNote = attr.ib()
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inlineQueryResults(InlineQueryResults):
    __tdlib_type__ = "inlineQueryResults"
    inline_query_id:int = attr.ib()
    next_offset:str = attr.ib()
    results:typing.Sequence[InlineQueryResult] = attr.ib()
    switch_pm_text:str = attr.ib()
    switch_pm_parameter:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputBackgroundLocal(InputBackground):
    __tdlib_type__ = "inputBackgroundLocal"
    background:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputBackgroundRemote(InputBackground):
    __tdlib_type__ = "inputBackgroundRemote"
    background_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputCredentialsAndroidPay(InputCredentials):
    __tdlib_type__ = "inputCredentialsAndroidPay"
    data:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputCredentialsApplePay(InputCredentials):
    __tdlib_type__ = "inputCredentialsApplePay"
    data:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputCredentialsNew(InputCredentials):
    __tdlib_type__ = "inputCredentialsNew"
    data:str = attr.ib()
    allow_save:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputCredentialsSaved(InputCredentials):
    __tdlib_type__ = "inputCredentialsSaved"
    saved_credentials_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputFileGenerated(InputFile):
    __tdlib_type__ = "inputFileGenerated"
    original_path:str = attr.ib()
    conversion:str = attr.ib()
    expected_size:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputFileId(InputFile):
    __tdlib_type__ = "inputFileId"
    id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputFileLocal(InputFile):
    __tdlib_type__ = "inputFileLocal"
    path:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputFileRemote(InputFile):
    __tdlib_type__ = "inputFileRemote"
    id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputIdentityDocument(InputIdentityDocument):
    __tdlib_type__ = "inputIdentityDocument"
    number:str = attr.ib()
    expiry_date:date = attr.ib()
    front_side:InputFile = attr.ib()
    reverse_side:InputFile = attr.ib()
    selfie:InputFile = attr.ib()
    translation:typing.Sequence[InputFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultAnimatedGif(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultAnimatedGif"
    id:str = attr.ib()
    title:str = attr.ib()
    thumbnail_url:str = attr.ib()
    gif_url:str = attr.ib()
    gif_duration:int = attr.ib()
    gif_width:int = attr.ib()
    gif_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultAnimatedMpeg4(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultAnimatedMpeg4"
    id:str = attr.ib()
    title:str = attr.ib()
    thumbnail_url:str = attr.ib()
    mpeg4_url:str = attr.ib()
    mpeg4_duration:int = attr.ib()
    mpeg4_width:int = attr.ib()
    mpeg4_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultArticle(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultArticle"
    id:str = attr.ib()
    url:str = attr.ib()
    hide_url:bool = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    thumbnail_url:str = attr.ib()
    thumbnail_width:int = attr.ib()
    thumbnail_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultAudio(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultAudio"
    id:str = attr.ib()
    title:str = attr.ib()
    performer:str = attr.ib()
    audio_url:str = attr.ib()
    audio_duration:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultContact(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultContact"
    id:str = attr.ib()
    contact:contact = attr.ib()
    thumbnail_url:str = attr.ib()
    thumbnail_width:int = attr.ib()
    thumbnail_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultDocument(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultDocument"
    id:str = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    document_url:str = attr.ib()
    mime_type:str = attr.ib()
    thumbnail_url:str = attr.ib()
    thumbnail_width:int = attr.ib()
    thumbnail_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultGame(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultGame"
    id:str = attr.ib()
    game_short_name:str = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultLocation(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultLocation"
    id:str = attr.ib()
    location:location = attr.ib()
    live_period:int = attr.ib()
    title:str = attr.ib()
    thumbnail_url:str = attr.ib()
    thumbnail_width:int = attr.ib()
    thumbnail_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultPhoto(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultPhoto"
    id:str = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    thumbnail_url:str = attr.ib()
    photo_url:str = attr.ib()
    photo_width:int = attr.ib()
    photo_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultSticker(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultSticker"
    id:str = attr.ib()
    thumbnail_url:str = attr.ib()
    sticker_url:str = attr.ib()
    sticker_width:int = attr.ib()
    sticker_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultVenue(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultVenue"
    id:str = attr.ib()
    venue:venue = attr.ib()
    thumbnail_url:str = attr.ib()
    thumbnail_width:int = attr.ib()
    thumbnail_height:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultVideo(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultVideo"
    id:str = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    thumbnail_url:str = attr.ib()
    video_url:str = attr.ib()
    mime_type:str = attr.ib()
    video_width:int = attr.ib()
    video_height:int = attr.ib()
    video_duration:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputInlineQueryResultVoiceNote(InputInlineQueryResult):
    __tdlib_type__ = "inputInlineQueryResultVoiceNote"
    id:str = attr.ib()
    title:str = attr.ib()
    voice_note_url:str = attr.ib()
    voice_note_duration:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageAnimation(InputMessageContent):
    __tdlib_type__ = "inputMessageAnimation"
    animation:InputFile = attr.ib()
    thumbnail:inputThumbnail = attr.ib()
    duration:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageAudio(InputMessageContent):
    __tdlib_type__ = "inputMessageAudio"
    audio:InputFile = attr.ib()
    album_cover_thumbnail:inputThumbnail = attr.ib()
    duration:int = attr.ib()
    title:str = attr.ib()
    performer:str = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageContact(InputMessageContent):
    __tdlib_type__ = "inputMessageContact"
    contact:contact = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageDocument(InputMessageContent):
    __tdlib_type__ = "inputMessageDocument"
    document:InputFile = attr.ib()
    thumbnail:inputThumbnail = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageForwarded(InputMessageContent):
    __tdlib_type__ = "inputMessageForwarded"
    from_chat_id:int = attr.ib()
    message_id:int = attr.ib()
    in_game_share:bool = attr.ib()
    send_copy:bool = attr.ib()
    remove_caption:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageGame(InputMessageContent):
    __tdlib_type__ = "inputMessageGame"
    bot_user_id:int = attr.ib()
    game_short_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageInvoice(InputMessageContent):
    __tdlib_type__ = "inputMessageInvoice"
    invoice:invoice = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    photo_url:str = attr.ib()
    photo_size:int = attr.ib()
    photo_width:int = attr.ib()
    photo_height:int = attr.ib()
    payload:bytes = attr.ib()
    provider_token:str = attr.ib()
    provider_data:str = attr.ib()
    start_parameter:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageLocation(InputMessageContent):
    __tdlib_type__ = "inputMessageLocation"
    location:location = attr.ib()
    live_period:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessagePhoto(InputMessageContent):
    __tdlib_type__ = "inputMessagePhoto"
    photo:InputFile = attr.ib()
    thumbnail:inputThumbnail = attr.ib()
    added_sticker_file_ids:typing.Sequence[int] = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    caption:formattedText = attr.ib()
    ttl:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessagePoll(InputMessageContent):
    __tdlib_type__ = "inputMessagePoll"
    question:str = attr.ib()
    options:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageSticker(InputMessageContent):
    __tdlib_type__ = "inputMessageSticker"
    sticker:InputFile = attr.ib()
    thumbnail:inputThumbnail = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageText(InputMessageContent):
    __tdlib_type__ = "inputMessageText"
    text:formattedText = attr.ib()
    disable_web_page_preview:bool = attr.ib()
    clear_draft:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageVenue(InputMessageContent):
    __tdlib_type__ = "inputMessageVenue"
    venue:venue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageVideo(InputMessageContent):
    __tdlib_type__ = "inputMessageVideo"
    video:InputFile = attr.ib()
    thumbnail:inputThumbnail = attr.ib()
    added_sticker_file_ids:typing.Sequence[int] = attr.ib()
    duration:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    supports_streaming:bool = attr.ib()
    caption:formattedText = attr.ib()
    ttl:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageVideoNote(InputMessageContent):
    __tdlib_type__ = "inputMessageVideoNote"
    video_note:InputFile = attr.ib()
    thumbnail:inputThumbnail = attr.ib()
    duration:int = attr.ib()
    length:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputMessageVoiceNote(InputMessageContent):
    __tdlib_type__ = "inputMessageVoiceNote"
    voice_note:InputFile = attr.ib()
    duration:int = attr.ib()
    waveform:bytes = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementAddress(InputPassportElement):
    __tdlib_type__ = "inputPassportElementAddress"
    address:address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementBankStatement(InputPassportElement):
    __tdlib_type__ = "inputPassportElementBankStatement"
    bank_statement:inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementDriverLicense(InputPassportElement):
    __tdlib_type__ = "inputPassportElementDriverLicense"
    driver_license:inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementEmailAddress(InputPassportElement):
    __tdlib_type__ = "inputPassportElementEmailAddress"
    email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementError(InputPassportElementError):
    __tdlib_type__ = "inputPassportElementError"
    type:PassportElementType = attr.ib()
    message:str = attr.ib()
    source:InputPassportElementErrorSource = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceDataField(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceDataField"
    field_name:str = attr.ib()
    data_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceFile(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceFile"
    file_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceFiles(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceFiles"
    file_hashes:typing.Sequence[bytes] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceFrontSide(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceFrontSide"
    file_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceReverseSide(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceReverseSide"
    file_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceSelfie(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceSelfie"
    file_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceTranslationFile(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceTranslationFile"
    file_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceTranslationFiles(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceTranslationFiles"
    file_hashes:typing.Sequence[bytes] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementErrorSourceUnspecified(InputPassportElementErrorSource):
    __tdlib_type__ = "inputPassportElementErrorSourceUnspecified"
    element_hash:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementIdentityCard(InputPassportElement):
    __tdlib_type__ = "inputPassportElementIdentityCard"
    identity_card:inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementInternalPassport(InputPassportElement):
    __tdlib_type__ = "inputPassportElementInternalPassport"
    internal_passport:inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementPassport(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPassport"
    passport:inputIdentityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementPassportRegistration(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPassportRegistration"
    passport_registration:inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementPersonalDetails(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPersonalDetails"
    personal_details:personalDetails = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementPhoneNumber(InputPassportElement):
    __tdlib_type__ = "inputPassportElementPhoneNumber"
    phone_number:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementRentalAgreement(InputPassportElement):
    __tdlib_type__ = "inputPassportElementRentalAgreement"
    rental_agreement:inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementTemporaryRegistration(InputPassportElement):
    __tdlib_type__ = "inputPassportElementTemporaryRegistration"
    temporary_registration:inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPassportElementUtilityBill(InputPassportElement):
    __tdlib_type__ = "inputPassportElementUtilityBill"
    utility_bill:inputPersonalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputPersonalDocument(InputPersonalDocument):
    __tdlib_type__ = "inputPersonalDocument"
    files:typing.Sequence[InputFile] = attr.ib()
    translation:typing.Sequence[InputFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputSticker(InputSticker):
    __tdlib_type__ = "inputSticker"
    png_sticker:InputFile = attr.ib()
    emojis:str = attr.ib()
    mask_position:maskPosition = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_inputThumbnail(InputThumbnail):
    __tdlib_type__ = "inputThumbnail"
    thumbnail:InputFile = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_invoice(Invoice):
    __tdlib_type__ = "invoice"
    currency:str = attr.ib()
    price_parts:typing.Sequence[labeledPricePart] = attr.ib()
    is_test:bool = attr.ib()
    need_name:bool = attr.ib()
    need_phone_number:bool = attr.ib()
    need_email_address:bool = attr.ib()
    need_shipping_address:bool = attr.ib()
    send_phone_number_to_provider:bool = attr.ib()
    send_email_address_to_provider:bool = attr.ib()
    is_flexible:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonObjectMember(JsonObjectMember):
    __tdlib_type__ = "jsonObjectMember"
    key:str = attr.ib()
    value:JsonValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonValueArray(JsonValue):
    __tdlib_type__ = "jsonValueArray"
    values:typing.Sequence[JsonValue] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonValueBoolean(JsonValue):
    __tdlib_type__ = "jsonValueBoolean"
    value:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonValueNull(JsonValue):
    __tdlib_type__ = "jsonValueNull"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonValueNumber(JsonValue):
    __tdlib_type__ = "jsonValueNumber"
    value:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonValueObject(JsonValue):
    __tdlib_type__ = "jsonValueObject"
    members:typing.Sequence[jsonObjectMember] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_jsonValueString(JsonValue):
    __tdlib_type__ = "jsonValueString"
    value:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_keyboardButton(KeyboardButton):
    __tdlib_type__ = "keyboardButton"
    text:str = attr.ib()
    type:KeyboardButtonType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_keyboardButtonTypeRequestLocation(KeyboardButtonType):
    __tdlib_type__ = "keyboardButtonTypeRequestLocation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_keyboardButtonTypeRequestPhoneNumber(KeyboardButtonType):
    __tdlib_type__ = "keyboardButtonTypeRequestPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_keyboardButtonTypeText(KeyboardButtonType):
    __tdlib_type__ = "keyboardButtonTypeText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_labeledPricePart(LabeledPricePart):
    __tdlib_type__ = "labeledPricePart"
    label:str = attr.ib()
    amount:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_languagePackInfo(LanguagePackInfo):
    __tdlib_type__ = "languagePackInfo"
    id:str = attr.ib()
    base_language_pack_id:str = attr.ib()
    name:str = attr.ib()
    native_name:str = attr.ib()
    plural_code:str = attr.ib()
    is_official:bool = attr.ib()
    is_rtl:bool = attr.ib()
    is_beta:bool = attr.ib()
    is_installed:bool = attr.ib()
    total_string_count:int = attr.ib()
    translated_string_count:int = attr.ib()
    local_string_count:int = attr.ib()
    translation_url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_languagePackString(LanguagePackString):
    __tdlib_type__ = "languagePackString"
    key:str = attr.ib()
    value:LanguagePackStringValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_languagePackStringValueDeleted(LanguagePackStringValue):
    __tdlib_type__ = "languagePackStringValueDeleted"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_languagePackStringValueOrdinary(LanguagePackStringValue):
    __tdlib_type__ = "languagePackStringValueOrdinary"
    value:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_languagePackStringValuePluralized(LanguagePackStringValue):
    __tdlib_type__ = "languagePackStringValuePluralized"
    zero_value:str = attr.ib()
    one_value:str = attr.ib()
    two_value:str = attr.ib()
    few_value:str = attr.ib()
    many_value:str = attr.ib()
    other_value:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_languagePackStrings(LanguagePackStrings):
    __tdlib_type__ = "languagePackStrings"
    strings:typing.Sequence[languagePackString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_linkStateIsContact(LinkState):
    __tdlib_type__ = "linkStateIsContact"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_linkStateKnowsPhoneNumber(LinkState):
    __tdlib_type__ = "linkStateKnowsPhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_linkStateNone(LinkState):
    __tdlib_type__ = "linkStateNone"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_localFile(LocalFile):
    __tdlib_type__ = "localFile"
    path:str = attr.ib()
    can_be_downloaded:bool = attr.ib()
    can_be_deleted:bool = attr.ib()
    is_downloading_active:bool = attr.ib()
    is_downloading_completed:bool = attr.ib()
    download_offset:int = attr.ib()
    downloaded_prefix_size:int = attr.ib()
    downloaded_size:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_localizationTargetInfo(LocalizationTargetInfo):
    __tdlib_type__ = "localizationTargetInfo"
    language_packs:typing.Sequence[languagePackInfo] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_location(Location):
    __tdlib_type__ = "location"
    latitude:decimal.Decimal = attr.ib()
    longitude:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_logStreamDefault(LogStream):
    __tdlib_type__ = "logStreamDefault"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_logStreamEmpty(LogStream):
    __tdlib_type__ = "logStreamEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_logStreamFile(LogStream):
    __tdlib_type__ = "logStreamFile"
    path:str = attr.ib()
    max_file_size:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_logTags(LogTags):
    __tdlib_type__ = "logTags"
    tags:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_logVerbosityLevel(LogVerbosityLevel):
    __tdlib_type__ = "logVerbosityLevel"
    verbosity_level:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_maskPointChin(MaskPoint):
    __tdlib_type__ = "maskPointChin"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_maskPointEyes(MaskPoint):
    __tdlib_type__ = "maskPointEyes"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_maskPointForehead(MaskPoint):
    __tdlib_type__ = "maskPointForehead"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_maskPointMouth(MaskPoint):
    __tdlib_type__ = "maskPointMouth"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_maskPosition(MaskPosition):
    __tdlib_type__ = "maskPosition"
    point:MaskPoint = attr.ib()
    x_shift:decimal.Decimal = attr.ib()
    y_shift:decimal.Decimal = attr.ib()
    scale:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_message(Message):
    __tdlib_type__ = "message"
    id:int = attr.ib()
    sender_user_id:int = attr.ib()
    chat_id:int = attr.ib()
    sending_state:MessageSendingState = attr.ib()
    is_outgoing:bool = attr.ib()
    can_be_edited:bool = attr.ib()
    can_be_forwarded:bool = attr.ib()
    can_be_deleted_only_for_self:bool = attr.ib()
    can_be_deleted_for_all_users:bool = attr.ib()
    is_channel_post:bool = attr.ib()
    contains_unread_mention:bool = attr.ib()
    date:int = attr.ib()
    edit_date:int = attr.ib()
    forward_info:messageForwardInfo = attr.ib()
    reply_to_message_id:int = attr.ib()
    ttl:int = attr.ib()
    ttl_expires_in:decimal.Decimal = attr.ib()
    via_bot_user_id:int = attr.ib()
    author_signature:str = attr.ib()
    views:int = attr.ib()
    media_album_id:int = attr.ib()
    content:MessageContent = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageAnimation(MessageContent):
    __tdlib_type__ = "messageAnimation"
    animation:animation = attr.ib()
    caption:formattedText = attr.ib()
    is_secret:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageAudio(MessageContent):
    __tdlib_type__ = "messageAudio"
    audio:audio = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageBasicGroupChatCreate(MessageContent):
    __tdlib_type__ = "messageBasicGroupChatCreate"
    title:str = attr.ib()
    member_user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageCall(MessageContent):
    __tdlib_type__ = "messageCall"
    discard_reason:CallDiscardReason = attr.ib()
    duration:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatAddMembers(MessageContent):
    __tdlib_type__ = "messageChatAddMembers"
    member_user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatChangePhoto(MessageContent):
    __tdlib_type__ = "messageChatChangePhoto"
    photo:photo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatChangeTitle(MessageContent):
    __tdlib_type__ = "messageChatChangeTitle"
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatDeleteMember(MessageContent):
    __tdlib_type__ = "messageChatDeleteMember"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatDeletePhoto(MessageContent):
    __tdlib_type__ = "messageChatDeletePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatJoinByLink(MessageContent):
    __tdlib_type__ = "messageChatJoinByLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatSetTtl(MessageContent):
    __tdlib_type__ = "messageChatSetTtl"
    ttl:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatUpgradeFrom(MessageContent):
    __tdlib_type__ = "messageChatUpgradeFrom"
    title:str = attr.ib()
    basic_group_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageChatUpgradeTo(MessageContent):
    __tdlib_type__ = "messageChatUpgradeTo"
    supergroup_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageContact(MessageContent):
    __tdlib_type__ = "messageContact"
    contact:contact = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageContactRegistered(MessageContent):
    __tdlib_type__ = "messageContactRegistered"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageCustomServiceAction(MessageContent):
    __tdlib_type__ = "messageCustomServiceAction"
    text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageDocument(MessageContent):
    __tdlib_type__ = "messageDocument"
    document:document = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageExpiredPhoto(MessageContent):
    __tdlib_type__ = "messageExpiredPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageExpiredVideo(MessageContent):
    __tdlib_type__ = "messageExpiredVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageForwardInfo(MessageForwardInfo):
    __tdlib_type__ = "messageForwardInfo"
    origin:MessageForwardOrigin = attr.ib()
    date:int = attr.ib()
    from_chat_id:int = attr.ib()
    from_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageForwardOriginChannel(MessageForwardOrigin):
    __tdlib_type__ = "messageForwardOriginChannel"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    author_signature:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageForwardOriginHiddenUser(MessageForwardOrigin):
    __tdlib_type__ = "messageForwardOriginHiddenUser"
    sender_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageForwardOriginUser(MessageForwardOrigin):
    __tdlib_type__ = "messageForwardOriginUser"
    sender_user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageGame(MessageContent):
    __tdlib_type__ = "messageGame"
    game:game = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageGameScore(MessageContent):
    __tdlib_type__ = "messageGameScore"
    game_message_id:int = attr.ib()
    game_id:int = attr.ib()
    score:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageInvoice(MessageContent):
    __tdlib_type__ = "messageInvoice"
    title:str = attr.ib()
    description:str = attr.ib()
    photo:photo = attr.ib()
    currency:str = attr.ib()
    total_amount:int = attr.ib()
    start_parameter:str = attr.ib()
    is_test:bool = attr.ib()
    need_shipping_address:bool = attr.ib()
    receipt_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageLinkInfo(MessageLinkInfo):
    __tdlib_type__ = "messageLinkInfo"
    is_public:bool = attr.ib()
    chat_id:int = attr.ib()
    message:message = attr.ib()
    for_album:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageLocation(MessageContent):
    __tdlib_type__ = "messageLocation"
    location:location = attr.ib()
    live_period:int = attr.ib()
    expires_in:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePassportDataReceived(MessageContent):
    __tdlib_type__ = "messagePassportDataReceived"
    elements:typing.Sequence[encryptedPassportElement] = attr.ib()
    credentials:encryptedCredentials = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePassportDataSent(MessageContent):
    __tdlib_type__ = "messagePassportDataSent"
    types:typing.Sequence[PassportElementType] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePaymentSuccessful(MessageContent):
    __tdlib_type__ = "messagePaymentSuccessful"
    invoice_message_id:int = attr.ib()
    currency:str = attr.ib()
    total_amount:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePaymentSuccessfulBot(MessageContent):
    __tdlib_type__ = "messagePaymentSuccessfulBot"
    invoice_message_id:int = attr.ib()
    currency:str = attr.ib()
    total_amount:int = attr.ib()
    invoice_payload:bytes = attr.ib()
    shipping_option_id:str = attr.ib()
    order_info:orderInfo = attr.ib()
    telegram_payment_charge_id:str = attr.ib()
    provider_payment_charge_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePhoto(MessageContent):
    __tdlib_type__ = "messagePhoto"
    photo:photo = attr.ib()
    caption:formattedText = attr.ib()
    is_secret:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePinMessage(MessageContent):
    __tdlib_type__ = "messagePinMessage"
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messagePoll(MessageContent):
    __tdlib_type__ = "messagePoll"
    poll:poll = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageScreenshotTaken(MessageContent):
    __tdlib_type__ = "messageScreenshotTaken"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageSendingStateFailed(MessageSendingState):
    __tdlib_type__ = "messageSendingStateFailed"
    error_code:int = attr.ib()
    error_message:str = attr.ib()
    can_retry:bool = attr.ib()
    retry_after:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageSendingStatePending(MessageSendingState):
    __tdlib_type__ = "messageSendingStatePending"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageSticker(MessageContent):
    __tdlib_type__ = "messageSticker"
    sticker:sticker = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageSupergroupChatCreate(MessageContent):
    __tdlib_type__ = "messageSupergroupChatCreate"
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageText(MessageContent):
    __tdlib_type__ = "messageText"
    text:formattedText = attr.ib()
    web_page:webPage = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageUnsupported(MessageContent):
    __tdlib_type__ = "messageUnsupported"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageVenue(MessageContent):
    __tdlib_type__ = "messageVenue"
    venue:venue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageVideo(MessageContent):
    __tdlib_type__ = "messageVideo"
    video:video = attr.ib()
    caption:formattedText = attr.ib()
    is_secret:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageVideoNote(MessageContent):
    __tdlib_type__ = "messageVideoNote"
    video_note:videoNote = attr.ib()
    is_viewed:bool = attr.ib()
    is_secret:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageVoiceNote(MessageContent):
    __tdlib_type__ = "messageVoiceNote"
    voice_note:voiceNote = attr.ib()
    caption:formattedText = attr.ib()
    is_listened:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messageWebsiteConnected(MessageContent):
    __tdlib_type__ = "messageWebsiteConnected"
    domain_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_messages(Messages):
    __tdlib_type__ = "messages"
    total_count:int = attr.ib()
    messages:typing.Sequence[message] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_minithumbnail(Minithumbnail):
    __tdlib_type__ = "minithumbnail"
    width:int = attr.ib()
    height:int = attr.ib()
    data:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkStatistics(NetworkStatistics):
    __tdlib_type__ = "networkStatistics"
    since_date:int = attr.ib()
    entries:typing.Sequence[NetworkStatisticsEntry] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkStatisticsEntryCall(NetworkStatisticsEntry):
    __tdlib_type__ = "networkStatisticsEntryCall"
    network_type:NetworkType = attr.ib()
    sent_bytes:int = attr.ib()
    received_bytes:int = attr.ib()
    duration:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkStatisticsEntryFile(NetworkStatisticsEntry):
    __tdlib_type__ = "networkStatisticsEntryFile"
    file_type:FileType = attr.ib()
    network_type:NetworkType = attr.ib()
    sent_bytes:int = attr.ib()
    received_bytes:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkTypeMobile(NetworkType):
    __tdlib_type__ = "networkTypeMobile"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkTypeMobileRoaming(NetworkType):
    __tdlib_type__ = "networkTypeMobileRoaming"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkTypeNone(NetworkType):
    __tdlib_type__ = "networkTypeNone"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkTypeOther(NetworkType):
    __tdlib_type__ = "networkTypeOther"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_networkTypeWiFi(NetworkType):
    __tdlib_type__ = "networkTypeWiFi"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notification(Notification):
    __tdlib_type__ = "notification"
    id:int = attr.ib()
    date:int = attr.ib()
    is_silent:bool = attr.ib()
    type:NotificationType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationGroup(NotificationGroup):
    __tdlib_type__ = "notificationGroup"
    id:int = attr.ib()
    type:NotificationGroupType = attr.ib()
    chat_id:int = attr.ib()
    total_count:int = attr.ib()
    notifications:typing.Sequence[notification] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationGroupTypeCalls(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationGroupTypeMentions(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeMentions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationGroupTypeMessages(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationGroupTypeSecretChat(NotificationGroupType):
    __tdlib_type__ = "notificationGroupTypeSecretChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationSettingsScopeChannelChats(NotificationSettingsScope):
    __tdlib_type__ = "notificationSettingsScopeChannelChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationSettingsScopeGroupChats(NotificationSettingsScope):
    __tdlib_type__ = "notificationSettingsScopeGroupChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationSettingsScopePrivateChats(NotificationSettingsScope):
    __tdlib_type__ = "notificationSettingsScopePrivateChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationTypeNewCall(NotificationType):
    __tdlib_type__ = "notificationTypeNewCall"
    call_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationTypeNewMessage(NotificationType):
    __tdlib_type__ = "notificationTypeNewMessage"
    message:message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationTypeNewPushMessage(NotificationType):
    __tdlib_type__ = "notificationTypeNewPushMessage"
    message_id:int = attr.ib()
    sender_user_id:int = attr.ib()
    content:PushMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_notificationTypeNewSecretChat(NotificationType):
    __tdlib_type__ = "notificationTypeNewSecretChat"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_ok(Ok):
    __tdlib_type__ = "ok"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_optionValueBoolean(OptionValue):
    __tdlib_type__ = "optionValueBoolean"
    value:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_optionValueEmpty(OptionValue):
    __tdlib_type__ = "optionValueEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_optionValueInteger(OptionValue):
    __tdlib_type__ = "optionValueInteger"
    value:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_optionValueString(OptionValue):
    __tdlib_type__ = "optionValueString"
    value:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_orderInfo(OrderInfo):
    __tdlib_type__ = "orderInfo"
    name:str = attr.ib()
    phone_number:str = attr.ib()
    email_address:str = attr.ib()
    shipping_address:address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockAnchor(PageBlock):
    __tdlib_type__ = "pageBlockAnchor"
    name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockAnimation(PageBlock):
    __tdlib_type__ = "pageBlockAnimation"
    animation:animation = attr.ib()
    caption:pageBlockCaption = attr.ib()
    need_autoplay:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockAudio(PageBlock):
    __tdlib_type__ = "pageBlockAudio"
    audio:audio = attr.ib()
    caption:pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockAuthorDate(PageBlock):
    __tdlib_type__ = "pageBlockAuthorDate"
    author:RichText = attr.ib()
    publish_date:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockBlockQuote(PageBlock):
    __tdlib_type__ = "pageBlockBlockQuote"
    text:RichText = attr.ib()
    credit:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockCaption(PageBlockCaption):
    __tdlib_type__ = "pageBlockCaption"
    text:RichText = attr.ib()
    credit:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockChatLink(PageBlock):
    __tdlib_type__ = "pageBlockChatLink"
    title:str = attr.ib()
    photo:chatPhoto = attr.ib()
    username:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockCollage(PageBlock):
    __tdlib_type__ = "pageBlockCollage"
    page_blocks:typing.Sequence[PageBlock] = attr.ib()
    caption:pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockCover(PageBlock):
    __tdlib_type__ = "pageBlockCover"
    cover:PageBlock = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockDetails(PageBlock):
    __tdlib_type__ = "pageBlockDetails"
    header:RichText = attr.ib()
    page_blocks:typing.Sequence[PageBlock] = attr.ib()
    is_open:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockDivider(PageBlock):
    __tdlib_type__ = "pageBlockDivider"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockEmbedded(PageBlock):
    __tdlib_type__ = "pageBlockEmbedded"
    url:str = attr.ib()
    html:str = attr.ib()
    poster_photo:photo = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    caption:pageBlockCaption = attr.ib()
    is_full_width:bool = attr.ib()
    allow_scrolling:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockEmbeddedPost(PageBlock):
    __tdlib_type__ = "pageBlockEmbeddedPost"
    url:str = attr.ib()
    author:str = attr.ib()
    author_photo:photo = attr.ib()
    date:int = attr.ib()
    page_blocks:typing.Sequence[PageBlock] = attr.ib()
    caption:pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockFooter(PageBlock):
    __tdlib_type__ = "pageBlockFooter"
    footer:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockHeader(PageBlock):
    __tdlib_type__ = "pageBlockHeader"
    header:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockHorizontalAlignmentCenter(PageBlockHorizontalAlignment):
    __tdlib_type__ = "pageBlockHorizontalAlignmentCenter"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockHorizontalAlignmentLeft(PageBlockHorizontalAlignment):
    __tdlib_type__ = "pageBlockHorizontalAlignmentLeft"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockHorizontalAlignmentRight(PageBlockHorizontalAlignment):
    __tdlib_type__ = "pageBlockHorizontalAlignmentRight"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockKicker(PageBlock):
    __tdlib_type__ = "pageBlockKicker"
    kicker:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockList(PageBlock):
    __tdlib_type__ = "pageBlockList"
    items:typing.Sequence[pageBlockListItem] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockListItem(PageBlockListItem):
    __tdlib_type__ = "pageBlockListItem"
    label:str = attr.ib()
    page_blocks:typing.Sequence[PageBlock] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockMap(PageBlock):
    __tdlib_type__ = "pageBlockMap"
    location:location = attr.ib()
    zoom:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    caption:pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockParagraph(PageBlock):
    __tdlib_type__ = "pageBlockParagraph"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockPhoto(PageBlock):
    __tdlib_type__ = "pageBlockPhoto"
    photo:photo = attr.ib()
    caption:pageBlockCaption = attr.ib()
    url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockPreformatted(PageBlock):
    __tdlib_type__ = "pageBlockPreformatted"
    text:RichText = attr.ib()
    language:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockPullQuote(PageBlock):
    __tdlib_type__ = "pageBlockPullQuote"
    text:RichText = attr.ib()
    credit:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockRelatedArticle(PageBlockRelatedArticle):
    __tdlib_type__ = "pageBlockRelatedArticle"
    url:str = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    photo:photo = attr.ib()
    author:str = attr.ib()
    publish_date:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockRelatedArticles(PageBlock):
    __tdlib_type__ = "pageBlockRelatedArticles"
    header:RichText = attr.ib()
    articles:typing.Sequence[pageBlockRelatedArticle] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockSlideshow(PageBlock):
    __tdlib_type__ = "pageBlockSlideshow"
    page_blocks:typing.Sequence[PageBlock] = attr.ib()
    caption:pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockSubheader(PageBlock):
    __tdlib_type__ = "pageBlockSubheader"
    subheader:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockSubtitle(PageBlock):
    __tdlib_type__ = "pageBlockSubtitle"
    subtitle:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockTable(PageBlock):
    __tdlib_type__ = "pageBlockTable"
    caption:RichText = attr.ib()
    cells:typing.Sequence[vector<pageBlockTableCell>] = attr.ib()
    is_bordered:bool = attr.ib()
    is_striped:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockTableCell(PageBlockTableCell):
    __tdlib_type__ = "pageBlockTableCell"
    text:RichText = attr.ib()
    is_header:bool = attr.ib()
    colspan:int = attr.ib()
    rowspan:int = attr.ib()
    align:PageBlockHorizontalAlignment = attr.ib()
    valign:PageBlockVerticalAlignment = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockTitle(PageBlock):
    __tdlib_type__ = "pageBlockTitle"
    title:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockVerticalAlignmentBottom(PageBlockVerticalAlignment):
    __tdlib_type__ = "pageBlockVerticalAlignmentBottom"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockVerticalAlignmentMiddle(PageBlockVerticalAlignment):
    __tdlib_type__ = "pageBlockVerticalAlignmentMiddle"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockVerticalAlignmentTop(PageBlockVerticalAlignment):
    __tdlib_type__ = "pageBlockVerticalAlignmentTop"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockVideo(PageBlock):
    __tdlib_type__ = "pageBlockVideo"
    video:video = attr.ib()
    caption:pageBlockCaption = attr.ib()
    need_autoplay:bool = attr.ib()
    is_looped:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pageBlockVoiceNote(PageBlock):
    __tdlib_type__ = "pageBlockVoiceNote"
    voice_note:voiceNote = attr.ib()
    caption:pageBlockCaption = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportAuthorizationForm(PassportAuthorizationForm):
    __tdlib_type__ = "passportAuthorizationForm"
    id:int = attr.ib()
    required_elements:typing.Sequence[passportRequiredElement] = attr.ib()
    privacy_policy_url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementAddress(PassportElement):
    __tdlib_type__ = "passportElementAddress"
    address:address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementBankStatement(PassportElement):
    __tdlib_type__ = "passportElementBankStatement"
    bank_statement:personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementDriverLicense(PassportElement):
    __tdlib_type__ = "passportElementDriverLicense"
    driver_license:identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementEmailAddress(PassportElement):
    __tdlib_type__ = "passportElementEmailAddress"
    email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementError(PassportElementError):
    __tdlib_type__ = "passportElementError"
    type:PassportElementType = attr.ib()
    message:str = attr.ib()
    source:PassportElementErrorSource = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceDataField(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceDataField"
    field_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceFile(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceFile"
    file_index:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceFiles(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceFiles"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceFrontSide(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceFrontSide"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceReverseSide(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceReverseSide"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceSelfie(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceSelfie"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceTranslationFile(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceTranslationFile"
    file_index:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceTranslationFiles(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceTranslationFiles"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementErrorSourceUnspecified(PassportElementErrorSource):
    __tdlib_type__ = "passportElementErrorSourceUnspecified"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementIdentityCard(PassportElement):
    __tdlib_type__ = "passportElementIdentityCard"
    identity_card:identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementInternalPassport(PassportElement):
    __tdlib_type__ = "passportElementInternalPassport"
    internal_passport:identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementPassport(PassportElement):
    __tdlib_type__ = "passportElementPassport"
    passport:identityDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementPassportRegistration(PassportElement):
    __tdlib_type__ = "passportElementPassportRegistration"
    passport_registration:personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementPersonalDetails(PassportElement):
    __tdlib_type__ = "passportElementPersonalDetails"
    personal_details:personalDetails = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementPhoneNumber(PassportElement):
    __tdlib_type__ = "passportElementPhoneNumber"
    phone_number:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementRentalAgreement(PassportElement):
    __tdlib_type__ = "passportElementRentalAgreement"
    rental_agreement:personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTemporaryRegistration(PassportElement):
    __tdlib_type__ = "passportElementTemporaryRegistration"
    temporary_registration:personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeAddress(PassportElementType):
    __tdlib_type__ = "passportElementTypeAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeBankStatement(PassportElementType):
    __tdlib_type__ = "passportElementTypeBankStatement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeDriverLicense(PassportElementType):
    __tdlib_type__ = "passportElementTypeDriverLicense"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeEmailAddress(PassportElementType):
    __tdlib_type__ = "passportElementTypeEmailAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeIdentityCard(PassportElementType):
    __tdlib_type__ = "passportElementTypeIdentityCard"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeInternalPassport(PassportElementType):
    __tdlib_type__ = "passportElementTypeInternalPassport"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypePassport(PassportElementType):
    __tdlib_type__ = "passportElementTypePassport"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypePassportRegistration(PassportElementType):
    __tdlib_type__ = "passportElementTypePassportRegistration"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypePersonalDetails(PassportElementType):
    __tdlib_type__ = "passportElementTypePersonalDetails"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypePhoneNumber(PassportElementType):
    __tdlib_type__ = "passportElementTypePhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeRentalAgreement(PassportElementType):
    __tdlib_type__ = "passportElementTypeRentalAgreement"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeTemporaryRegistration(PassportElementType):
    __tdlib_type__ = "passportElementTypeTemporaryRegistration"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementTypeUtilityBill(PassportElementType):
    __tdlib_type__ = "passportElementTypeUtilityBill"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementUtilityBill(PassportElement):
    __tdlib_type__ = "passportElementUtilityBill"
    utility_bill:personalDocument = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElements(PassportElements):
    __tdlib_type__ = "passportElements"
    elements:typing.Sequence[PassportElement] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportElementsWithErrors(PassportElementsWithErrors):
    __tdlib_type__ = "passportElementsWithErrors"
    elements:typing.Sequence[PassportElement] = attr.ib()
    errors:typing.Sequence[passportElementError] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportRequiredElement(PassportRequiredElement):
    __tdlib_type__ = "passportRequiredElement"
    suitable_elements:typing.Sequence[passportSuitableElement] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passportSuitableElement(PassportSuitableElement):
    __tdlib_type__ = "passportSuitableElement"
    type:PassportElementType = attr.ib()
    is_selfie_required:bool = attr.ib()
    is_translation_required:bool = attr.ib()
    is_native_name_required:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_passwordState(PasswordState):
    __tdlib_type__ = "passwordState"
    has_password:bool = attr.ib()
    password_hint:str = attr.ib()
    has_recovery_email_address:bool = attr.ib()
    has_passport_data:bool = attr.ib()
    recovery_email_address_code_info:emailAddressAuthenticationCodeInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_paymentForm(PaymentForm):
    __tdlib_type__ = "paymentForm"
    invoice:invoice = attr.ib()
    url:str = attr.ib()
    payments_provider:paymentsProviderStripe = attr.ib()
    saved_order_info:orderInfo = attr.ib()
    saved_credentials:savedCredentials = attr.ib()
    can_save_credentials:bool = attr.ib()
    need_password:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_paymentReceipt(PaymentReceipt):
    __tdlib_type__ = "paymentReceipt"
    date:int = attr.ib()
    payments_provider_user_id:int = attr.ib()
    invoice:invoice = attr.ib()
    order_info:orderInfo = attr.ib()
    shipping_option:shippingOption = attr.ib()
    credentials_title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_paymentResult(PaymentResult):
    __tdlib_type__ = "paymentResult"
    success:bool = attr.ib()
    verification_url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_paymentsProviderStripe(PaymentsProviderStripe):
    __tdlib_type__ = "paymentsProviderStripe"
    publishable_key:str = attr.ib()
    need_country:bool = attr.ib()
    need_postal_code:bool = attr.ib()
    need_cardholder_name:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_personalDetails(PersonalDetails):
    __tdlib_type__ = "personalDetails"
    first_name:str = attr.ib()
    middle_name:str = attr.ib()
    last_name:str = attr.ib()
    native_first_name:str = attr.ib()
    native_middle_name:str = attr.ib()
    native_last_name:str = attr.ib()
    birthdate:date = attr.ib()
    gender:str = attr.ib()
    country_code:str = attr.ib()
    residence_country_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_personalDocument(PersonalDocument):
    __tdlib_type__ = "personalDocument"
    files:typing.Sequence[datedFile] = attr.ib()
    translation:typing.Sequence[datedFile] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_phoneNumberAuthenticationSettings(PhoneNumberAuthenticationSettings):
    __tdlib_type__ = "phoneNumberAuthenticationSettings"
    allow_flash_call:bool = attr.ib()
    is_current_phone_number:bool = attr.ib()
    allow_sms_retriever_api:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_photo(Photo):
    __tdlib_type__ = "photo"
    has_stickers:bool = attr.ib()
    minithumbnail:minithumbnail = attr.ib()
    sizes:typing.Sequence[photoSize] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_photoSize(PhotoSize):
    __tdlib_type__ = "photoSize"
    type:str = attr.ib()
    photo:file = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_poll(Poll):
    __tdlib_type__ = "poll"
    id:int = attr.ib()
    question:str = attr.ib()
    options:typing.Sequence[pollOption] = attr.ib()
    total_voter_count:int = attr.ib()
    is_closed:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pollOption(PollOption):
    __tdlib_type__ = "pollOption"
    text:str = attr.ib()
    voter_count:int = attr.ib()
    vote_percentage:int = attr.ib()
    is_chosen:bool = attr.ib()
    is_being_chosen:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_profilePhoto(ProfilePhoto):
    __tdlib_type__ = "profilePhoto"
    id:int = attr.ib()
    small:file = attr.ib()
    big:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_proxies(Proxies):
    __tdlib_type__ = "proxies"
    proxies:typing.Sequence[proxy] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_proxy(Proxy):
    __tdlib_type__ = "proxy"
    id:int = attr.ib()
    server:str = attr.ib()
    port:int = attr.ib()
    last_used_date:int = attr.ib()
    is_enabled:bool = attr.ib()
    type:ProxyType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_proxyTypeHttp(ProxyType):
    __tdlib_type__ = "proxyTypeHttp"
    username:str = attr.ib()
    password:str = attr.ib()
    http_only:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_proxyTypeMtproto(ProxyType):
    __tdlib_type__ = "proxyTypeMtproto"
    secret:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_proxyTypeSocks5(ProxyType):
    __tdlib_type__ = "proxyTypeSocks5"
    username:str = attr.ib()
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_publicMessageLink(PublicMessageLink):
    __tdlib_type__ = "publicMessageLink"
    link:str = attr.ib()
    html:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentAnimation(PushMessageContent):
    __tdlib_type__ = "pushMessageContentAnimation"
    animation:animation = attr.ib()
    caption:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentAudio(PushMessageContent):
    __tdlib_type__ = "pushMessageContentAudio"
    audio:audio = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentBasicGroupChatCreate(PushMessageContent):
    __tdlib_type__ = "pushMessageContentBasicGroupChatCreate"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentChatAddMembers(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatAddMembers"
    member_name:str = attr.ib()
    is_current_user:bool = attr.ib()
    is_returned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentChatChangePhoto(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatChangePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentChatChangeTitle(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatChangeTitle"
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentChatDeleteMember(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatDeleteMember"
    member_name:str = attr.ib()
    is_current_user:bool = attr.ib()
    is_left:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentChatJoinByLink(PushMessageContent):
    __tdlib_type__ = "pushMessageContentChatJoinByLink"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentContact(PushMessageContent):
    __tdlib_type__ = "pushMessageContentContact"
    name:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentContactRegistered(PushMessageContent):
    __tdlib_type__ = "pushMessageContentContactRegistered"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentDocument(PushMessageContent):
    __tdlib_type__ = "pushMessageContentDocument"
    document:document = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentGame(PushMessageContent):
    __tdlib_type__ = "pushMessageContentGame"
    title:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentGameScore(PushMessageContent):
    __tdlib_type__ = "pushMessageContentGameScore"
    title:str = attr.ib()
    score:int = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentHidden(PushMessageContent):
    __tdlib_type__ = "pushMessageContentHidden"
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentInvoice(PushMessageContent):
    __tdlib_type__ = "pushMessageContentInvoice"
    price:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentLocation(PushMessageContent):
    __tdlib_type__ = "pushMessageContentLocation"
    is_live:bool = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentMediaAlbum(PushMessageContent):
    __tdlib_type__ = "pushMessageContentMediaAlbum"
    total_count:int = attr.ib()
    has_photos:bool = attr.ib()
    has_videos:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentMessageForwards(PushMessageContent):
    __tdlib_type__ = "pushMessageContentMessageForwards"
    total_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentPhoto(PushMessageContent):
    __tdlib_type__ = "pushMessageContentPhoto"
    photo:photo = attr.ib()
    caption:str = attr.ib()
    is_secret:bool = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentPoll(PushMessageContent):
    __tdlib_type__ = "pushMessageContentPoll"
    question:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentScreenshotTaken(PushMessageContent):
    __tdlib_type__ = "pushMessageContentScreenshotTaken"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentSticker(PushMessageContent):
    __tdlib_type__ = "pushMessageContentSticker"
    sticker:sticker = attr.ib()
    emoji:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentText(PushMessageContent):
    __tdlib_type__ = "pushMessageContentText"
    text:str = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentVideo(PushMessageContent):
    __tdlib_type__ = "pushMessageContentVideo"
    video:video = attr.ib()
    caption:str = attr.ib()
    is_secret:bool = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentVideoNote(PushMessageContent):
    __tdlib_type__ = "pushMessageContentVideoNote"
    video_note:videoNote = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushMessageContentVoiceNote(PushMessageContent):
    __tdlib_type__ = "pushMessageContentVoiceNote"
    voice_note:voiceNote = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_pushReceiverId(PushReceiverId):
    __tdlib_type__ = "pushReceiverId"
    id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_recoveryEmailAddress(RecoveryEmailAddress):
    __tdlib_type__ = "recoveryEmailAddress"
    recovery_email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_remoteFile(RemoteFile):
    __tdlib_type__ = "remoteFile"
    id:str = attr.ib()
    is_uploading_active:bool = attr.ib()
    is_uploading_completed:bool = attr.ib()
    uploaded_size:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_replyMarkupForceReply(ReplyMarkup):
    __tdlib_type__ = "replyMarkupForceReply"
    is_personal:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_replyMarkupInlineKeyboard(ReplyMarkup):
    __tdlib_type__ = "replyMarkupInlineKeyboard"
    rows:typing.Sequence[vector<inlineKeyboardButton>] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_replyMarkupRemoveKeyboard(ReplyMarkup):
    __tdlib_type__ = "replyMarkupRemoveKeyboard"
    is_personal:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_replyMarkupShowKeyboard(ReplyMarkup):
    __tdlib_type__ = "replyMarkupShowKeyboard"
    rows:typing.Sequence[vector<keyboardButton>] = attr.ib()
    resize_keyboard:bool = attr.ib()
    one_time:bool = attr.ib()
    is_personal:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextAnchor(RichText):
    __tdlib_type__ = "richTextAnchor"
    text:RichText = attr.ib()
    name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextBold(RichText):
    __tdlib_type__ = "richTextBold"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextEmailAddress(RichText):
    __tdlib_type__ = "richTextEmailAddress"
    text:RichText = attr.ib()
    email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextFixed(RichText):
    __tdlib_type__ = "richTextFixed"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextIcon(RichText):
    __tdlib_type__ = "richTextIcon"
    document:document = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextItalic(RichText):
    __tdlib_type__ = "richTextItalic"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextMarked(RichText):
    __tdlib_type__ = "richTextMarked"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextPhoneNumber(RichText):
    __tdlib_type__ = "richTextPhoneNumber"
    text:RichText = attr.ib()
    phone_number:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextPlain(RichText):
    __tdlib_type__ = "richTextPlain"
    text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextStrikethrough(RichText):
    __tdlib_type__ = "richTextStrikethrough"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextSubscript(RichText):
    __tdlib_type__ = "richTextSubscript"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextSuperscript(RichText):
    __tdlib_type__ = "richTextSuperscript"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextUnderline(RichText):
    __tdlib_type__ = "richTextUnderline"
    text:RichText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTextUrl(RichText):
    __tdlib_type__ = "richTextUrl"
    text:RichText = attr.ib()
    url:str = attr.ib()
    is_cached:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_richTexts(RichText):
    __tdlib_type__ = "richTexts"
    texts:typing.Sequence[RichText] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_savedCredentials(SavedCredentials):
    __tdlib_type__ = "savedCredentials"
    id:str = attr.ib()
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_scopeNotificationSettings(ScopeNotificationSettings):
    __tdlib_type__ = "scopeNotificationSettings"
    mute_for:int = attr.ib()
    sound:str = attr.ib()
    show_preview:bool = attr.ib()
    disable_pinned_message_notifications:bool = attr.ib()
    disable_mention_notifications:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterAnimation(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterAnimation"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterAudio(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterAudio"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterCall(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterCall"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterChatPhoto(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterChatPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterDocument(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterDocument"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterEmpty(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterMention(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterMention"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterMissedCall(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterMissedCall"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterPhoto(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterPhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterPhotoAndVideo(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterPhotoAndVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterUnreadMention(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterUnreadMention"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterUrl(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterVideo(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVideo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterVideoNote(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterVoiceAndVideoNote(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVoiceAndVideoNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_searchMessagesFilterVoiceNote(SearchMessagesFilter):
    __tdlib_type__ = "searchMessagesFilterVoiceNote"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_seconds(Seconds):
    __tdlib_type__ = "seconds"
    seconds:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_secretChat(SecretChat):
    __tdlib_type__ = "secretChat"
    id:int = attr.ib()
    user_id:int = attr.ib()
    state:SecretChatState = attr.ib()
    is_outbound:bool = attr.ib()
    ttl:int = attr.ib()
    key_hash:bytes = attr.ib()
    layer:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_secretChatStateClosed(SecretChatState):
    __tdlib_type__ = "secretChatStateClosed"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_secretChatStatePending(SecretChatState):
    __tdlib_type__ = "secretChatStatePending"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_secretChatStateReady(SecretChatState):
    __tdlib_type__ = "secretChatStateReady"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_session(Session):
    __tdlib_type__ = "session"
    id:int = attr.ib()
    is_current:bool = attr.ib()
    is_password_pending:bool = attr.ib()
    api_id:int = attr.ib()
    application_name:str = attr.ib()
    application_version:str = attr.ib()
    is_official_application:bool = attr.ib()
    device_model:str = attr.ib()
    platform:str = attr.ib()
    system_version:str = attr.ib()
    log_in_date:int = attr.ib()
    last_active_date:int = attr.ib()
    ip:str = attr.ib()
    country:str = attr.ib()
    region:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_sessions(Sessions):
    __tdlib_type__ = "sessions"
    sessions:typing.Sequence[session] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_shippingOption(ShippingOption):
    __tdlib_type__ = "shippingOption"
    id:str = attr.ib()
    title:str = attr.ib()
    price_parts:typing.Sequence[labeledPricePart] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_sticker(Sticker):
    __tdlib_type__ = "sticker"
    set_id:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    emoji:str = attr.ib()
    is_animated:bool = attr.ib()
    is_mask:bool = attr.ib()
    mask_position:maskPosition = attr.ib()
    thumbnail:photoSize = attr.ib()
    sticker:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_stickerSet(StickerSet):
    __tdlib_type__ = "stickerSet"
    id:int = attr.ib()
    title:str = attr.ib()
    name:str = attr.ib()
    thumbnail:photoSize = attr.ib()
    is_installed:bool = attr.ib()
    is_archived:bool = attr.ib()
    is_official:bool = attr.ib()
    is_animated:bool = attr.ib()
    is_masks:bool = attr.ib()
    is_viewed:bool = attr.ib()
    stickers:typing.Sequence[sticker] = attr.ib()
    emojis:typing.Sequence[emojis] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_stickerSetInfo(StickerSetInfo):
    __tdlib_type__ = "stickerSetInfo"
    id:int = attr.ib()
    title:str = attr.ib()
    name:str = attr.ib()
    thumbnail:photoSize = attr.ib()
    is_installed:bool = attr.ib()
    is_archived:bool = attr.ib()
    is_official:bool = attr.ib()
    is_animated:bool = attr.ib()
    is_masks:bool = attr.ib()
    is_viewed:bool = attr.ib()
    size:int = attr.ib()
    covers:typing.Sequence[sticker] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_stickerSets(StickerSets):
    __tdlib_type__ = "stickerSets"
    total_count:int = attr.ib()
    sets:typing.Sequence[stickerSetInfo] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_stickers(Stickers):
    __tdlib_type__ = "stickers"
    stickers:typing.Sequence[sticker] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_storageStatistics(StorageStatistics):
    __tdlib_type__ = "storageStatistics"
    size:int = attr.ib()
    count:int = attr.ib()
    by_chat:typing.Sequence[storageStatisticsByChat] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_storageStatisticsByChat(StorageStatisticsByChat):
    __tdlib_type__ = "storageStatisticsByChat"
    chat_id:int = attr.ib()
    size:int = attr.ib()
    count:int = attr.ib()
    by_file_type:typing.Sequence[storageStatisticsByFileType] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_storageStatisticsByFileType(StorageStatisticsByFileType):
    __tdlib_type__ = "storageStatisticsByFileType"
    file_type:FileType = attr.ib()
    size:int = attr.ib()
    count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_storageStatisticsFast(StorageStatisticsFast):
    __tdlib_type__ = "storageStatisticsFast"
    files_size:int = attr.ib()
    file_count:int = attr.ib()
    database_size:int = attr.ib()
    language_pack_database_size:int = attr.ib()
    log_size:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroup(Supergroup):
    __tdlib_type__ = "supergroup"
    id:int = attr.ib()
    username:str = attr.ib()
    date:int = attr.ib()
    status:ChatMemberStatus = attr.ib()
    member_count:int = attr.ib()
    sign_messages:bool = attr.ib()
    is_channel:bool = attr.ib()
    is_verified:bool = attr.ib()
    restriction_reason:str = attr.ib()
    is_scam:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupFullInfo(SupergroupFullInfo):
    __tdlib_type__ = "supergroupFullInfo"
    description:str = attr.ib()
    member_count:int = attr.ib()
    administrator_count:int = attr.ib()
    restricted_count:int = attr.ib()
    banned_count:int = attr.ib()
    can_get_members:bool = attr.ib()
    can_set_username:bool = attr.ib()
    can_set_sticker_set:bool = attr.ib()
    can_view_statistics:bool = attr.ib()
    is_all_history_available:bool = attr.ib()
    sticker_set_id:int = attr.ib()
    invite_link:str = attr.ib()
    upgraded_from_basic_group_id:int = attr.ib()
    upgraded_from_max_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterAdministrators(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterAdministrators"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterBanned(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterBanned"
    query:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterBots(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterContacts(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterContacts"
    query:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterRecent(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterRecent"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterRestricted(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterRestricted"
    query:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_supergroupMembersFilterSearch(SupergroupMembersFilter):
    __tdlib_type__ = "supergroupMembersFilterSearch"
    query:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tMeUrl(TMeUrl):
    __tdlib_type__ = "tMeUrl"
    url:str = attr.ib()
    type:TMeUrlType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tMeUrlTypeChatInvite(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeChatInvite"
    info:chatInviteLinkInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tMeUrlTypeStickerSet(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeStickerSet"
    sticker_set_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tMeUrlTypeSupergroup(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeSupergroup"
    supergroup_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tMeUrlTypeUser(TMeUrlType):
    __tdlib_type__ = "tMeUrlTypeUser"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tMeUrls(TMeUrls):
    __tdlib_type__ = "tMeUrls"
    urls:typing.Sequence[tMeUrl] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tdlibParameters(TdlibParameters):
    __tdlib_type__ = "tdlibParameters"
    use_test_dc:bool = attr.ib()
    database_directory:str = attr.ib()
    files_directory:str = attr.ib()
    use_file_database:bool = attr.ib()
    use_chat_info_database:bool = attr.ib()
    use_message_database:bool = attr.ib()
    use_secret_chats:bool = attr.ib()
    api_id:int = attr.ib()
    api_hash:str = attr.ib()
    system_language_code:str = attr.ib()
    device_model:str = attr.ib()
    system_version:str = attr.ib()
    application_version:str = attr.ib()
    enable_storage_optimizer:bool = attr.ib()
    ignore_file_names:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_temporaryPasswordState(TemporaryPasswordState):
    __tdlib_type__ = "temporaryPasswordState"
    has_password:bool = attr.ib()
    valid_for:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_termsOfService(TermsOfService):
    __tdlib_type__ = "termsOfService"
    text:formattedText = attr.ib()
    min_user_age:int = attr.ib()
    show_popup:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testBytes(TestBytes):
    __tdlib_type__ = "testBytes"
    value:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testInt(TestInt):
    __tdlib_type__ = "testInt"
    value:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testString(TestString):
    __tdlib_type__ = "testString"
    value:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testVectorInt(TestVectorInt):
    __tdlib_type__ = "testVectorInt"
    value:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testVectorIntObject(TestVectorIntObject):
    __tdlib_type__ = "testVectorIntObject"
    value:typing.Sequence[testInt] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testVectorString(TestVectorString):
    __tdlib_type__ = "testVectorString"
    value:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_testVectorStringObject(TestVectorStringObject):
    __tdlib_type__ = "testVectorStringObject"
    value:typing.Sequence[testString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_text(Text):
    __tdlib_type__ = "text"
    text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntities(TextEntities):
    __tdlib_type__ = "textEntities"
    entities:typing.Sequence[textEntity] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntity(TextEntity):
    __tdlib_type__ = "textEntity"
    offset:int = attr.ib()
    length:int = attr.ib()
    type:TextEntityType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeBold(TextEntityType):
    __tdlib_type__ = "textEntityTypeBold"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeBotCommand(TextEntityType):
    __tdlib_type__ = "textEntityTypeBotCommand"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeCashtag(TextEntityType):
    __tdlib_type__ = "textEntityTypeCashtag"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeCode(TextEntityType):
    __tdlib_type__ = "textEntityTypeCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeEmailAddress(TextEntityType):
    __tdlib_type__ = "textEntityTypeEmailAddress"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeHashtag(TextEntityType):
    __tdlib_type__ = "textEntityTypeHashtag"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeItalic(TextEntityType):
    __tdlib_type__ = "textEntityTypeItalic"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeMention(TextEntityType):
    __tdlib_type__ = "textEntityTypeMention"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeMentionName(TextEntityType):
    __tdlib_type__ = "textEntityTypeMentionName"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypePhoneNumber(TextEntityType):
    __tdlib_type__ = "textEntityTypePhoneNumber"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypePre(TextEntityType):
    __tdlib_type__ = "textEntityTypePre"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypePreCode(TextEntityType):
    __tdlib_type__ = "textEntityTypePreCode"
    language:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeTextUrl(TextEntityType):
    __tdlib_type__ = "textEntityTypeTextUrl"
    url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textEntityTypeUrl(TextEntityType):
    __tdlib_type__ = "textEntityTypeUrl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textParseModeHTML(TextParseMode):
    __tdlib_type__ = "textParseModeHTML"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_textParseModeMarkdown(TextParseMode):
    __tdlib_type__ = "textParseModeMarkdown"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tonLiteServerResponse(TonLiteServerResponse):
    __tdlib_type__ = "tonLiteServerResponse"
    response:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_tonWalletPasswordSalt(TonWalletPasswordSalt):
    __tdlib_type__ = "tonWalletPasswordSalt"
    salt:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_topChatCategoryBots(TopChatCategory):
    __tdlib_type__ = "topChatCategoryBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_topChatCategoryCalls(TopChatCategory):
    __tdlib_type__ = "topChatCategoryCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_topChatCategoryChannels(TopChatCategory):
    __tdlib_type__ = "topChatCategoryChannels"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_topChatCategoryGroups(TopChatCategory):
    __tdlib_type__ = "topChatCategoryGroups"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_topChatCategoryInlineBots(TopChatCategory):
    __tdlib_type__ = "topChatCategoryInlineBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_topChatCategoryUsers(TopChatCategory):
    __tdlib_type__ = "topChatCategoryUsers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateActiveNotifications(Update):
    __tdlib_type__ = "updateActiveNotifications"
    groups:typing.Sequence[notificationGroup] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateAuthorizationState(Update):
    __tdlib_type__ = "updateAuthorizationState"
    authorization_state:AuthorizationState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateBasicGroup(Update):
    __tdlib_type__ = "updateBasicGroup"
    basic_group:basicGroup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateBasicGroupFullInfo(Update):
    __tdlib_type__ = "updateBasicGroupFullInfo"
    basic_group_id:int = attr.ib()
    basic_group_full_info:basicGroupFullInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateCall(Update):
    __tdlib_type__ = "updateCall"
    call:call = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatDefaultDisableNotification(Update):
    __tdlib_type__ = "updateChatDefaultDisableNotification"
    chat_id:int = attr.ib()
    default_disable_notification:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatDraftMessage(Update):
    __tdlib_type__ = "updateChatDraftMessage"
    chat_id:int = attr.ib()
    draft_message:draftMessage = attr.ib()
    order:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatIsMarkedAsUnread(Update):
    __tdlib_type__ = "updateChatIsMarkedAsUnread"
    chat_id:int = attr.ib()
    is_marked_as_unread:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatIsPinned(Update):
    __tdlib_type__ = "updateChatIsPinned"
    chat_id:int = attr.ib()
    is_pinned:bool = attr.ib()
    order:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatIsSponsored(Update):
    __tdlib_type__ = "updateChatIsSponsored"
    chat_id:int = attr.ib()
    is_sponsored:bool = attr.ib()
    order:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatLastMessage(Update):
    __tdlib_type__ = "updateChatLastMessage"
    chat_id:int = attr.ib()
    last_message:message = attr.ib()
    order:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatNotificationSettings(Update):
    __tdlib_type__ = "updateChatNotificationSettings"
    chat_id:int = attr.ib()
    notification_settings:chatNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatOnlineMemberCount(Update):
    __tdlib_type__ = "updateChatOnlineMemberCount"
    chat_id:int = attr.ib()
    online_member_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatOrder(Update):
    __tdlib_type__ = "updateChatOrder"
    chat_id:int = attr.ib()
    order:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatPermissions(Update):
    __tdlib_type__ = "updateChatPermissions"
    chat_id:int = attr.ib()
    permissions:chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatPhoto(Update):
    __tdlib_type__ = "updateChatPhoto"
    chat_id:int = attr.ib()
    photo:chatPhoto = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatPinnedMessage(Update):
    __tdlib_type__ = "updateChatPinnedMessage"
    chat_id:int = attr.ib()
    pinned_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatReadInbox(Update):
    __tdlib_type__ = "updateChatReadInbox"
    chat_id:int = attr.ib()
    last_read_inbox_message_id:int = attr.ib()
    unread_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatReadOutbox(Update):
    __tdlib_type__ = "updateChatReadOutbox"
    chat_id:int = attr.ib()
    last_read_outbox_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatReplyMarkup(Update):
    __tdlib_type__ = "updateChatReplyMarkup"
    chat_id:int = attr.ib()
    reply_markup_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatTitle(Update):
    __tdlib_type__ = "updateChatTitle"
    chat_id:int = attr.ib()
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateChatUnreadMentionCount(Update):
    __tdlib_type__ = "updateChatUnreadMentionCount"
    chat_id:int = attr.ib()
    unread_mention_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateConnectionState(Update):
    __tdlib_type__ = "updateConnectionState"
    state:ConnectionState = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateDeleteMessages(Update):
    __tdlib_type__ = "updateDeleteMessages"
    chat_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()
    is_permanent:bool = attr.ib()
    from_cache:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateFavoriteStickers(Update):
    __tdlib_type__ = "updateFavoriteStickers"
    sticker_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateFile(Update):
    __tdlib_type__ = "updateFile"
    file:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateFileGenerationStart(Update):
    __tdlib_type__ = "updateFileGenerationStart"
    generation_id:int = attr.ib()
    original_path:str = attr.ib()
    destination_path:str = attr.ib()
    conversion:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateFileGenerationStop(Update):
    __tdlib_type__ = "updateFileGenerationStop"
    generation_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateHavePendingNotifications(Update):
    __tdlib_type__ = "updateHavePendingNotifications"
    have_delayed_notifications:bool = attr.ib()
    have_unreceived_notifications:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateInstalledStickerSets(Update):
    __tdlib_type__ = "updateInstalledStickerSets"
    is_masks:bool = attr.ib()
    sticker_set_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateLanguagePackStrings(Update):
    __tdlib_type__ = "updateLanguagePackStrings"
    localization_target:str = attr.ib()
    language_pack_id:str = attr.ib()
    strings:typing.Sequence[languagePackString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageContent(Update):
    __tdlib_type__ = "updateMessageContent"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    new_content:MessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageContentOpened(Update):
    __tdlib_type__ = "updateMessageContentOpened"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageEdited(Update):
    __tdlib_type__ = "updateMessageEdited"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    edit_date:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageMentionRead(Update):
    __tdlib_type__ = "updateMessageMentionRead"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    unread_mention_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageSendAcknowledged(Update):
    __tdlib_type__ = "updateMessageSendAcknowledged"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageSendFailed(Update):
    __tdlib_type__ = "updateMessageSendFailed"
    message:message = attr.ib()
    old_message_id:int = attr.ib()
    error_code:int = attr.ib()
    error_message:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageSendSucceeded(Update):
    __tdlib_type__ = "updateMessageSendSucceeded"
    message:message = attr.ib()
    old_message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateMessageViews(Update):
    __tdlib_type__ = "updateMessageViews"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    views:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewCallbackQuery(Update):
    __tdlib_type__ = "updateNewCallbackQuery"
    id:int = attr.ib()
    sender_user_id:int = attr.ib()
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    chat_instance:int = attr.ib()
    payload:CallbackQueryPayload = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewChat(Update):
    __tdlib_type__ = "updateNewChat"
    chat:chat = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewChosenInlineResult(Update):
    __tdlib_type__ = "updateNewChosenInlineResult"
    sender_user_id:int = attr.ib()
    user_location:location = attr.ib()
    query:str = attr.ib()
    result_id:str = attr.ib()
    inline_message_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewCustomEvent(Update):
    __tdlib_type__ = "updateNewCustomEvent"
    event:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewCustomQuery(Update):
    __tdlib_type__ = "updateNewCustomQuery"
    id:int = attr.ib()
    data:str = attr.ib()
    timeout:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewInlineCallbackQuery(Update):
    __tdlib_type__ = "updateNewInlineCallbackQuery"
    id:int = attr.ib()
    sender_user_id:int = attr.ib()
    inline_message_id:str = attr.ib()
    chat_instance:int = attr.ib()
    payload:CallbackQueryPayload = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewInlineQuery(Update):
    __tdlib_type__ = "updateNewInlineQuery"
    id:int = attr.ib()
    sender_user_id:int = attr.ib()
    user_location:location = attr.ib()
    query:str = attr.ib()
    offset:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewMessage(Update):
    __tdlib_type__ = "updateNewMessage"
    message:message = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewPreCheckoutQuery(Update):
    __tdlib_type__ = "updateNewPreCheckoutQuery"
    id:int = attr.ib()
    sender_user_id:int = attr.ib()
    currency:str = attr.ib()
    total_amount:int = attr.ib()
    invoice_payload:bytes = attr.ib()
    shipping_option_id:str = attr.ib()
    order_info:orderInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNewShippingQuery(Update):
    __tdlib_type__ = "updateNewShippingQuery"
    id:int = attr.ib()
    sender_user_id:int = attr.ib()
    invoice_payload:str = attr.ib()
    shipping_address:address = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNotification(Update):
    __tdlib_type__ = "updateNotification"
    notification_group_id:int = attr.ib()
    notification:notification = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateNotificationGroup(Update):
    __tdlib_type__ = "updateNotificationGroup"
    notification_group_id:int = attr.ib()
    type:NotificationGroupType = attr.ib()
    chat_id:int = attr.ib()
    notification_settings_chat_id:int = attr.ib()
    is_silent:bool = attr.ib()
    total_count:int = attr.ib()
    added_notifications:typing.Sequence[notification] = attr.ib()
    removed_notification_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateOption(Update):
    __tdlib_type__ = "updateOption"
    name:str = attr.ib()
    value:OptionValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updatePoll(Update):
    __tdlib_type__ = "updatePoll"
    poll:poll = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateRecentStickers(Update):
    __tdlib_type__ = "updateRecentStickers"
    is_attached:bool = attr.ib()
    sticker_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateSavedAnimations(Update):
    __tdlib_type__ = "updateSavedAnimations"
    animation_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateScopeNotificationSettings(Update):
    __tdlib_type__ = "updateScopeNotificationSettings"
    scope:NotificationSettingsScope = attr.ib()
    notification_settings:scopeNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateSecretChat(Update):
    __tdlib_type__ = "updateSecretChat"
    secret_chat:secretChat = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateSelectedBackground(Update):
    __tdlib_type__ = "updateSelectedBackground"
    for_dark_theme:bool = attr.ib()
    background:background = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateServiceNotification(Update):
    __tdlib_type__ = "updateServiceNotification"
    type:str = attr.ib()
    content:MessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateSupergroup(Update):
    __tdlib_type__ = "updateSupergroup"
    supergroup:supergroup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateSupergroupFullInfo(Update):
    __tdlib_type__ = "updateSupergroupFullInfo"
    supergroup_id:int = attr.ib()
    supergroup_full_info:supergroupFullInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateTermsOfService(Update):
    __tdlib_type__ = "updateTermsOfService"
    terms_of_service_id:str = attr.ib()
    terms_of_service:termsOfService = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateTrendingStickerSets(Update):
    __tdlib_type__ = "updateTrendingStickerSets"
    sticker_sets:stickerSets = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUnreadChatCount(Update):
    __tdlib_type__ = "updateUnreadChatCount"
    unread_count:int = attr.ib()
    unread_unmuted_count:int = attr.ib()
    marked_as_unread_count:int = attr.ib()
    marked_as_unread_unmuted_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUnreadMessageCount(Update):
    __tdlib_type__ = "updateUnreadMessageCount"
    unread_count:int = attr.ib()
    unread_unmuted_count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUser(Update):
    __tdlib_type__ = "updateUser"
    user:user = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUserChatAction(Update):
    __tdlib_type__ = "updateUserChatAction"
    chat_id:int = attr.ib()
    user_id:int = attr.ib()
    action:ChatAction = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUserFullInfo(Update):
    __tdlib_type__ = "updateUserFullInfo"
    user_id:int = attr.ib()
    user_full_info:userFullInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUserPrivacySettingRules(Update):
    __tdlib_type__ = "updateUserPrivacySettingRules"
    setting:UserPrivacySetting = attr.ib()
    rules:userPrivacySettingRules = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updateUserStatus(Update):
    __tdlib_type__ = "updateUserStatus"
    user_id:int = attr.ib()
    status:UserStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_updates(Updates):
    __tdlib_type__ = "updates"
    updates:typing.Sequence[Update] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_user(User):
    __tdlib_type__ = "user"
    id:int = attr.ib()
    first_name:str = attr.ib()
    last_name:str = attr.ib()
    username:str = attr.ib()
    phone_number:str = attr.ib()
    status:UserStatus = attr.ib()
    profile_photo:profilePhoto = attr.ib()
    outgoing_link:LinkState = attr.ib()
    incoming_link:LinkState = attr.ib()
    is_verified:bool = attr.ib()
    is_support:bool = attr.ib()
    restriction_reason:str = attr.ib()
    is_scam:bool = attr.ib()
    have_access:bool = attr.ib()
    type:UserType = attr.ib()
    language_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userFullInfo(UserFullInfo):
    __tdlib_type__ = "userFullInfo"
    is_blocked:bool = attr.ib()
    can_be_called:bool = attr.ib()
    has_private_calls:bool = attr.ib()
    bio:str = attr.ib()
    share_text:str = attr.ib()
    group_in_common_count:int = attr.ib()
    bot_info:botInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingAllowCalls(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingAllowChatInvites(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowChatInvites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingAllowPeerToPeerCalls(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingAllowPeerToPeerCalls"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRuleAllowAll(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowAll"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRuleAllowContacts(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRuleAllowUsers(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleAllowUsers"
    user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRuleRestrictAll(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictAll"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRuleRestrictContacts(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRuleRestrictUsers(UserPrivacySettingRule):
    __tdlib_type__ = "userPrivacySettingRuleRestrictUsers"
    user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingRules(UserPrivacySettingRules):
    __tdlib_type__ = "userPrivacySettingRules"
    rules:typing.Sequence[UserPrivacySettingRule] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingShowLinkInForwardedMessages(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowLinkInForwardedMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingShowProfilePhoto(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowProfilePhoto"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userPrivacySettingShowStatus(UserPrivacySetting):
    __tdlib_type__ = "userPrivacySettingShowStatus"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userProfilePhoto(UserProfilePhoto):
    __tdlib_type__ = "userProfilePhoto"
    id:int = attr.ib()
    added_date:int = attr.ib()
    sizes:typing.Sequence[photoSize] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userProfilePhotos(UserProfilePhotos):
    __tdlib_type__ = "userProfilePhotos"
    total_count:int = attr.ib()
    photos:typing.Sequence[userProfilePhoto] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userStatusEmpty(UserStatus):
    __tdlib_type__ = "userStatusEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userStatusLastMonth(UserStatus):
    __tdlib_type__ = "userStatusLastMonth"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userStatusLastWeek(UserStatus):
    __tdlib_type__ = "userStatusLastWeek"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userStatusOffline(UserStatus):
    __tdlib_type__ = "userStatusOffline"
    was_online:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userStatusOnline(UserStatus):
    __tdlib_type__ = "userStatusOnline"
    expires:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userStatusRecently(UserStatus):
    __tdlib_type__ = "userStatusRecently"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userTypeBot(UserType):
    __tdlib_type__ = "userTypeBot"
    can_join_groups:bool = attr.ib()
    can_read_all_group_messages:bool = attr.ib()
    is_inline:bool = attr.ib()
    inline_query_placeholder:str = attr.ib()
    need_location:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userTypeDeleted(UserType):
    __tdlib_type__ = "userTypeDeleted"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userTypeRegular(UserType):
    __tdlib_type__ = "userTypeRegular"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_userTypeUnknown(UserType):
    __tdlib_type__ = "userTypeUnknown"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_users(Users):
    __tdlib_type__ = "users"
    total_count:int = attr.ib()
    user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_validatedOrderInfo(ValidatedOrderInfo):
    __tdlib_type__ = "validatedOrderInfo"
    order_info_id:str = attr.ib()
    shipping_options:typing.Sequence[shippingOption] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_venue(Venue):
    __tdlib_type__ = "venue"
    location:location = attr.ib()
    title:str = attr.ib()
    address:str = attr.ib()
    provider:str = attr.ib()
    id:str = attr.ib()
    type:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_video(Video):
    __tdlib_type__ = "video"
    duration:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    file_name:str = attr.ib()
    mime_type:str = attr.ib()
    has_stickers:bool = attr.ib()
    supports_streaming:bool = attr.ib()
    minithumbnail:minithumbnail = attr.ib()
    thumbnail:photoSize = attr.ib()
    video:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_videoNote(VideoNote):
    __tdlib_type__ = "videoNote"
    duration:int = attr.ib()
    length:int = attr.ib()
    minithumbnail:minithumbnail = attr.ib()
    thumbnail:photoSize = attr.ib()
    video:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_voiceNote(VoiceNote):
    __tdlib_type__ = "voiceNote"
    duration:int = attr.ib()
    waveform:bytes = attr.ib()
    mime_type:str = attr.ib()
    voice:file = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_webPage(WebPage):
    __tdlib_type__ = "webPage"
    url:str = attr.ib()
    display_url:str = attr.ib()
    type:str = attr.ib()
    site_name:str = attr.ib()
    title:str = attr.ib()
    description:str = attr.ib()
    photo:photo = attr.ib()
    embed_url:str = attr.ib()
    embed_type:str = attr.ib()
    embed_width:int = attr.ib()
    embed_height:int = attr.ib()
    duration:int = attr.ib()
    author:str = attr.ib()
    animation:animation = attr.ib()
    audio:audio = attr.ib()
    document:document = attr.ib()
    sticker:sticker = attr.ib()
    video:video = attr.ib()
    video_note:videoNote = attr.ib()
    voice_note:voiceNote = attr.ib()
    instant_view_version:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_type_webPageInstantView(WebPageInstantView):
    __tdlib_type__ = "webPageInstantView"
    page_blocks:typing.Sequence[PageBlock] = attr.ib()
    version:int = attr.ib()
    url:str = attr.ib()
    is_rtl:bool = attr.ib()
    is_full:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getAuthorizationState(RootObject):
    __tdlib_type__ = "getAuthorizationState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setTdlibParameters(RootObject):
    __tdlib_type__ = "setTdlibParameters"
    parameters:tdlibParameters = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkDatabaseEncryptionKey(RootObject):
    __tdlib_type__ = "checkDatabaseEncryptionKey"
    encryption_key:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setAuthenticationPhoneNumber(RootObject):
    __tdlib_type__ = "setAuthenticationPhoneNumber"
    phone_number:str = attr.ib()
    settings:phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendAuthenticationCode(RootObject):
    __tdlib_type__ = "resendAuthenticationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkAuthenticationCode(RootObject):
    __tdlib_type__ = "checkAuthenticationCode"
    code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_registerUser(RootObject):
    __tdlib_type__ = "registerUser"
    first_name:str = attr.ib()
    last_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkAuthenticationPassword(RootObject):
    __tdlib_type__ = "checkAuthenticationPassword"
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_requestAuthenticationPasswordRecovery(RootObject):
    __tdlib_type__ = "requestAuthenticationPasswordRecovery"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_recoverAuthenticationPassword(RootObject):
    __tdlib_type__ = "recoverAuthenticationPassword"
    recovery_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkAuthenticationBotToken(RootObject):
    __tdlib_type__ = "checkAuthenticationBotToken"
    token:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_logOut(RootObject):
    __tdlib_type__ = "logOut"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_close(RootObject):
    __tdlib_type__ = "close"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_destroy(RootObject):
    __tdlib_type__ = "destroy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getCurrentState(RootObject):
    __tdlib_type__ = "getCurrentState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setDatabaseEncryptionKey(RootObject):
    __tdlib_type__ = "setDatabaseEncryptionKey"
    new_encryption_key:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPasswordState(RootObject):
    __tdlib_type__ = "getPasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setPassword(RootObject):
    __tdlib_type__ = "setPassword"
    old_password:str = attr.ib()
    new_password:str = attr.ib()
    new_hint:str = attr.ib()
    set_recovery_email_address:bool = attr.ib()
    new_recovery_email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getRecoveryEmailAddress(RootObject):
    __tdlib_type__ = "getRecoveryEmailAddress"
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setRecoveryEmailAddress(RootObject):
    __tdlib_type__ = "setRecoveryEmailAddress"
    password:str = attr.ib()
    new_recovery_email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkRecoveryEmailAddressCode(RootObject):
    __tdlib_type__ = "checkRecoveryEmailAddressCode"
    code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendRecoveryEmailAddressCode(RootObject):
    __tdlib_type__ = "resendRecoveryEmailAddressCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_requestPasswordRecovery(RootObject):
    __tdlib_type__ = "requestPasswordRecovery"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_recoverPassword(RootObject):
    __tdlib_type__ = "recoverPassword"
    recovery_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createTemporaryPassword(RootObject):
    __tdlib_type__ = "createTemporaryPassword"
    password:str = attr.ib()
    valid_for:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getTemporaryPasswordState(RootObject):
    __tdlib_type__ = "getTemporaryPasswordState"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMe(RootObject):
    __tdlib_type__ = "getMe"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getUser(RootObject):
    __tdlib_type__ = "getUser"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getUserFullInfo(RootObject):
    __tdlib_type__ = "getUserFullInfo"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getBasicGroup(RootObject):
    __tdlib_type__ = "getBasicGroup"
    basic_group_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getBasicGroupFullInfo(RootObject):
    __tdlib_type__ = "getBasicGroupFullInfo"
    basic_group_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSupergroup(RootObject):
    __tdlib_type__ = "getSupergroup"
    supergroup_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSupergroupFullInfo(RootObject):
    __tdlib_type__ = "getSupergroupFullInfo"
    supergroup_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSecretChat(RootObject):
    __tdlib_type__ = "getSecretChat"
    secret_chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChat(RootObject):
    __tdlib_type__ = "getChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMessage(RootObject):
    __tdlib_type__ = "getMessage"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMessageLocally(RootObject):
    __tdlib_type__ = "getMessageLocally"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getRepliedMessage(RootObject):
    __tdlib_type__ = "getRepliedMessage"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatPinnedMessage(RootObject):
    __tdlib_type__ = "getChatPinnedMessage"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMessages(RootObject):
    __tdlib_type__ = "getMessages"
    chat_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getFile(RootObject):
    __tdlib_type__ = "getFile"
    file_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getRemoteFile(RootObject):
    __tdlib_type__ = "getRemoteFile"
    remote_file_id:str = attr.ib()
    file_type:FileType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChats(RootObject):
    __tdlib_type__ = "getChats"
    offset_order:int = attr.ib()
    offset_chat_id:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchPublicChat(RootObject):
    __tdlib_type__ = "searchPublicChat"
    username:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchPublicChats(RootObject):
    __tdlib_type__ = "searchPublicChats"
    query:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchChats(RootObject):
    __tdlib_type__ = "searchChats"
    query:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchChatsOnServer(RootObject):
    __tdlib_type__ = "searchChatsOnServer"
    query:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getTopChats(RootObject):
    __tdlib_type__ = "getTopChats"
    category:TopChatCategory = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeTopChat(RootObject):
    __tdlib_type__ = "removeTopChat"
    category:TopChatCategory = attr.ib()
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addRecentlyFoundChat(RootObject):
    __tdlib_type__ = "addRecentlyFoundChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeRecentlyFoundChat(RootObject):
    __tdlib_type__ = "removeRecentlyFoundChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_clearRecentlyFoundChats(RootObject):
    __tdlib_type__ = "clearRecentlyFoundChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkChatUsername(RootObject):
    __tdlib_type__ = "checkChatUsername"
    chat_id:int = attr.ib()
    username:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getCreatedPublicChats(RootObject):
    __tdlib_type__ = "getCreatedPublicChats"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getGroupsInCommon(RootObject):
    __tdlib_type__ = "getGroupsInCommon"
    user_id:int = attr.ib()
    offset_chat_id:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatHistory(RootObject):
    __tdlib_type__ = "getChatHistory"
    chat_id:int = attr.ib()
    from_message_id:int = attr.ib()
    offset:int = attr.ib()
    limit:int = attr.ib()
    only_local:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteChatHistory(RootObject):
    __tdlib_type__ = "deleteChatHistory"
    chat_id:int = attr.ib()
    remove_from_chat_list:bool = attr.ib()
    revoke:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchChatMessages(RootObject):
    __tdlib_type__ = "searchChatMessages"
    chat_id:int = attr.ib()
    query:str = attr.ib()
    sender_user_id:int = attr.ib()
    from_message_id:int = attr.ib()
    offset:int = attr.ib()
    limit:int = attr.ib()
    filter:SearchMessagesFilter = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchMessages(RootObject):
    __tdlib_type__ = "searchMessages"
    query:str = attr.ib()
    offset_date:int = attr.ib()
    offset_chat_id:int = attr.ib()
    offset_message_id:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchSecretMessages(RootObject):
    __tdlib_type__ = "searchSecretMessages"
    chat_id:int = attr.ib()
    query:str = attr.ib()
    from_search_id:int = attr.ib()
    limit:int = attr.ib()
    filter:SearchMessagesFilter = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchCallMessages(RootObject):
    __tdlib_type__ = "searchCallMessages"
    from_message_id:int = attr.ib()
    limit:int = attr.ib()
    only_missed:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchChatRecentLocationMessages(RootObject):
    __tdlib_type__ = "searchChatRecentLocationMessages"
    chat_id:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getActiveLiveLocationMessages(RootObject):
    __tdlib_type__ = "getActiveLiveLocationMessages"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatMessageByDate(RootObject):
    __tdlib_type__ = "getChatMessageByDate"
    chat_id:int = attr.ib()
    date:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatMessageCount(RootObject):
    __tdlib_type__ = "getChatMessageCount"
    chat_id:int = attr.ib()
    filter:SearchMessagesFilter = attr.ib()
    return_local:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeNotification(RootObject):
    __tdlib_type__ = "removeNotification"
    notification_group_id:int = attr.ib()
    notification_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeNotificationGroup(RootObject):
    __tdlib_type__ = "removeNotificationGroup"
    notification_group_id:int = attr.ib()
    max_notification_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPublicMessageLink(RootObject):
    __tdlib_type__ = "getPublicMessageLink"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    for_album:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMessageLink(RootObject):
    __tdlib_type__ = "getMessageLink"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMessageLinkInfo(RootObject):
    __tdlib_type__ = "getMessageLinkInfo"
    url:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendMessage(RootObject):
    __tdlib_type__ = "sendMessage"
    chat_id:int = attr.ib()
    reply_to_message_id:int = attr.ib()
    disable_notification:bool = attr.ib()
    from_background:bool = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendMessageAlbum(RootObject):
    __tdlib_type__ = "sendMessageAlbum"
    chat_id:int = attr.ib()
    reply_to_message_id:int = attr.ib()
    disable_notification:bool = attr.ib()
    from_background:bool = attr.ib()
    input_message_contents:typing.Sequence[InputMessageContent] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendBotStartMessage(RootObject):
    __tdlib_type__ = "sendBotStartMessage"
    bot_user_id:int = attr.ib()
    chat_id:int = attr.ib()
    parameter:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendInlineQueryResultMessage(RootObject):
    __tdlib_type__ = "sendInlineQueryResultMessage"
    chat_id:int = attr.ib()
    reply_to_message_id:int = attr.ib()
    disable_notification:bool = attr.ib()
    from_background:bool = attr.ib()
    query_id:int = attr.ib()
    result_id:str = attr.ib()
    hide_via_bot:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_forwardMessages(RootObject):
    __tdlib_type__ = "forwardMessages"
    chat_id:int = attr.ib()
    from_chat_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()
    disable_notification:bool = attr.ib()
    from_background:bool = attr.ib()
    as_album:bool = attr.ib()
    send_copy:bool = attr.ib()
    remove_caption:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendMessages(RootObject):
    __tdlib_type__ = "resendMessages"
    chat_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendChatSetTtlMessage(RootObject):
    __tdlib_type__ = "sendChatSetTtlMessage"
    chat_id:int = attr.ib()
    ttl:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendChatScreenshotTakenNotification(RootObject):
    __tdlib_type__ = "sendChatScreenshotTakenNotification"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addLocalMessage(RootObject):
    __tdlib_type__ = "addLocalMessage"
    chat_id:int = attr.ib()
    sender_user_id:int = attr.ib()
    reply_to_message_id:int = attr.ib()
    disable_notification:bool = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteMessages(RootObject):
    __tdlib_type__ = "deleteMessages"
    chat_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()
    revoke:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteChatMessagesFromUser(RootObject):
    __tdlib_type__ = "deleteChatMessagesFromUser"
    chat_id:int = attr.ib()
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editMessageText(RootObject):
    __tdlib_type__ = "editMessageText"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editMessageLiveLocation(RootObject):
    __tdlib_type__ = "editMessageLiveLocation"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    location:location = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editMessageMedia(RootObject):
    __tdlib_type__ = "editMessageMedia"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editMessageCaption(RootObject):
    __tdlib_type__ = "editMessageCaption"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editMessageReplyMarkup(RootObject):
    __tdlib_type__ = "editMessageReplyMarkup"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editInlineMessageText(RootObject):
    __tdlib_type__ = "editInlineMessageText"
    inline_message_id:str = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editInlineMessageLiveLocation(RootObject):
    __tdlib_type__ = "editInlineMessageLiveLocation"
    inline_message_id:str = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    location:location = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editInlineMessageMedia(RootObject):
    __tdlib_type__ = "editInlineMessageMedia"
    inline_message_id:str = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    input_message_content:InputMessageContent = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editInlineMessageCaption(RootObject):
    __tdlib_type__ = "editInlineMessageCaption"
    inline_message_id:str = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()
    caption:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editInlineMessageReplyMarkup(RootObject):
    __tdlib_type__ = "editInlineMessageReplyMarkup"
    inline_message_id:str = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getTextEntities(RootObject):
    __tdlib_type__ = "getTextEntities"
    text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_parseTextEntities(RootObject):
    __tdlib_type__ = "parseTextEntities"
    text:str = attr.ib()
    parse_mode:TextParseMode = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getFileMimeType(RootObject):
    __tdlib_type__ = "getFileMimeType"
    file_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getFileExtension(RootObject):
    __tdlib_type__ = "getFileExtension"
    mime_type:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_cleanFileName(RootObject):
    __tdlib_type__ = "cleanFileName"
    file_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLanguagePackString(RootObject):
    __tdlib_type__ = "getLanguagePackString"
    language_pack_database_path:str = attr.ib()
    localization_target:str = attr.ib()
    language_pack_id:str = attr.ib()
    key:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getJsonValue(RootObject):
    __tdlib_type__ = "getJsonValue"
    json:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getJsonString(RootObject):
    __tdlib_type__ = "getJsonString"
    json_value:JsonValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setPollAnswer(RootObject):
    __tdlib_type__ = "setPollAnswer"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    option_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_stopPoll(RootObject):
    __tdlib_type__ = "stopPoll"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    reply_markup:ReplyMarkup = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getInlineQueryResults(RootObject):
    __tdlib_type__ = "getInlineQueryResults"
    bot_user_id:int = attr.ib()
    chat_id:int = attr.ib()
    user_location:location = attr.ib()
    query:str = attr.ib()
    offset:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_answerInlineQuery(RootObject):
    __tdlib_type__ = "answerInlineQuery"
    inline_query_id:int = attr.ib()
    is_personal:bool = attr.ib()
    results:typing.Sequence[InputInlineQueryResult] = attr.ib()
    cache_time:int = attr.ib()
    next_offset:str = attr.ib()
    switch_pm_text:str = attr.ib()
    switch_pm_parameter:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getCallbackQueryAnswer(RootObject):
    __tdlib_type__ = "getCallbackQueryAnswer"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    payload:CallbackQueryPayload = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_answerCallbackQuery(RootObject):
    __tdlib_type__ = "answerCallbackQuery"
    callback_query_id:int = attr.ib()
    text:str = attr.ib()
    show_alert:bool = attr.ib()
    url:str = attr.ib()
    cache_time:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_answerShippingQuery(RootObject):
    __tdlib_type__ = "answerShippingQuery"
    shipping_query_id:int = attr.ib()
    shipping_options:typing.Sequence[shippingOption] = attr.ib()
    error_message:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_answerPreCheckoutQuery(RootObject):
    __tdlib_type__ = "answerPreCheckoutQuery"
    pre_checkout_query_id:int = attr.ib()
    error_message:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setGameScore(RootObject):
    __tdlib_type__ = "setGameScore"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    edit_message:bool = attr.ib()
    user_id:int = attr.ib()
    score:int = attr.ib()
    force:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setInlineGameScore(RootObject):
    __tdlib_type__ = "setInlineGameScore"
    inline_message_id:str = attr.ib()
    edit_message:bool = attr.ib()
    user_id:int = attr.ib()
    score:int = attr.ib()
    force:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getGameHighScores(RootObject):
    __tdlib_type__ = "getGameHighScores"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getInlineGameHighScores(RootObject):
    __tdlib_type__ = "getInlineGameHighScores"
    inline_message_id:str = attr.ib()
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteChatReplyMarkup(RootObject):
    __tdlib_type__ = "deleteChatReplyMarkup"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendChatAction(RootObject):
    __tdlib_type__ = "sendChatAction"
    chat_id:int = attr.ib()
    action:ChatAction = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_openChat(RootObject):
    __tdlib_type__ = "openChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_closeChat(RootObject):
    __tdlib_type__ = "closeChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_viewMessages(RootObject):
    __tdlib_type__ = "viewMessages"
    chat_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()
    force_read:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_openMessageContent(RootObject):
    __tdlib_type__ = "openMessageContent"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_readAllChatMentions(RootObject):
    __tdlib_type__ = "readAllChatMentions"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createPrivateChat(RootObject):
    __tdlib_type__ = "createPrivateChat"
    user_id:int = attr.ib()
    force:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createBasicGroupChat(RootObject):
    __tdlib_type__ = "createBasicGroupChat"
    basic_group_id:int = attr.ib()
    force:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createSupergroupChat(RootObject):
    __tdlib_type__ = "createSupergroupChat"
    supergroup_id:int = attr.ib()
    force:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createSecretChat(RootObject):
    __tdlib_type__ = "createSecretChat"
    secret_chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createNewBasicGroupChat(RootObject):
    __tdlib_type__ = "createNewBasicGroupChat"
    user_ids:typing.Sequence[int] = attr.ib()
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createNewSupergroupChat(RootObject):
    __tdlib_type__ = "createNewSupergroupChat"
    title:str = attr.ib()
    is_channel:bool = attr.ib()
    description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createNewSecretChat(RootObject):
    __tdlib_type__ = "createNewSecretChat"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_upgradeBasicGroupChatToSupergroupChat(RootObject):
    __tdlib_type__ = "upgradeBasicGroupChatToSupergroupChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatTitle(RootObject):
    __tdlib_type__ = "setChatTitle"
    chat_id:int = attr.ib()
    title:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatPhoto(RootObject):
    __tdlib_type__ = "setChatPhoto"
    chat_id:int = attr.ib()
    photo:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatPermissions(RootObject):
    __tdlib_type__ = "setChatPermissions"
    chat_id:int = attr.ib()
    permissions:chatPermissions = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatDraftMessage(RootObject):
    __tdlib_type__ = "setChatDraftMessage"
    chat_id:int = attr.ib()
    draft_message:draftMessage = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatNotificationSettings(RootObject):
    __tdlib_type__ = "setChatNotificationSettings"
    chat_id:int = attr.ib()
    notification_settings:chatNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_toggleChatIsPinned(RootObject):
    __tdlib_type__ = "toggleChatIsPinned"
    chat_id:int = attr.ib()
    is_pinned:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_toggleChatIsMarkedAsUnread(RootObject):
    __tdlib_type__ = "toggleChatIsMarkedAsUnread"
    chat_id:int = attr.ib()
    is_marked_as_unread:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_toggleChatDefaultDisableNotification(RootObject):
    __tdlib_type__ = "toggleChatDefaultDisableNotification"
    chat_id:int = attr.ib()
    default_disable_notification:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatClientData(RootObject):
    __tdlib_type__ = "setChatClientData"
    chat_id:int = attr.ib()
    client_data:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatDescription(RootObject):
    __tdlib_type__ = "setChatDescription"
    chat_id:int = attr.ib()
    description:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_pinChatMessage(RootObject):
    __tdlib_type__ = "pinChatMessage"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    disable_notification:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_unpinChatMessage(RootObject):
    __tdlib_type__ = "unpinChatMessage"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_joinChat(RootObject):
    __tdlib_type__ = "joinChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_leaveChat(RootObject):
    __tdlib_type__ = "leaveChat"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addChatMember(RootObject):
    __tdlib_type__ = "addChatMember"
    chat_id:int = attr.ib()
    user_id:int = attr.ib()
    forward_limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addChatMembers(RootObject):
    __tdlib_type__ = "addChatMembers"
    chat_id:int = attr.ib()
    user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setChatMemberStatus(RootObject):
    __tdlib_type__ = "setChatMemberStatus"
    chat_id:int = attr.ib()
    user_id:int = attr.ib()
    status:ChatMemberStatus = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatMember(RootObject):
    __tdlib_type__ = "getChatMember"
    chat_id:int = attr.ib()
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchChatMembers(RootObject):
    __tdlib_type__ = "searchChatMembers"
    chat_id:int = attr.ib()
    query:str = attr.ib()
    limit:int = attr.ib()
    filter:ChatMembersFilter = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatAdministrators(RootObject):
    __tdlib_type__ = "getChatAdministrators"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_clearAllDraftMessages(RootObject):
    __tdlib_type__ = "clearAllDraftMessages"
    exclude_secret_chats:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatNotificationSettingsExceptions(RootObject):
    __tdlib_type__ = "getChatNotificationSettingsExceptions"
    scope:NotificationSettingsScope = attr.ib()
    compare_sound:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getScopeNotificationSettings(RootObject):
    __tdlib_type__ = "getScopeNotificationSettings"
    scope:NotificationSettingsScope = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setScopeNotificationSettings(RootObject):
    __tdlib_type__ = "setScopeNotificationSettings"
    scope:NotificationSettingsScope = attr.ib()
    notification_settings:scopeNotificationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resetAllNotificationSettings(RootObject):
    __tdlib_type__ = "resetAllNotificationSettings"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setPinnedChats(RootObject):
    __tdlib_type__ = "setPinnedChats"
    chat_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_downloadFile(RootObject):
    __tdlib_type__ = "downloadFile"
    file_id:int = attr.ib()
    priority:int = attr.ib()
    offset:int = attr.ib()
    limit:int = attr.ib()
    synchronous:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getFileDownloadedPrefixSize(RootObject):
    __tdlib_type__ = "getFileDownloadedPrefixSize"
    file_id:int = attr.ib()
    offset:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_cancelDownloadFile(RootObject):
    __tdlib_type__ = "cancelDownloadFile"
    file_id:int = attr.ib()
    only_if_pending:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_uploadFile(RootObject):
    __tdlib_type__ = "uploadFile"
    file:InputFile = attr.ib()
    file_type:FileType = attr.ib()
    priority:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_cancelUploadFile(RootObject):
    __tdlib_type__ = "cancelUploadFile"
    file_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_writeGeneratedFilePart(RootObject):
    __tdlib_type__ = "writeGeneratedFilePart"
    generation_id:int = attr.ib()
    offset:int = attr.ib()
    data:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setFileGenerationProgress(RootObject):
    __tdlib_type__ = "setFileGenerationProgress"
    generation_id:int = attr.ib()
    expected_size:int = attr.ib()
    local_prefix_size:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_finishFileGeneration(RootObject):
    __tdlib_type__ = "finishFileGeneration"
    generation_id:int = attr.ib()
    error:error = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_readFilePart(RootObject):
    __tdlib_type__ = "readFilePart"
    file_id:int = attr.ib()
    offset:int = attr.ib()
    count:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteFile(RootObject):
    __tdlib_type__ = "deleteFile"
    file_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_generateChatInviteLink(RootObject):
    __tdlib_type__ = "generateChatInviteLink"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkChatInviteLink(RootObject):
    __tdlib_type__ = "checkChatInviteLink"
    invite_link:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_joinChatByInviteLink(RootObject):
    __tdlib_type__ = "joinChatByInviteLink"
    invite_link:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createCall(RootObject):
    __tdlib_type__ = "createCall"
    user_id:int = attr.ib()
    protocol:callProtocol = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_acceptCall(RootObject):
    __tdlib_type__ = "acceptCall"
    call_id:int = attr.ib()
    protocol:callProtocol = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_discardCall(RootObject):
    __tdlib_type__ = "discardCall"
    call_id:int = attr.ib()
    is_disconnected:bool = attr.ib()
    duration:int = attr.ib()
    connection_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendCallRating(RootObject):
    __tdlib_type__ = "sendCallRating"
    call_id:int = attr.ib()
    rating:int = attr.ib()
    comment:str = attr.ib()
    problems:typing.Sequence[CallProblem] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendCallDebugInformation(RootObject):
    __tdlib_type__ = "sendCallDebugInformation"
    call_id:int = attr.ib()
    debug_information:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_blockUser(RootObject):
    __tdlib_type__ = "blockUser"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_unblockUser(RootObject):
    __tdlib_type__ = "unblockUser"
    user_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getBlockedUsers(RootObject):
    __tdlib_type__ = "getBlockedUsers"
    offset:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_importContacts(RootObject):
    __tdlib_type__ = "importContacts"
    contacts:typing.Sequence[contact] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getContacts(RootObject):
    __tdlib_type__ = "getContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchContacts(RootObject):
    __tdlib_type__ = "searchContacts"
    query:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeContacts(RootObject):
    __tdlib_type__ = "removeContacts"
    user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getImportedContactCount(RootObject):
    __tdlib_type__ = "getImportedContactCount"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_changeImportedContacts(RootObject):
    __tdlib_type__ = "changeImportedContacts"
    contacts:typing.Sequence[contact] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_clearImportedContacts(RootObject):
    __tdlib_type__ = "clearImportedContacts"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getUserProfilePhotos(RootObject):
    __tdlib_type__ = "getUserProfilePhotos"
    user_id:int = attr.ib()
    offset:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getStickers(RootObject):
    __tdlib_type__ = "getStickers"
    emoji:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchStickers(RootObject):
    __tdlib_type__ = "searchStickers"
    emoji:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getInstalledStickerSets(RootObject):
    __tdlib_type__ = "getInstalledStickerSets"
    is_masks:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getArchivedStickerSets(RootObject):
    __tdlib_type__ = "getArchivedStickerSets"
    is_masks:bool = attr.ib()
    offset_sticker_set_id:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getTrendingStickerSets(RootObject):
    __tdlib_type__ = "getTrendingStickerSets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getAttachedStickerSets(RootObject):
    __tdlib_type__ = "getAttachedStickerSets"
    file_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getStickerSet(RootObject):
    __tdlib_type__ = "getStickerSet"
    set_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchStickerSet(RootObject):
    __tdlib_type__ = "searchStickerSet"
    name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchInstalledStickerSets(RootObject):
    __tdlib_type__ = "searchInstalledStickerSets"
    is_masks:bool = attr.ib()
    query:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchStickerSets(RootObject):
    __tdlib_type__ = "searchStickerSets"
    query:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_changeStickerSet(RootObject):
    __tdlib_type__ = "changeStickerSet"
    set_id:int = attr.ib()
    is_installed:bool = attr.ib()
    is_archived:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_viewTrendingStickerSets(RootObject):
    __tdlib_type__ = "viewTrendingStickerSets"
    sticker_set_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_reorderInstalledStickerSets(RootObject):
    __tdlib_type__ = "reorderInstalledStickerSets"
    is_masks:bool = attr.ib()
    sticker_set_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getRecentStickers(RootObject):
    __tdlib_type__ = "getRecentStickers"
    is_attached:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addRecentSticker(RootObject):
    __tdlib_type__ = "addRecentSticker"
    is_attached:bool = attr.ib()
    sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeRecentSticker(RootObject):
    __tdlib_type__ = "removeRecentSticker"
    is_attached:bool = attr.ib()
    sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_clearRecentStickers(RootObject):
    __tdlib_type__ = "clearRecentStickers"
    is_attached:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getFavoriteStickers(RootObject):
    __tdlib_type__ = "getFavoriteStickers"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addFavoriteSticker(RootObject):
    __tdlib_type__ = "addFavoriteSticker"
    sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeFavoriteSticker(RootObject):
    __tdlib_type__ = "removeFavoriteSticker"
    sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getStickerEmojis(RootObject):
    __tdlib_type__ = "getStickerEmojis"
    sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchEmojis(RootObject):
    __tdlib_type__ = "searchEmojis"
    text:str = attr.ib()
    exact_match:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getEmojiSuggestionsUrl(RootObject):
    __tdlib_type__ = "getEmojiSuggestionsUrl"
    language_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSavedAnimations(RootObject):
    __tdlib_type__ = "getSavedAnimations"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addSavedAnimation(RootObject):
    __tdlib_type__ = "addSavedAnimation"
    animation:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeSavedAnimation(RootObject):
    __tdlib_type__ = "removeSavedAnimation"
    animation:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getRecentInlineBots(RootObject):
    __tdlib_type__ = "getRecentInlineBots"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchHashtags(RootObject):
    __tdlib_type__ = "searchHashtags"
    prefix:str = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeRecentHashtag(RootObject):
    __tdlib_type__ = "removeRecentHashtag"
    hashtag:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getWebPagePreview(RootObject):
    __tdlib_type__ = "getWebPagePreview"
    text:formattedText = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getWebPageInstantView(RootObject):
    __tdlib_type__ = "getWebPageInstantView"
    url:str = attr.ib()
    force_full:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setProfilePhoto(RootObject):
    __tdlib_type__ = "setProfilePhoto"
    photo:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteProfilePhoto(RootObject):
    __tdlib_type__ = "deleteProfilePhoto"
    profile_photo_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setName(RootObject):
    __tdlib_type__ = "setName"
    first_name:str = attr.ib()
    last_name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setBio(RootObject):
    __tdlib_type__ = "setBio"
    bio:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setUsername(RootObject):
    __tdlib_type__ = "setUsername"
    username:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_changePhoneNumber(RootObject):
    __tdlib_type__ = "changePhoneNumber"
    phone_number:str = attr.ib()
    settings:phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendChangePhoneNumberCode(RootObject):
    __tdlib_type__ = "resendChangePhoneNumberCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkChangePhoneNumberCode(RootObject):
    __tdlib_type__ = "checkChangePhoneNumberCode"
    code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getActiveSessions(RootObject):
    __tdlib_type__ = "getActiveSessions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_terminateSession(RootObject):
    __tdlib_type__ = "terminateSession"
    session_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_terminateAllOtherSessions(RootObject):
    __tdlib_type__ = "terminateAllOtherSessions"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getConnectedWebsites(RootObject):
    __tdlib_type__ = "getConnectedWebsites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_disconnectWebsite(RootObject):
    __tdlib_type__ = "disconnectWebsite"
    website_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_disconnectAllWebsites(RootObject):
    __tdlib_type__ = "disconnectAllWebsites"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setSupergroupUsername(RootObject):
    __tdlib_type__ = "setSupergroupUsername"
    supergroup_id:int = attr.ib()
    username:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setSupergroupStickerSet(RootObject):
    __tdlib_type__ = "setSupergroupStickerSet"
    supergroup_id:int = attr.ib()
    sticker_set_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_toggleSupergroupSignMessages(RootObject):
    __tdlib_type__ = "toggleSupergroupSignMessages"
    supergroup_id:int = attr.ib()
    sign_messages:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_toggleSupergroupIsAllHistoryAvailable(RootObject):
    __tdlib_type__ = "toggleSupergroupIsAllHistoryAvailable"
    supergroup_id:int = attr.ib()
    is_all_history_available:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_reportSupergroupSpam(RootObject):
    __tdlib_type__ = "reportSupergroupSpam"
    supergroup_id:int = attr.ib()
    user_id:int = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSupergroupMembers(RootObject):
    __tdlib_type__ = "getSupergroupMembers"
    supergroup_id:int = attr.ib()
    filter:SupergroupMembersFilter = attr.ib()
    offset:int = attr.ib()
    limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteSupergroup(RootObject):
    __tdlib_type__ = "deleteSupergroup"
    supergroup_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_closeSecretChat(RootObject):
    __tdlib_type__ = "closeSecretChat"
    secret_chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatEventLog(RootObject):
    __tdlib_type__ = "getChatEventLog"
    chat_id:int = attr.ib()
    query:str = attr.ib()
    from_event_id:int = attr.ib()
    limit:int = attr.ib()
    filters:chatEventLogFilters = attr.ib()
    user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPaymentForm(RootObject):
    __tdlib_type__ = "getPaymentForm"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_validateOrderInfo(RootObject):
    __tdlib_type__ = "validateOrderInfo"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    order_info:orderInfo = attr.ib()
    allow_save:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendPaymentForm(RootObject):
    __tdlib_type__ = "sendPaymentForm"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()
    order_info_id:str = attr.ib()
    shipping_option_id:str = attr.ib()
    credentials:InputCredentials = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPaymentReceipt(RootObject):
    __tdlib_type__ = "getPaymentReceipt"
    chat_id:int = attr.ib()
    message_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSavedOrderInfo(RootObject):
    __tdlib_type__ = "getSavedOrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteSavedOrderInfo(RootObject):
    __tdlib_type__ = "deleteSavedOrderInfo"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteSavedCredentials(RootObject):
    __tdlib_type__ = "deleteSavedCredentials"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getSupportUser(RootObject):
    __tdlib_type__ = "getSupportUser"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getBackgrounds(RootObject):
    __tdlib_type__ = "getBackgrounds"
    for_dark_theme:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getBackgroundUrl(RootObject):
    __tdlib_type__ = "getBackgroundUrl"
    name:str = attr.ib()
    type:BackgroundType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_searchBackground(RootObject):
    __tdlib_type__ = "searchBackground"
    name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setBackground(RootObject):
    __tdlib_type__ = "setBackground"
    background:InputBackground = attr.ib()
    type:BackgroundType = attr.ib()
    for_dark_theme:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeBackground(RootObject):
    __tdlib_type__ = "removeBackground"
    background_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resetBackgrounds(RootObject):
    __tdlib_type__ = "resetBackgrounds"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLocalizationTargetInfo(RootObject):
    __tdlib_type__ = "getLocalizationTargetInfo"
    only_local:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLanguagePackInfo(RootObject):
    __tdlib_type__ = "getLanguagePackInfo"
    language_pack_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLanguagePackStrings(RootObject):
    __tdlib_type__ = "getLanguagePackStrings"
    language_pack_id:str = attr.ib()
    keys:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_synchronizeLanguagePack(RootObject):
    __tdlib_type__ = "synchronizeLanguagePack"
    language_pack_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addCustomServerLanguagePack(RootObject):
    __tdlib_type__ = "addCustomServerLanguagePack"
    language_pack_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setCustomLanguagePack(RootObject):
    __tdlib_type__ = "setCustomLanguagePack"
    info:languagePackInfo = attr.ib()
    strings:typing.Sequence[languagePackString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editCustomLanguagePackInfo(RootObject):
    __tdlib_type__ = "editCustomLanguagePackInfo"
    info:languagePackInfo = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setCustomLanguagePackString(RootObject):
    __tdlib_type__ = "setCustomLanguagePackString"
    language_pack_id:str = attr.ib()
    new_string:languagePackString = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteLanguagePack(RootObject):
    __tdlib_type__ = "deleteLanguagePack"
    language_pack_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_registerDevice(RootObject):
    __tdlib_type__ = "registerDevice"
    device_token:DeviceToken = attr.ib()
    other_user_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_processPushNotification(RootObject):
    __tdlib_type__ = "processPushNotification"
    payload:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPushReceiverId(RootObject):
    __tdlib_type__ = "getPushReceiverId"
    payload:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getRecentlyVisitedTMeUrls(RootObject):
    __tdlib_type__ = "getRecentlyVisitedTMeUrls"
    referrer:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setUserPrivacySettingRules(RootObject):
    __tdlib_type__ = "setUserPrivacySettingRules"
    setting:UserPrivacySetting = attr.ib()
    rules:userPrivacySettingRules = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getUserPrivacySettingRules(RootObject):
    __tdlib_type__ = "getUserPrivacySettingRules"
    setting:UserPrivacySetting = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getOption(RootObject):
    __tdlib_type__ = "getOption"
    name:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setOption(RootObject):
    __tdlib_type__ = "setOption"
    name:str = attr.ib()
    value:OptionValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setAccountTtl(RootObject):
    __tdlib_type__ = "setAccountTtl"
    ttl:accountTtl = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getAccountTtl(RootObject):
    __tdlib_type__ = "getAccountTtl"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deleteAccount(RootObject):
    __tdlib_type__ = "deleteAccount"
    reason:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatReportSpamState(RootObject):
    __tdlib_type__ = "getChatReportSpamState"
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_changeChatReportSpamState(RootObject):
    __tdlib_type__ = "changeChatReportSpamState"
    chat_id:int = attr.ib()
    is_spam_chat:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_reportChat(RootObject):
    __tdlib_type__ = "reportChat"
    chat_id:int = attr.ib()
    reason:ChatReportReason = attr.ib()
    message_ids:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getChatStatisticsUrl(RootObject):
    __tdlib_type__ = "getChatStatisticsUrl"
    chat_id:int = attr.ib()
    parameters:str = attr.ib()
    is_dark:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getStorageStatistics(RootObject):
    __tdlib_type__ = "getStorageStatistics"
    chat_limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getStorageStatisticsFast(RootObject):
    __tdlib_type__ = "getStorageStatisticsFast"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getDatabaseStatistics(RootObject):
    __tdlib_type__ = "getDatabaseStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_optimizeStorage(RootObject):
    __tdlib_type__ = "optimizeStorage"
    size:int = attr.ib()
    ttl:int = attr.ib()
    count:int = attr.ib()
    immunity_delay:int = attr.ib()
    file_types:typing.Sequence[FileType] = attr.ib()
    chat_ids:typing.Sequence[int] = attr.ib()
    exclude_chat_ids:typing.Sequence[int] = attr.ib()
    chat_limit:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setNetworkType(RootObject):
    __tdlib_type__ = "setNetworkType"
    type:NetworkType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getNetworkStatistics(RootObject):
    __tdlib_type__ = "getNetworkStatistics"
    only_current:bool = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addNetworkStatistics(RootObject):
    __tdlib_type__ = "addNetworkStatistics"
    entry:NetworkStatisticsEntry = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resetNetworkStatistics(RootObject):
    __tdlib_type__ = "resetNetworkStatistics"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getAutoDownloadSettingsPresets(RootObject):
    __tdlib_type__ = "getAutoDownloadSettingsPresets"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setAutoDownloadSettings(RootObject):
    __tdlib_type__ = "setAutoDownloadSettings"
    settings:autoDownloadSettings = attr.ib()
    type:NetworkType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPassportElement(RootObject):
    __tdlib_type__ = "getPassportElement"
    type:PassportElementType = attr.ib()
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getAllPassportElements(RootObject):
    __tdlib_type__ = "getAllPassportElements"
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setPassportElement(RootObject):
    __tdlib_type__ = "setPassportElement"
    element:InputPassportElement = attr.ib()
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_deletePassportElement(RootObject):
    __tdlib_type__ = "deletePassportElement"
    type:PassportElementType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setPassportElementErrors(RootObject):
    __tdlib_type__ = "setPassportElementErrors"
    user_id:int = attr.ib()
    errors:typing.Sequence[inputPassportElementError] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPreferredCountryLanguage(RootObject):
    __tdlib_type__ = "getPreferredCountryLanguage"
    country_code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendPhoneNumberVerificationCode(RootObject):
    __tdlib_type__ = "sendPhoneNumberVerificationCode"
    phone_number:str = attr.ib()
    settings:phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendPhoneNumberVerificationCode(RootObject):
    __tdlib_type__ = "resendPhoneNumberVerificationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkPhoneNumberVerificationCode(RootObject):
    __tdlib_type__ = "checkPhoneNumberVerificationCode"
    code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendEmailAddressVerificationCode(RootObject):
    __tdlib_type__ = "sendEmailAddressVerificationCode"
    email_address:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendEmailAddressVerificationCode(RootObject):
    __tdlib_type__ = "resendEmailAddressVerificationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkEmailAddressVerificationCode(RootObject):
    __tdlib_type__ = "checkEmailAddressVerificationCode"
    code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPassportAuthorizationForm(RootObject):
    __tdlib_type__ = "getPassportAuthorizationForm"
    bot_user_id:int = attr.ib()
    scope:str = attr.ib()
    public_key:str = attr.ib()
    nonce:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getPassportAuthorizationFormAvailableElements(RootObject):
    __tdlib_type__ = "getPassportAuthorizationFormAvailableElements"
    autorization_form_id:int = attr.ib()
    password:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendPassportAuthorizationForm(RootObject):
    __tdlib_type__ = "sendPassportAuthorizationForm"
    autorization_form_id:int = attr.ib()
    types:typing.Sequence[PassportElementType] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendPhoneNumberConfirmationCode(RootObject):
    __tdlib_type__ = "sendPhoneNumberConfirmationCode"
    hash:str = attr.ib()
    phone_number:str = attr.ib()
    settings:phoneNumberAuthenticationSettings = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_resendPhoneNumberConfirmationCode(RootObject):
    __tdlib_type__ = "resendPhoneNumberConfirmationCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_checkPhoneNumberConfirmationCode(RootObject):
    __tdlib_type__ = "checkPhoneNumberConfirmationCode"
    code:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setBotUpdatesStatus(RootObject):
    __tdlib_type__ = "setBotUpdatesStatus"
    pending_update_count:int = attr.ib()
    error_message:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_uploadStickerFile(RootObject):
    __tdlib_type__ = "uploadStickerFile"
    user_id:int = attr.ib()
    png_sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_createNewStickerSet(RootObject):
    __tdlib_type__ = "createNewStickerSet"
    user_id:int = attr.ib()
    title:str = attr.ib()
    name:str = attr.ib()
    is_masks:bool = attr.ib()
    stickers:typing.Sequence[inputSticker] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addStickerToSet(RootObject):
    __tdlib_type__ = "addStickerToSet"
    user_id:int = attr.ib()
    name:str = attr.ib()
    sticker:inputSticker = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setStickerPositionInSet(RootObject):
    __tdlib_type__ = "setStickerPositionInSet"
    sticker:InputFile = attr.ib()
    position:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeStickerFromSet(RootObject):
    __tdlib_type__ = "removeStickerFromSet"
    sticker:InputFile = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getMapThumbnailFile(RootObject):
    __tdlib_type__ = "getMapThumbnailFile"
    location:location = attr.ib()
    zoom:int = attr.ib()
    width:int = attr.ib()
    height:int = attr.ib()
    scale:int = attr.ib()
    chat_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_acceptTermsOfService(RootObject):
    __tdlib_type__ = "acceptTermsOfService"
    terms_of_service_id:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendCustomRequest(RootObject):
    __tdlib_type__ = "sendCustomRequest"
    method:str = attr.ib()
    parameters:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_answerCustomQuery(RootObject):
    __tdlib_type__ = "answerCustomQuery"
    custom_query_id:int = attr.ib()
    data:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_sendTonLiteServerRequest(RootObject):
    __tdlib_type__ = "sendTonLiteServerRequest"
    request:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getTonWalletPasswordSalt(RootObject):
    __tdlib_type__ = "getTonWalletPasswordSalt"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setAlarm(RootObject):
    __tdlib_type__ = "setAlarm"
    seconds:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getCountryCode(RootObject):
    __tdlib_type__ = "getCountryCode"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getInviteText(RootObject):
    __tdlib_type__ = "getInviteText"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getDeepLinkInfo(RootObject):
    __tdlib_type__ = "getDeepLinkInfo"
    link:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getApplicationConfig(RootObject):
    __tdlib_type__ = "getApplicationConfig"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_saveApplicationLogEvent(RootObject):
    __tdlib_type__ = "saveApplicationLogEvent"
    type:str = attr.ib()
    chat_id:int = attr.ib()
    data:JsonValue = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addProxy(RootObject):
    __tdlib_type__ = "addProxy"
    server:str = attr.ib()
    port:int = attr.ib()
    enable:bool = attr.ib()
    type:ProxyType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_editProxy(RootObject):
    __tdlib_type__ = "editProxy"
    proxy_id:int = attr.ib()
    server:str = attr.ib()
    port:int = attr.ib()
    enable:bool = attr.ib()
    type:ProxyType = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_enableProxy(RootObject):
    __tdlib_type__ = "enableProxy"
    proxy_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_disableProxy(RootObject):
    __tdlib_type__ = "disableProxy"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_removeProxy(RootObject):
    __tdlib_type__ = "removeProxy"
    proxy_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getProxies(RootObject):
    __tdlib_type__ = "getProxies"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getProxyLink(RootObject):
    __tdlib_type__ = "getProxyLink"
    proxy_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_pingProxy(RootObject):
    __tdlib_type__ = "pingProxy"
    proxy_id:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setLogStream(RootObject):
    __tdlib_type__ = "setLogStream"
    log_stream:LogStream = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLogStream(RootObject):
    __tdlib_type__ = "getLogStream"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setLogVerbosityLevel(RootObject):
    __tdlib_type__ = "setLogVerbosityLevel"
    new_verbosity_level:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLogVerbosityLevel(RootObject):
    __tdlib_type__ = "getLogVerbosityLevel"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLogTags(RootObject):
    __tdlib_type__ = "getLogTags"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_setLogTagVerbosityLevel(RootObject):
    __tdlib_type__ = "setLogTagVerbosityLevel"
    tag:str = attr.ib()
    new_verbosity_level:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_getLogTagVerbosityLevel(RootObject):
    __tdlib_type__ = "getLogTagVerbosityLevel"
    tag:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_addLogMessage(RootObject):
    __tdlib_type__ = "addLogMessage"
    verbosity_level:int = attr.ib()
    text:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallEmpty(RootObject):
    __tdlib_type__ = "testCallEmpty"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallString(RootObject):
    __tdlib_type__ = "testCallString"
    x:str = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallBytes(RootObject):
    __tdlib_type__ = "testCallBytes"
    x:bytes = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallVectorInt(RootObject):
    __tdlib_type__ = "testCallVectorInt"
    x:typing.Sequence[int] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallVectorIntObject(RootObject):
    __tdlib_type__ = "testCallVectorIntObject"
    x:typing.Sequence[testInt] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallVectorString(RootObject):
    __tdlib_type__ = "testCallVectorString"
    x:typing.Sequence[str] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testCallVectorStringObject(RootObject):
    __tdlib_type__ = "testCallVectorStringObject"
    x:typing.Sequence[testString] = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testSquareInt(RootObject):
    __tdlib_type__ = "testSquareInt"
    x:int = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testNetwork(RootObject):
    __tdlib_type__ = "testNetwork"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testProxy(RootObject):
    __tdlib_type__ = "testProxy"
    server:str = attr.ib()
    port:int = attr.ib()
    type:ProxyType = attr.ib()
    dc_id:int = attr.ib()
    timeout:decimal.Decimal = attr.ib()


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testGetDifference(RootObject):
    __tdlib_type__ = "testGetDifference"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testUseUpdate(RootObject):
    __tdlib_type__ = "testUseUpdate"


@attr.s(auto_attribs=True, frozen=True, kw_only=True)
class tdlib_func_testReturnError(RootObject):
    __tdlib_type__ = "testReturnError"
    error:error = attr.ib()


