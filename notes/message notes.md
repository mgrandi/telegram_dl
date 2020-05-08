# `message` type notes

## Messages

`updateNewMessage`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_new_message.html

`message`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message.html

messages usually come from the `updateNewMessage` object, which contains a `message` object, and inside the `message` object
is a `content` member that is of type `MessageContent`

## Contents of messages

`MessageContent` (superclasss): https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_message_content.html

`messageAnimation`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_animation.html
`messageAudio`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_audio.html
`messageBasicGroupChatCreate`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_basic_group_chat_create.html
`messageCall`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_call.html
`messageChatAddMembers`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_add_members.html
`messageChatChangePhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_change_photo.html
`messageChatChangeTitle`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_change_title.html
`messageChatDeleteMember`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_delete_member.html
`messageChatDeletePhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_delete_photo.html
`messageChatJoinByLink`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_join_by_link.html
`messageChatSetTtl`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_set_ttl.html
`messageChatUpgradeFrom`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_upgrade_from.html
`messageChatUpgradeTo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_chat_upgrade_to.html
`messageContact`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_contact.html
`messageContactRegistered`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_contact_registered.html
`messageCustomServiceAction`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_custom_service_action.html
`messageDocument`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_document.html
`messageExpiredPhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_expired_photo.html
`messageExpiredVideo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_expired_video.html
`messageGame`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_game.html
`messageGameScore`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_game_score.html
`messageInvoice`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_invoice.html
`messageLocation`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_location.html
`messagePassportDataReceived`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_passport_data_received.html
`messagePassportDataSent`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_passport_data_sent.html
`messagePaymentSuccessful`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_payment_successful.html
`messagePaymentSuccessfulBot`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_payment_successful_bot.html
`messagePhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_photo.html
`messagePinMessage`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_pin_message.html
`messagePoll`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_poll.html
`messageScreenshotTaken`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_screenshot_taken.html
`messageSticker`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_sticker.html
`messageSupergroupChatCreate`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_supergroup_chat_create.html
`messageText`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_text.html
`messageUnsupported`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_unsupported.html
`messageVenue`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_venue.html
`messageVideo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_video.html
`messageVideoNote`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_video_note.html
`messageVoiceNote`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_voice_note.html


## message docs copy and paste

```plaintext
std::int64_t  id_
  Message identifier, unique for the chat to which the message belongs.

std::int32_t  sender_user_id_
  Identifier of the user who sent the message; 0 if unknown. Currently, it is unknown for channel posts and for channel posts automatically forwarded to discussion group.

std::int64_t  chat_id_
  Chat identifier.

object_ptr< MessageSendingState >   sending_state_
  Information about the sending state of the message; may be null.

object_ptr< MessageSchedulingState >  scheduling_state_
  Information about the scheduling state of the message; may be null.

bool  is_outgoing_
  True, if the message is outgoing.

bool  can_be_edited_
  True, if the message can be edited. For live location and poll messages this fields shows whether editMessageLiveLocation or stopPoll can be used with this message by the client.

bool  can_be_forwarded_
  True, if the message can be forwarded.

bool  can_be_deleted_only_for_self_
  True, if the message can be deleted only for the current user while other users will continue to see it.

bool  can_be_deleted_for_all_users_
  True, if the message can be deleted for all users.

bool  is_channel_post_
  True, if the message is a channel post. All messages to channels are channel posts, all other messages are not channel posts.

bool  contains_unread_mention_
  True, if the message contains an unread mention for the current user.

std::int32_t  date_
  Point in time (Unix timestamp) when the message was sent.

std::int32_t  edit_date_
  Point in time (Unix timestamp) when the message was last edited.

object_ptr< messageForwardInfo >  forward_info_
  Information about the initial message sender; may be null.

std::int64_t  reply_to_message_id_
  If non-zero, the identifier of the message this message is replying to; can be the identifier of a deleted message.

std::int32_t  ttl_
  For self-destructing messages, the message's TTL (Time To Live), in seconds; 0 if none. TDLib will send updateDeleteMessages or updateMessageContent once the TTL expires.

double  ttl_expires_in_
  Time left before the message expires, in seconds.

std::int32_t  via_bot_user_id_
  If non-zero, the user identifier of the bot through which this message was sent.

std::string   author_signature_
  For channel posts, optional author signature.

std::int32_t  views_
  Number of times this message was viewed.

std::int64_t  media_album_id_
  Unique identifier of an album this message belongs to. Only photos and videos can be grouped together in albums.

std::string   restriction_reason_
  If non-empty, contains a human-readable description of the reason why access to this message must be restricted.

object_ptr< MessageContent >  content_
  Content of the message.

object_ptr< ReplyMarkup >   reply_markup_
  Reply markup for the message; may be null.

```


## stuff messages contain

`photo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html

`messageForwardInfo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_forward_info.html

## message content

### `messageAnimation`

these are GIFS, if you right click a gif and click "save to gifs" it calls `updateSavedAnimations` with the `id` of the `animation` object

```json
{
  "_extra": null,
  "chat_id": 678406,
  "last_message": {
    "_extra": null,
    "id": 17825792,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588224944,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "animation": {
        "_extra": null,
        "duration": 3,
        "width": 354,
        "height": 274,
        "file_name": "tenor.gif.mp4",
        "mime_type": "video/mp4",
        "minithumbnail": {
          "_extra": null,
          "width": 40,
          "height": 31,
          "data": "LzlqLzRBQVFTa1pKUmdBQkFRQUFBUUFCQUFELzJ3QkRBQ2djSGlNZUdTZ2pJU010S3lnd1BHUkJQRGMzUEh0WVhVbGtrWUNabG8rQWpJcWd0T2JEb0tyYXJZcU15UC9MMnU3MS8vLy9tOEgvLy8vNi8rYjkvL2ovMndCREFTc3RMVHcxUEhaQlFYYjRwWXlsK1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQai93QUFSQ0FBZkFDZ0RBU0lBQWhFQkF4RUIvOFFBSHdBQUFRVUJBUUVCQVFFQUFBQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkFBQWdFREF3SUVBd1VGQkFRQUFBRjlBUUlEQUFRUkJSSWhNVUVHRTFGaEJ5SnhGREtCa2FFSUkwS3h3UlZTMGZBa00ySnlnZ2tLRmhjWUdSb2xKaWNvS1NvME5UWTNPRGs2UTBSRlJrZElTVXBUVkZWV1YxaFpXbU5rWldabmFHbHFjM1IxZG5kNGVYcURoSVdHaDRpSmlwS1RsSldXbDVpWm1xS2pwS1dtcDZpcHFyS3p0TFcydDdpNXVzTER4TVhHeDhqSnl0TFQxTlhXMTlqWjJ1SGk0K1RsNXVmbzZlcng4dlAwOWZiMytQbjYvOFFBSHdFQUF3RUJBUUVCQVFFQkFRQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkVBQWdFQ0JBUURCQWNGQkFRQUFRSjNBQUVDQXhFRUJTRXhCaEpCVVFkaGNSTWlNb0VJRkVLUm9iSEJDU016VXZBVlluTFJDaFlrTk9FbDhSY1lHUm9tSnlncEtqVTJOemc1T2tORVJVWkhTRWxLVTFSVlZsZFlXVnBqWkdWbVoyaHBhbk4wZFhaM2VIbDZnb09FaFlhSGlJbUtrcE9VbFphWG1KbWFvcU9rcGFhbnFLbXFzck8wdGJhM3VMbTZ3c1BFeGNiSHlNbkswdFBVMWRiWDJObmE0dVBrNWVibjZPbnE4dlAwOWZiMytQbjYvOW9BREFNQkFBSVJBeEVBUHdDQm1MTUF2VTFlK3lSaUVEY3dZOUNlbWFvcEcvbktlQnlLdFJCbWtaUVRndGsxTGRpMHJsWGM4YVNLMlEzSXhTcTRDZ210Vnl2UmxERG9Od3pWTzh0UTBEUEd1MWh5VkhRMGN3ckZacEZLOGNqMG9xb0NSMUJvcGdhUi9XbXM3SzRJNzgwOEFuQnhrSDNxSXR2bDI0MmR2V2hxNEoyTE16a3hLYzRKUFdwN2VkU0Fqam1xY3hEVExFSENvb3p1SXpuOEtrU2VFTmdieHdlVFVXWTdvaHVyY1JQOG95amRLS1RkS3liWkd5S0swSlAvMlE9PQ==",
          "@type": "minithumbnail"
        },
        "thumbnail": {
          "_extra": null,
          "type": "m",
          "photo": {
            "_extra": null,
            "id": 26,
            "size": 23316,
            "expected_size": 23316,
            "local": {
              "_extra": null,
              "path": "",
              "can_be_downloaded": true,
              "can_be_deleted": false,
              "is_downloading_active": false,
              "is_downloading_completed": false,
              "download_offset": 0,
              "downloaded_prefix_size": 0,
              "downloaded_size": 0,
              "@type": "localFile"
            },
            "remote": {
              "_extra": null,
              "id": "AAMCAQADGQEAAxFeqmNv1gqiNKsJWX8XwHfPRIzMJAACAgADkrRRRVxW289ZITDHYUnskC4AAwEAB20AA0kFAAIYBA",
              "unique_id": "AQADYUnskC4AA0kFAAI",
              "is_uploading_active": false,
              "is_uploading_completed": true,
              "uploaded_size": 23316,
              "@type": "remoteFile"
            },
            "@type": "file"
          },
          "width": 320,
          "height": 248,
          "@type": "photoSize"
        },
        "animation": {
          "_extra": null,
          "id": 27,
          "size": 232271,
          "expected_size": 232271,
          "local": {
            "_extra": null,
            "path": "",
            "can_be_downloaded": true,
            "can_be_deleted": false,
            "is_downloading_active": false,
            "is_downloading_completed": false,
            "download_offset": 0,
            "downloaded_prefix_size": 0,
            "downloaded_size": 0,
            "@type": "localFile"
          },
          "remote": {
            "_extra": null,
            "id": "CgACAgEAAxkBAAMRXqpjb9YKojSrCVl_F8B3z0SMzCQAAgIAA5K0UUVcVtvPWSEwxxgE",
            "unique_id": "AgADAgADkrRRRQ",
            "is_uploading_active": false,
            "is_uploading_completed": true,
            "uploaded_size": 232271,
            "@type": "remoteFile"
          },
          "@type": "file"
        },
        "@type": "animation"
      },
      "caption": {
        "_extra": null,
        "text": "",
        "entities": [],
        "@type": "formattedText"
      },
      "is_secret": false,
      "@type": "messageAnimation"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821374193171431000,
  "@type": "updateChatLastMessage"
}
```

#### `updateSavedAnimations`

```json
{
  "_extra": null,
  "animation_ids": [
    27
  ],
  "@type": "updateSavedAnimations"
}
```

### `messageAudio`

```json

```

### `messageBasicGroupChatCreate`

```json
{
  "_extra": null,
  "chat_id": -356102,
  "last_message": {
    "_extra": null,
    "id": 30408704,
    "sender_user_id": 678406,
    "chat_id": -356102,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": false,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588228575,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "title": "PenguinTestGroup",
      "member_user_ids": [
        678406,
        369973
      ],
      "@type": "messageBasicGroupChatCreate"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821389788197683000,
  "@type": "updateChatLastMessage"
}
```

### `messageCall`

```json

```

### `messageChatAddMembers`

```json

```

### `messageChatChangePhoto`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 2097152,
    "sender_user_id": 0,
    "chat_id": -1000010597257,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": false,
    "can_be_deleted_only_for_self": false,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": true,
    "contains_unread_mention": false,
    "date": 1588227392,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "photo": {
        "_extra": null,
        "has_stickers": false,
        "minithumbnail": null,
        "sizes": [
          {
            "_extra": null,
            "type": "a",
            "photo": {
              "_extra": null,
              "id": 10,
              "size": 11622,
              "expected_size": 11622,
              "local": {
                "_extra": null,
                "path": "",
                "can_be_downloaded": true,
                "can_be_deleted": false,
                "is_downloading_active": false,
                "is_downloading_completed": false,
                "download_offset": 0,
                "downloaded_prefix_size": 0,
                "downloaded_size": 0,
                "@type": "localFile"
              },
              "remote": {
                "_extra": null,
                "id": "AgACAgEAAx0EAAGhs4kAAwJeqm1DO7IdOs5WEa3n6o9lp_i_DAACqacxGzeSWUUbEy5NX2UTkWFJ7JAuAAMBAAMCAANhAANQBQACGAQ",
                "unique_id": "AQADYUnskC4AA1AFAAI",
                "is_uploading_active": false,
                "is_uploading_completed": true,
                "uploaded_size": 11622,
                "@type": "remoteFile"
              },
              "@type": "file"
            },
            "width": 160,
            "height": 160,
            "@type": "photoSize"
          },
          {
            "_extra": null,
            "type": "b",
            "photo": {
              "_extra": null,
              "id": 11,
              "size": 28541,
              "expected_size": 28541,
              "local": {
                "_extra": null,
                "path": "",
                "can_be_downloaded": true,
                "can_be_deleted": false,
                "is_downloading_active": false,
                "is_downloading_completed": false,
                "download_offset": 0,
                "downloaded_prefix_size": 0,
                "downloaded_size": 0,
                "@type": "localFile"
              },
              "remote": {
                "_extra": null,
                "id": "AgACAgEAAx0EAAGhs4kAAwJeqm1DO7IdOs5WEa3n6o9lp_i_DAACqacxGzeSWUUbEy5NX2UTkWFJ7JAuAAMBAAMCAANiAANRBQACGAQ",
                "unique_id": "AQADYUnskC4AA1EFAAI",
                "is_uploading_active": false,
                "is_uploading_completed": true,
                "uploaded_size": 28541,
                "@type": "remoteFile"
              },
              "@type": "file"
            },
            "width": 320,
            "height": 320,
            "@type": "photoSize"
          },
          {
            "_extra": null,
            "type": "c",
            "photo": {
              "_extra": null,
              "id": 12,
              "size": 67752,
              "expected_size": 67752,
              "local": {
                "_extra": null,
                "path": "",
                "can_be_downloaded": true,
                "can_be_deleted": false,
                "is_downloading_active": false,
                "is_downloading_completed": false,
                "download_offset": 0,
                "downloaded_prefix_size": 0,
                "downloaded_size": 0,
                "@type": "localFile"
              },
              "remote": {
                "_extra": null,
                "id": "AgACAgEAAx0EAAGhs4kAAwJeqm1DO7IdOs5WEa3n6o9lp_i_DAACqacxGzeSWUUbEy5NX2UTkWFJ7JAuAAMBAAMCAANjAANSBQACGAQ",
                "unique_id": "AQADYUnskC4AA1IFAAI",
                "is_uploading_active": false,
                "is_uploading_completed": true,
                "uploaded_size": 67752,
                "@type": "remoteFile"
              },
              "@type": "file"
            },
            "width": 640,
            "height": 640,
            "@type": "photoSize"
          }
        ],
        "@type": "photo"
      },
      "@type": "messageChatChangePhoto"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

### `messageChatChangeTitle`

```json
{
  "_extra": null,
  "chat_id": -356102,
  "last_message": {
    "_extra": null,
    "id": 35651584,
    "sender_user_id": 678406,
    "chat_id": -356102,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": false,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588229534,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "title": "PenguinTestGroup 🐧",
      "@type": "messageChatChangeTitle"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821393907071320000,
  "@type": "updateChatLastMessage"
}
```

### `messageChatDeleteMember`

```json

```

### `messageChatDeletePhoto`

```json

```

### `messageChatJoinByLink`

```json

```

### `messageChatSetTtl`

```json

```

### `messageChatUpgradeFrom`

```json

```

### `messageChatUpgradeTo`

```json

```

### `messageContact`

```json
{
  "_extra": null,
  "chat_id": 678406,
  "last_message": {
    "_extra": null,
    "id": 19922944,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588225513,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "contact": {
        "_extra": null,
        "phone_number": "+15555555555",
        "first_name": "john",
        "last_name": "smith",
        "vcard": "",
        "user_id": 678406,
        "@type": "contact"
      },
      "@type": "messageContact"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821376637007823000,
  "@type": "updateChatLastMessage"
}
```

### `messageContactRegistered`

```json

```

### `messageCustomServiceAction`

```json

```

### `messageDocument`


#### audo file uploaded as document

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 18874368,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588225357,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "document": {
        "_extra": null,
        "file_name": "doom2016alarm.wav",
        "mime_type": "audio/x-wav",
        "minithumbnail": null,
        "thumbnail": null,
        "document": {
          "_extra": null,
          "id": 28,
          "size": 182572,
          "expected_size": 182572,
          "local": {
            "_extra": null,
            "path": "",
            "can_be_downloaded": true,
            "can_be_deleted": false,
            "is_downloading_active": false,
            "is_downloading_completed": false,
            "download_offset": 0,
            "downloaded_prefix_size": 0,
            "downloaded_size": 0,
            "@type": "localFile"
          },
          "remote": {
            "_extra": null,
            "id": "BQACAgEAAxkBAAMSXqplTTB_4VucsQ01pQtOqcSCcYwAAgMAA5K0UUV-W9HVBV0LtRgE",
            "unique_id": "AgADAwADkrRRRQ",
            "is_uploading_active": false,
            "is_uploading_completed": true,
            "uploaded_size": 182572,
            "@type": "remoteFile"
          },
          "@type": "file"
        },
        "@type": "document"
      },
      "caption": {
        "_extra": null,
        "text": "",
        "entities": [],
        "@type": "formattedText"
      },
      "@type": "messageDocument"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

#### a photo document (upload without compression)

```json

{
  "_extra": null,
  "chat_id": 678406,
  "last_message": {
    "_extra": null,
    "id": 25165824,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588227153,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "document": {
        "_extra": null,
        "file_name": "PNG-Gradient.png",
        "mime_type": "image/png",
        "minithumbnail": {
          "_extra": null,
          "width": 40,
          "height": 21,
          "data": "LzlqLzRBQVFTa1pKUmdBQkFRQUFBUUFCQUFELzJ3QkRBQ2djSGlNZUdTZ2pJU010S3lnd1BHUkJQRGMzUEh0WVhVbGtrWUNabG8rQWpJcWd0T2JEb0tyYXJZcU15UC9MMnU3MS8vLy9tOEgvLy8vNi8rYjkvL2ovMndCREFTc3RMVHcxUEhaQlFYYjRwWXlsK1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQai93QUFSQ0FBVkFDZ0RBU0lBQWhFQkF4RUIvOFFBSHdBQUFRVUJBUUVCQVFFQUFBQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkFBQWdFREF3SUVBd1VGQkFRQUFBRjlBUUlEQUFRUkJSSWhNVUVHRTFGaEJ5SnhGREtCa2FFSUkwS3h3UlZTMGZBa00ySnlnZ2tLRmhjWUdSb2xKaWNvS1NvME5UWTNPRGs2UTBSRlJrZElTVXBUVkZWV1YxaFpXbU5rWldabmFHbHFjM1IxZG5kNGVYcURoSVdHaDRpSmlwS1RsSldXbDVpWm1xS2pwS1dtcDZpcHFyS3p0TFcydDdpNXVzTER4TVhHeDhqSnl0TFQxTlhXMTlqWjJ1SGk0K1RsNXVmbzZlcng4dlAwOWZiMytQbjYvOFFBSHdFQUF3RUJBUUVCQVFFQkFRQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkVBQWdFQ0JBUURCQWNGQkFRQUFRSjNBQUVDQXhFRUJTRXhCaEpCVVFkaGNSTWlNb0VJRkVLUm9iSEJDU016VXZBVlluTFJDaFlrTk9FbDhSY1lHUm9tSnlncEtqVTJOemc1T2tORVJVWkhTRWxLVTFSVlZsZFlXVnBqWkdWbVoyaHBhbk4wZFhaM2VIbDZnb09FaFlhSGlJbUtrcE9VbFphWG1KbWFvcU9rcGFhbnFLbXFzck8wdGJhM3VMbTZ3c1BFeGNiSHlNbkswdFBVMWRiWDJObmE0dVBrNWVibjZPbnE4dlAwOWZiMytQbjYvOW9BREFNQkFBSVJBeEVBUHdCZ3A0cVJZbE5UTGJvZXgvT3RQcmRObWp4RUo3RUFwNHF3YmVNTGtaL09vWFVMMHBmV0lNeGxTbFBZVVVWV2VaMTZZb3BlMmlaZjJmVmV1aFlTcDBvb3J6MFowaVUvZHFwTFJSVm85R2tVcGFLS0tzNzQ3SC8vMlE9PQ==",
          "@type": "minithumbnail"
        },
        "thumbnail": {
          "_extra": null,
          "type": "m",
          "photo": {
            "_extra": null,
            "id": 6,
            "size": 1073,
            "expected_size": 1073,
            "local": {
              "_extra": null,
              "path": "",
              "can_be_downloaded": true,
              "can_be_deleted": false,
              "is_downloading_active": false,
              "is_downloading_completed": false,
              "download_offset": 0,
              "downloaded_prefix_size": 0,
              "downloaded_size": 0,
              "@type": "localFile"
            },
            "remote": {
              "_extra": null,
              "id": "AAMCAQADGQEAAxheqmxRbXXwuiYnIH56ep8hC2tdwQACBAADkrRRRRFCaRYkpvlBYUnskC4AAwEAB20AA04FAAIYBA",
              "unique_id": "AQADYUnskC4AA04FAAI",
              "is_uploading_active": false,
              "is_uploading_completed": true,
              "uploaded_size": 1073,
              "@type": "remoteFile"
            },
            "@type": "file"
          },
          "width": 128,
          "height": 68,
          "@type": "photoSize"
        },
        "document": {
          "_extra": null,
          "id": 7,
          "size": 251,
          "expected_size": 251,
          "local": {
            "_extra": null,
            "path": "",
            "can_be_downloaded": true,
            "can_be_deleted": false,
            "is_downloading_active": false,
            "is_downloading_completed": false,
            "download_offset": 0,
            "downloaded_prefix_size": 0,
            "downloaded_size": 0,
            "@type": "localFile"
          },
          "remote": {
            "_extra": null,
            "id": "BQACAgEAAxkBAAMYXqpsUW118LomJyB-enqfIQtrXcEAAgQAA5K0UUURQmkWJKb5QRgE",
            "unique_id": "AgADBAADkrRRRQ",
            "is_uploading_active": false,
            "is_uploading_completed": true,
            "uploaded_size": 251,
            "@type": "remoteFile"
          },
          "@type": "file"
        },
        "@type": "document"
      },
      "caption": {
        "_extra": null,
        "text": "",
        "entities": [],
        "@type": "formattedText"
      },
      "@type": "messageDocument"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821383680754188000,
  "@type": "updateChatLastMessage"
}
```

### `messageExpiredPhoto`

```json

```

### `messageExpiredVideo`

```json

```

### `messageGame`

```json

```

### `messageGameScore`

```json

```

### `messageInvoice`

```json

```

### `messageLocation`

```json

```

### `messagePassportDataReceived`

```json

```

### `messagePassportDataSent`

```json

```

### `messagePaymentSuccessful`

```json

```

### `messagePaymentSuccessfulBot`

```json

```

### `messagePhoto`

```json
{
  "_extra": null,
  "chat_id": 678406,
  "last_message": {
    "_extra": null,
    "id": 24117248,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588227053,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "photo": {
        "_extra": null,
        "has_stickers": false,
        "minithumbnail": {
          "_extra": null,
          "width": 40,
          "height": 21,
          "data": "LzlqLzRBQVFTa1pKUmdBQkFRQUFBUUFCQUFELzJ3QkRBQ2djSGlNZUdTZ2pJU010S3lnd1BHUkJQRGMzUEh0WVhVbGtrWUNabG8rQWpJcWd0T2JEb0tyYXJZcU15UC9MMnU3MS8vLy9tOEgvLy8vNi8rYjkvL2ovMndCREFTc3RMVHcxUEhaQlFYYjRwWXlsK1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQai93QUFSQ0FBVkFDZ0RBU0lBQWhFQkF4RUIvOFFBSHdBQUFRVUJBUUVCQVFFQUFBQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkFBQWdFREF3SUVBd1VGQkFRQUFBRjlBUUlEQUFRUkJSSWhNVUVHRTFGaEJ5SnhGREtCa2FFSUkwS3h3UlZTMGZBa00ySnlnZ2tLRmhjWUdSb2xKaWNvS1NvME5UWTNPRGs2UTBSRlJrZElTVXBUVkZWV1YxaFpXbU5rWldabmFHbHFjM1IxZG5kNGVYcURoSVdHaDRpSmlwS1RsSldXbDVpWm1xS2pwS1dtcDZpcHFyS3p0TFcydDdpNXVzTER4TVhHeDhqSnl0TFQxTlhXMTlqWjJ1SGk0K1RsNXVmbzZlcng4dlAwOWZiMytQbjYvOFFBSHdFQUF3RUJBUUVCQVFFQkFRQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkVBQWdFQ0JBUURCQWNGQkFRQUFRSjNBQUVDQXhFRUJTRXhCaEpCVVFkaGNSTWlNb0VJRkVLUm9iSEJDU016VXZBVlluTFJDaFlrTk9FbDhSY1lHUm9tSnlncEtqVTJOemc1T2tORVJVWkhTRWxLVTFSVlZsZFlXVnBqWkdWbVoyaHBhbk4wZFhaM2VIbDZnb09FaFlhSGlJbUtrcE9VbFphWG1KbWFvcU9rcGFhbnFLbXFzck8wdGJhM3VMbTZ3c1BFeGNiSHlNbkswdFBVMWRiWDJObmE0dVBrNWVibjZPbnE4dlAwOWZiMytQbjYvOW9BREFNQkFBSVJBeEVBUHdCZ3A0cVJZbE5UTGJvZTM2MXA5YXBzMGVJaFBZZ0ZQRldEYnhoYzgvblVMZ0wwcGZXSU14ZEtVOWhSUlZaNW5YcGlpbDdhSm04dnF2WFFzSlU2VVVWNTZNcVJLZnUxVWxvb3EwZWpTS1V0RkZGVWQ4ZGovOWs9",
          "@type": "minithumbnail"
        },
        "sizes": [
          {
            "_extra": null,
            "type": "m",
            "photo": {
              "_extra": null,
              "id": 5,
              "size": 1174,
              "expected_size": 1174,
              "local": {
                "_extra": null,
                "path": "",
                "can_be_downloaded": true,
                "can_be_deleted": false,
                "is_downloading_active": false,
                "is_downloading_completed": false,
                "download_offset": 0,
                "downloaded_prefix_size": 0,
                "downloaded_size": 0,
                "@type": "localFile"
              },
              "remote": {
                "_extra": null,
                "id": "AgACAgEAAxkBAAMXXqpr7A1SOst4fhW2qjvutcrdgjgAAqmnMRuStFFFcw5KBGoq_cBhSeyQLgADAQADAgADbQADTAUAAhgE",
                "unique_id": "AQADYUnskC4AA0wFAAI",
                "is_uploading_active": false,
                "is_uploading_completed": true,
                "uploaded_size": 1174,
                "@type": "remoteFile"
              },
              "@type": "file"
            },
            "width": 128,
            "height": 68,
            "@type": "photoSize"
          }
        ],
        "@type": "photo"
      },
      "caption": {
        "_extra": null,
        "text": "",
        "entities": [],
        "@type": "formattedText"
      },
      "is_secret": false,
      "@type": "messagePhoto"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821383251257459000,
  "@type": "updateChatLastMessage"
}
```

### `messagePinMessage`

```json

```

### `messagePoll`

#### creating

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 36700160,
    "sender_user_id": 678406,
    "chat_id": -356102,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588229614,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "poll": {
        "_extra": null,
        "id": 4994759266863677000,
        "question": "Is this a penguin 🐧",
        "options": [
          {
            "_extra": null,
            "text": "yes",
            "voter_count": 0,
            "vote_percentage": 0,
            "is_chosen": false,
            "is_being_chosen": false,
            "@type": "pollOption"
          },
          {
            "_extra": null,
            "text": "no",
            "voter_count": 0,
            "vote_percentage": 0,
            "is_chosen": false,
            "is_being_chosen": false,
            "@type": "pollOption"
          }
        ],
        "total_voter_count": 0,
        "recent_voter_user_ids": [],
        "is_anonymous": true,
        "type": {
          "_extra": null,
          "allow_multiple_answers": false,
          "@type": "pollTypeRegular"
        },
        "is_closed": false,
        "@type": "poll"
      },
      "@type": "messagePoll"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

#### after voting
```json
{
  "_extra": null,
  "chat_id": -356102,
  "last_message": {
    "_extra": null,
    "id": 36700160,
    "sender_user_id": 678406,
    "chat_id": -356102,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588229614,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "poll": {
        "_extra": null,
        "id": 4994759266863677000,
        "question": "Is this a penguin 🐧",
        "options": [
          {
            "_extra": null,
            "text": "yes",
            "voter_count": 1,
            "vote_percentage": 100,
            "is_chosen": true,
            "is_being_chosen": false,
            "@type": "pollOption"
          },
          {
            "_extra": null,
            "text": "no",
            "voter_count": 0,
            "vote_percentage": 0,
            "is_chosen": false,
            "is_being_chosen": false,
            "@type": "pollOption"
          }
        ],
        "total_voter_count": 1,
        "recent_voter_user_ids": [],
        "is_anonymous": true,
        "type": {
          "_extra": null,
          "allow_multiple_answers": false,
          "@type": "pollTypeRegular"
        },
        "is_closed": false,
        "@type": "poll"
      },
      "@type": "messagePoll"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821394250668704000,
  "@type": "updateChatLastMessage"
}
```


### `messageScreenshotTaken`

```json

```

### `messageSticker`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 20971520,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588226806,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "sticker": {
        "_extra": null,
        "set_id": 1258816259751954,
        "width": 512,
        "height": 310,
        "emoji": "❤",
        "is_animated": true,
        "is_mask": false,
        "mask_position": null,
        "thumbnail": {
          "_extra": null,
          "type": "m",
          "photo": {
            "_extra": null,
            "id": 3,
            "size": 2014,
            "expected_size": 2014,
            "local": {
              "_extra": null,
              "path": "",
              "can_be_downloaded": true,
              "can_be_deleted": false,
              "is_downloading_active": false,
              "is_downloading_completed": false,
              "download_offset": 0,
              "downloaded_prefix_size": 0,
              "downloaded_size": 0,
              "@type": "localFile"
            },
            "remote": {
              "_extra": null,
              "id": "AAMCAQADGQEAAxReqmr2SmDPdaYLS0N4PXdQeH-uDQACzAEAAuN4BAABt6ig2_-1vr5gWNkpAAQBAAdtAAM0BQACGAQ",
              "unique_id": "AQADYFjZKQAENAUAAg",
              "is_uploading_active": false,
              "is_uploading_completed": true,
              "uploaded_size": 2014,
              "@type": "remoteFile"
            },
            "@type": "file"
          },
          "width": 128,
          "height": 128,
          "@type": "photoSize"
        },
        "sticker": {
          "_extra": null,
          "id": 4,
          "size": 56208,
          "expected_size": 56208,
          "local": {
            "_extra": null,
            "path": "",
            "can_be_downloaded": true,
            "can_be_deleted": false,
            "is_downloading_active": false,
            "is_downloading_completed": false,
            "download_offset": 0,
            "downloaded_prefix_size": 0,
            "downloaded_size": 0,
            "@type": "localFile"
          },
          "remote": {
            "_extra": null,
            "id": "CAACAgEAAxkBAAMUXqpq9kpgz3WmC0tDeD13UHh_rg0AAswBAALjeAQAAbeooNv_tb6-GAQ",
            "unique_id": "AgADzAEAAuN4BAAB",
            "is_uploading_active": false,
            "is_uploading_completed": true,
            "uploaded_size": 56208,
            "@type": "remoteFile"
          },
          "@type": "file"
        },
        "@type": "sticker"
      },
      "@type": "messageSticker"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

### `messageSupergroupChatCreate`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 1048576,
    "sender_user_id": 0,
    "chat_id": -1000010597257,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": false,
    "can_be_deleted_only_for_self": false,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": true,
    "contains_unread_mention": false,
    "date": 1588227391,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "title": "TestingChannel",
      "@type": "messageSupergroupChatCreate"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

### `messageText`

```json
{
  "_extra": null,
  "chat_id": 678406,
  "last_message": {
    "_extra": null,
    "id": 23068672,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588226866,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "text": {
        "_extra": null,
        "text": "testing 1 2 3",
        "entities": [],
        "@type": "formattedText"
      },
      "web_page": null,
      "@type": "messageText"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 6821382448098574000,
  "@type": "updateChatLastMessage"
}
```

### `messageUnsupported`

```json

```

### `messageVenue`

```json

```

### `messageVideo`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 37748736,
    "sender_user_id": 678406,
    "chat_id": 678406,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1588230111,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "video": {
        "_extra": null,
        "duration": 9,
        "width": 1280,
        "height": 720,
        "file_name": "˗ˏˋ_siins_ˎˊ˗_hm_yeah_@wayneradiotv_1255260182835273731.mp4",
        "mime_type": "video/mp4",
        "has_stickers": false,
        "supports_streaming": true,
        "minithumbnail": {
          "_extra": null,
          "width": 40,
          "height": 22,
          "data": "LzlqLzRBQVFTa1pKUmdBQkFRQUFBUUFCQUFELzJ3QkRBQ2djSGlNZUdTZ2pJU010S3lnd1BHUkJQRGMzUEh0WVhVbGtrWUNabG8rQWpJcWd0T2JEb0tyYXJZcU15UC9MMnU3MS8vLy9tOEgvLy8vNi8rYjkvL2ovMndCREFTc3RMVHcxUEhaQlFYYjRwWXlsK1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQajQrUGo0K1BqNCtQai93QUFSQ0FBV0FDZ0RBU0lBQWhFQkF4RUIvOFFBSHdBQUFRVUJBUUVCQVFFQUFBQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkFBQWdFREF3SUVBd1VGQkFRQUFBRjlBUUlEQUFRUkJSSWhNVUVHRTFGaEJ5SnhGREtCa2FFSUkwS3h3UlZTMGZBa00ySnlnZ2tLRmhjWUdSb2xKaWNvS1NvME5UWTNPRGs2UTBSRlJrZElTVXBUVkZWV1YxaFpXbU5rWldabmFHbHFjM1IxZG5kNGVYcURoSVdHaDRpSmlwS1RsSldXbDVpWm1xS2pwS1dtcDZpcHFyS3p0TFcydDdpNXVzTER4TVhHeDhqSnl0TFQxTlhXMTlqWjJ1SGk0K1RsNXVmbzZlcng4dlAwOWZiMytQbjYvOFFBSHdFQUF3RUJBUUVCQVFFQkFRQUFBQUFBQUFFQ0F3UUZCZ2NJQ1FvTC84UUF0UkVBQWdFQ0JBUURCQWNGQkFRQUFRSjNBQUVDQXhFRUJTRXhCaEpCVVFkaGNSTWlNb0VJRkVLUm9iSEJDU016VXZBVlluTFJDaFlrTk9FbDhSY1lHUm9tSnlncEtqVTJOemc1T2tORVJVWkhTRWxLVTFSVlZsZFlXVnBqWkdWbVoyaHBhbk4wZFhaM2VIbDZnb09FaFlhSGlJbUtrcE9VbFphWG1KbWFvcU9rcGFhbnFLbXFzck8wdGJhM3VMbTZ3c1BFeGNiSHlNbkswdFBVMWRiWDJObmE0dVBrNWVibjZPbnE4dlAwOWZiMytQbjYvOW9BREFNQkFBSVJBeEVBUHdCZ1pWR1Rpa01tN29jQ21xcVNKa3Rqc0tnKytRTTlQeXFtelJNdDdDRTNkalRTd1U0Si9Lb3ZPVmNqUFNsQkQ0eHlPL0ZGdzVydlFrREFuQUhQdlJUSFFsbWtoenRQYWltZ3VTMnVQcy9JQitVbXFtY1VVVW4wQ0tSRzdocFNBb0dLdHNNUEdvNHd1S0tLSWtkU3hHdjdqR2Z1azBVVVZhR2ovOWs9",
          "@type": "minithumbnail"
        },
        "thumbnail": {
          "_extra": null,
          "type": "m",
          "photo": {
            "_extra": null,
            "id": 15,
            "size": 16931,
            "expected_size": 16931,
            "local": {
              "_extra": null,
              "path": "",
              "can_be_downloaded": true,
              "can_be_deleted": false,
              "is_downloading_active": false,
              "is_downloading_completed": false,
              "download_offset": 0,
              "downloaded_prefix_size": 0,
              "downloaded_size": 0,
              "@type": "localFile"
            },
            "remote": {
              "_extra": null,
              "id": "AAMCAQADGQEAAyReqnffCHl-xxqSuBMlRf0v2PqGxgACBQADkrRRRc87YX_3G-D6YUnskC4AAwEAB20AA1MFAAIYBA",
              "unique_id": "AQADYUnskC4AA1MFAAI",
              "is_uploading_active": false,
              "is_uploading_completed": true,
              "uploaded_size": 16931,
              "@type": "remoteFile"
            },
            "@type": "file"
          },
          "width": 320,
          "height": 180,
          "@type": "photoSize"
        },
        "video": {
          "_extra": null,
          "id": 16,
          "size": 750320,
          "expected_size": 750320,
          "local": {
            "_extra": null,
            "path": "",
            "can_be_downloaded": true,
            "can_be_deleted": false,
            "is_downloading_active": false,
            "is_downloading_completed": false,
            "download_offset": 0,
            "downloaded_prefix_size": 0,
            "downloaded_size": 0,
            "@type": "localFile"
          },
          "remote": {
            "_extra": null,
            "id": "BAACAgEAAxkBAAMkXqp33wh5fscakrgTJUX9L9j6hsYAAgUAA5K0UUXPO2F_9xvg-hgE",
            "unique_id": "AgADBQADkrRRRQ",
            "is_uploading_active": false,
            "is_uploading_completed": true,
            "uploaded_size": 750320,
            "@type": "remoteFile"
          },
          "@type": "file"
        },
        "@type": "video"
      },
      "caption": {
        "_extra": null,
        "text": "hm. yeah.",
        "entities": [],
        "@type": "formattedText"
      },
      "is_secret": false,
      "@type": "messageVideo"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```


### `messageVideoNote`

```json

```

### `messageVoiceNote`

```json

```




## database layout

```plaintext
message_version

  as_of -> ArrowType

  date
  edit date

  sending_state
  scheduling_state

  views (PROBABLY DON'T NEED)

  author_signature

  ttl



message

  VERSIONED

  message_id -> integer, pk


  sender_user_id -> integer, FK to user
  chat_id -> integer, FK to chat

  reply_to_message_id -> integer, should this be a FK? might not have the message yet?
    can this change when the message is edited??


  via_bot_user_id -> integer, FK to user maybe?

  is_outgoing (PROBABLY DON'T NEED)

  is_channel_post (PROBABLY DON'T NEED)

  can_edit
  can_forward

  can_be_deleted_only_for_self

  can_be_deleted_for_all_users


  restriction_reason
```

  # STUFF THAT IS MORE COMPLEX THAN JUST A SINGLE FIELD

  content

  foward_info

  reply_markup

  media_album_id


## editing messages

### original message
so if you send a message, you get this:

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 12582912,
    "sender_user_id": 0,
    "chat_id": -1001446368458,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": false,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": true,
    "contains_unread_mention": false,
    "date": 1588897698,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 1,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "text": {
        "_extra": null,
        "text": "testing edit 1 2 3",
        "entities": [],
        "@type": "formattedText"
      },
      "web_page": null,
      "@type": "messageText"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

then if you edit it, you will get probably two separate messages

one will be `updateMessageContent` which seems to just contain the edit,
the other will be just the `updateChatLastMessage` which seems like the full message
again

### edited message `updateMessageContent`

```json
{
  "_extra": null,
  "chat_id": -1001446368458,
  "message_id": 12582912,
  "new_content": {
    "_extra": null,
    "text": {
      "_extra": null,
      "text": "testing edit 1 2 3 this is an edit",
      "entities": [],
      "@type": "formattedText"
    },
    "web_page": null,
    "@type": "messageText"
  },
  "@type": "updateMessageContent"
}
```

### edited message `updateChatLastMessage`

```json
{
  "_extra": null,
  "chat_id": -1001446368458,
  "last_message": {
    "_extra": null,
    "id": 12582912,
    "sender_user_id": 0,
    "chat_id": -1001446368458,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": false,
    "can_be_deleted_for_all_users": true,
    "is_channel_post": true,
    "contains_unread_mention": false,
    "date": 1588897698,
    "edit_date": 1588897703,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 1,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "text": {
        "_extra": null,
        "text": "testing edit 1 2 3 this is an edit",
        "entities": [],
        "@type": "formattedText"
      },
      "web_page": null,
      "@type": "messageText"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "order": 9221294784512000000,
  "@type": "updateChatLastMessage"
}
```