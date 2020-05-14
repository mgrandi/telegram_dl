# unit test stuff


## message, channel post

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 341835776,
    "sender_user_id": 0,
    "chat_id": -1001369510863,
    "sending_state": null,
    "scheduling_state": null,
    "is_outgoing": false,
    "can_be_edited": false,
    "can_be_forwarded": true,
    "can_be_deleted_only_for_self": false,
    "can_be_deleted_for_all_users": false,
    "is_channel_post": true,
    "contains_unread_mention": false,
    "date": 1589210415,
    "edit_date": 0,
    "forward_info": null,
    "reply_to_message_id": 0,
    "ttl": 0,
    "ttl_expires_in": "0",
    "via_bot_user_id": 0,
    "author_signature": "",
    "views": 31,
    "media_album_id": 0,
    "restriction_reason": "",
    "content": {
      "_extra": null,
      "text": {
        "_extra": null,
        "text": "*concern*",
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

## message , text entity variations
```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 35651584,
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
    "date": 1589414963,
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
        "text": "Testing 123 @AuroraPenguin BOLD ITALIC underline STRIKE monospaced $USD #hey",
        "entities": [
          {
            "_extra": null,
            "offset": 12,
            "length": 14,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeMention"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 27,
            "length": 4,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeBold"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 32,
            "length": 6,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeItalic"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 39,
            "length": 9,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeUnderline"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 49,
            "length": 6,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeStrikethrough"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 56,
            "length": 10,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeCode"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 67,
            "length": 4,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeCashtag"
            },
            "@type": "textEntity"
          },
          {
            "_extra": null,
            "offset": 72,
            "length": 4,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeHashtag"
            },
            "@type": "textEntity"
          }
        ],
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