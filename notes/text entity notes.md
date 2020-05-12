# TextEntity notes

## Base Class

`textEntity`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity.html

```plaintext
std::int32_t    offset_
    Offset of the entity in UTF-16 code units.

std::int32_t    length_
    Length of the entity, in UTF-16 code units.

object_ptr< TextEntityType >    type_
    Type of the entity.

```

## TextEntityType

`TextEntityType`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_text_entity_type.html

### Subclasses

`textEntityTypeBold`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_bold.html
`textEntityTypeBotCommand`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_bot_command.html
`textEntityTypeCashtag`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_cashtag.html
`textEntityTypeCode`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_code.html
`textEntityTypeEmailAddress`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_email_address.html
`textEntityTypeHashtag`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_hashtag.html
`textEntityTypeItalic`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_italic.html
`textEntityTypeMention`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_mention.html
`textEntityTypeMentionName`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_mention_name.html
`textEntityTypePhoneNumber`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_phone_number.html
`textEntityTypePre`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_pre.html
`textEntityTypePreCode`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_pre_code.html
`textEntityTypeStrikethrough`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_strikethrough.html
`textEntityTypeTextUrl`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_text_url.html
`textEntityTypeUnderline`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_underline.html
`textEntityTypeUrl`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1text_entity_type_url.html


### Examples

#### `textEntityTypeBold`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 18874368,
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
    "date": 1589260488,
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
        "text": "TESTING123 BOLD",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 4,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeBold"
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

#### `textEntityTypeBotCommand`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 33554432,
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
    "date": 1589260965,
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
        "text": "/start",
        "entities": [
          {
            "_extra": null,
            "offset": 0,
            "length": 6,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeBotCommand"
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

#### `textEntityTypeCashtag`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 32505856,
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
    "date": 1589260948,
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
        "text": "$USD CASHTAG TESTING123",
        "entities": [
          {
            "_extra": null,
            "offset": 0,
            "length": 4,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeCashtag"
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

#### `textEntityTypeCode`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 17825792,
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
    "date": 1589260476,
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
        "text": "TESTING123 preformatted",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 12,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeCode"
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

#### `textEntityTypeEmailAddress`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 24117248,
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
    "date": 1589260594,
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
        "text": "TESTING123 mark@example.com",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 16,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeEmailAddress"
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

#### `textEntityTypeHashtag`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 27262976,
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
    "date": 1589260622,
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
        "text": "testing123 #hashtag",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 8,
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

#### `textEntityTypeItalic`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 19922944,
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
    "date": 1589260501,
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
        "text": "TESTING123 ITALIC",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 6,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeItalic"
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

#### `textEntityTypeMention`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 31457280,
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
    "date": 1589260925,
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
        "text": "hey @ExampleUser12 how are you TESTING123",
        "entities": [
          {
            "_extra": null,
            "offset": 4,
            "length": 14,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeMention"
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

#### `textEntityTypeMentionName`

```json

```

#### `textEntityTypePhoneNumber`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 26214400,
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
    "date": 1589260616,
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
        "text": "TESTING123 (520) 555-5555",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 14,
            "type": {
              "_extra": null,
              "@type": "textEntityTypePhoneNumber"
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

#### `textEntityTypePre`

```json

```

#### `textEntityTypePreCode`

```json

```

#### `textEntityTypeStrikethrough`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 22020096,
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
    "date": 1589260520,
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
        "text": "TESTING123 STRIKE",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 6,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeStrikethrough"
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

#### `textEntityTypeTextUrl`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 23068672,
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
    "date": 1589260540,
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
        "text": "TESTING123 LINK https://zombo.com",
        "entities": [
          {
            "_extra": null,
            "offset": 16,
            "length": 17,
            "type": {
              "_extra": null,
              "url": "https://zombo.com/",
              "@type": "textEntityTypeTextUrl"
            },
            "@type": "textEntity"
          }
        ],
        "@type": "formattedText"
      },
      "web_page": {
        "_extra": null,
        "url": "https://zombo.com/",
        "display_url": "zombo.com",
        "type": "article",
        "site_name": "Zombo",
        "title": "15footstick",
        "description": {
          "_extra": null,
          "text": "15footstick is the independent record labelish aspect of the Zombocom zombo.com and home of Paw Paw Fuk, Giant Trio, Known In Bakersfield, Stars In Storage,and the  Kazoomy Love Guns. Serving The abstract world with digital power relics for the duration.   independent record label, music,Paw Paw Fuk, Giant Trio, Known In Bakersfield, Stars In Storage, Kazoomy Love Guns,Zombocom, zombo.com, post-cultural,webart, poetry, video,  flash, webart, metta, an early post-cultural portal. Serving The abstract transcommunity with Music and Multi-Media For since the bioZomb + The Independent World Report.",
          "entities": [
            {
              "_extra": null,
              "offset": 70,
              "length": 9,
              "type": {
                "_extra": null,
                "@type": "textEntityTypeUrl"
              },
              "@type": "textEntity"
            },
            {
              "_extra": null,
              "offset": 382,
              "length": 9,
              "type": {
                "_extra": null,
                "@type": "textEntityTypeUrl"
              },
              "@type": "textEntity"
            }
          ],
          "@type": "formattedText"
        },
        "photo": null,
        "embed_url": "",
        "embed_type": "",
        "embed_width": 0,
        "embed_height": 0,
        "duration": 0,
        "author": "Zombocom",
        "animation": null,
        "audio": null,
        "document": null,
        "sticker": null,
        "video": null,
        "video_note": null,
        "voice_note": null,
        "instant_view_version": 0,
        "@type": "webPage"
      },
      "@type": "messageText"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

#### `textEntityTypeUnderline`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 20971520,
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
    "date": 1589260512,
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
        "text": "TESTING123 UNDERLINE",
        "entities": [
          {
            "_extra": null,
            "offset": 11,
            "length": 9,
            "type": {
              "_extra": null,
              "@type": "textEntityTypeUnderline"
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

#### `textEntityTypeUrl`

```json
{
  "_extra": null,
  "message": {
    "_extra": null,
    "id": 23068672,
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
    "date": 1589260540,
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
        "text": "TESTING123 LINK https://zombo.com",
        "entities": [
          {
            "_extra": null,
            "offset": 16,
            "length": 17,
            "type": {
              "_extra": null,
              "url": "https://zombo.com/",
              "@type": "textEntityTypeTextUrl"
            },
            "@type": "textEntity"
          }
        ],
        "@type": "formattedText"
      },
      "web_page": {
        "_extra": null,
        "url": "https://zombo.com/",
        "display_url": "zombo.com",
        "type": "article",
        "site_name": "Zombo",
        "title": "15footstick",
        "description": {
          "_extra": null,
          "text": "15footstick is the independent record labelish aspect of the Zombocom zombo.com and home of Paw Paw Fuk, Giant Trio, Known In Bakersfield, Stars In Storage,and the  Kazoomy Love Guns. Serving The abstract world with digital power relics for the duration.   independent record label, music,Paw Paw Fuk, Giant Trio, Known In Bakersfield, Stars In Storage, Kazoomy Love Guns,Zombocom, zombo.com, post-cultural,webart, poetry, video,  flash, webart, metta, an early post-cultural portal. Serving The abstract transcommunity with Music and Multi-Media For since the bioZomb + The Independent World Report.",
          "entities": [
            {
              "_extra": null,
              "offset": 70,
              "length": 9,
              "type": {
                "_extra": null,
                "@type": "textEntityTypeUrl"
              },
              "@type": "textEntity"
            },
            {
              "_extra": null,
              "offset": 382,
              "length": 9,
              "type": {
                "_extra": null,
                "@type": "textEntityTypeUrl"
              },
              "@type": "textEntity"
            }
          ],
          "@type": "formattedText"
        },
        "photo": null,
        "embed_url": "",
        "embed_type": "",
        "embed_width": 0,
        "embed_height": 0,
        "duration": 0,
        "author": "Zombocom",
        "animation": null,
        "audio": null,
        "document": null,
        "sticker": null,
        "video": null,
        "video_note": null,
        "voice_note": null,
        "instant_view_version": 0,
        "@type": "webPage"
      },
      "@type": "messageText"
    },
    "reply_markup": null,
    "@type": "message"
  },
  "@type": "updateNewMessage"
}
```

