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


## stuff messages contain

`photo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html

`messageForwardInfo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_forward_info.html

## message content

### `messageText`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 123,
    "sender_user_id": 12345,
    "chat_id": 1234567,
    "sending_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1585887938,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "content": {
      "_extra": null,
      "text": {
        "_extra": null,
        "text": "TESTING MESSAGE 1 2 3 4 5",
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

### `messageSticker`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 123,
    "sender_user_id": 12345,
    "chat_id": 1234567,
    "sending_state": null,
    "is_outgoing": true,
    "can_be_edited": false,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1585815178,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "content": {
      "_extra": null,
      "sticker": {
        "_extra": null,
        "set_id": 1391391008142393300,
        "width": 512,
        "height": 512,
        "emoji": "😂",
        "is_animated": true,
        "is_mask": false,
        "mask_position": null,
        "thumbnail": {
          "_extra": null,
          "type": "m",
          "photo": {
            "_extra": null,
            "id": 743,
            "size": 2750,
            "expected_size": 2750,
            "local": {
              "_extra": null,
              "path": "",
              "can_be_downloaded": true,
              "can_be_deleted": false,
              "is_downloading_active": true,
              "is_downloading_completed": false,
              "download_offset": 0,
              "downloaded_prefix_size": 0,
              "downloaded_size": 0,
              "@type": "localFile"
            },
            "remote": {
              "_extra": null,
              "id": "AAQCAAMBAAPANk8TGC5zMKs_LVFIVbgPAAQBAAdtAAOAZQACFgQ",
              "is_uploading_active": false,
              "is_uploading_completed": true,
              "uploaded_size": 2750,
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
          "id": 744,
          "size": 8244,
          "expected_size": 8244,
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
            "id": "CAADAgADAQADwDZPExguczCrPy1RFgQ",
            "is_uploading_active": false,
            "is_uploading_completed": true,
            "uploaded_size": 8244,
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

### `messagePhoto`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 123,
    "sender_user_id": 12345,
    "chat_id": 123456,
    "sending_state": null,
    "is_outgoing": true,
    "can_be_edited": true,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": false,
    "contains_unread_mention": false,
    "date": 1585815193,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 0,
    "media_album_id": 0,
    "content": {
      "_extra": null,
      "photo": {
        "_extra": null,
        "has_stickers": false,
        "minithumbnail": {
          "_extra": null,
          "width": 21,
          "height": 40,
          "data": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDACgcHiMeGSgjISMtKygwPGRBPDc3PHtYXUlkkYCZlo+AjIqgtObDoKrarYqMyP/L2u71////m8H////6/+b9//j/2wBDASstLTw1PHZBQXb4pYyl+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj4+Pj/wAARCAAVACgDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwBgp4qRYlNTLboe361p9aps0eIhPYgFPFWDbxhc8/nULgL0pfWIMxdKU9hRRVZ5nXpiil7aJm8vqvXQsJU6UUV56MqRKfu1Ulooq0ejSKUtFFFUd8dj/9k=",
          "@type": "minithumbnail"
        },
        "sizes": [
          {
            "_extra": null,
            "type": "m",
            "photo": {
              "_extra": null,
              "id": 754,
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
                "id": "AgADAQADr6cxG3n_MEwNWGCFuxTITBh-EjAABAEAAwIAA20AA8EEAAIWBA",
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
  "@type": "updateNewMessage"
}
```