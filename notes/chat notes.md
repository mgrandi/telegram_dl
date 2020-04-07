# `chat` notes


## class references

`chat`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat.html

## examples

```json
{
  "_extra": null,
  "chat": {
    "_extra": null,
    "id": 123456,
    "type": {
      "_extra": null,
      "user_id": 123456,
      "@type": "chatTypePrivate"
    },
    "title": "My Saved Messages Chat",
    "photo": {
      "_extra": null,
      "small": {
        "_extra": null,
        "id": 3,
        "size": 0,
        "expected_size": 0,
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
          "id": "AQADAQADXKkxG6vLzgQACLJsEjAABAIAA6vLzgQABHHpJIC1z601EGwAAhYE",
          "is_uploading_active": false,
          "is_uploading_completed": true,
          "uploaded_size": 0,
          "@type": "remoteFile"
        },
        "@type": "file"
      },
      "big": {
        "_extra": null,
        "id": 4,
        "size": 0,
        "expected_size": 0,
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
          "id": "AQADAQADXKkxG6vLzgQACLJsEjAABAMAA6vLzgQABHHpJIC1z601EmwAAhYE",
          "is_uploading_active": false,
          "is_uploading_completed": true,
          "uploaded_size": 0,
          "@type": "remoteFile"
        },
        "@type": "file"
      },
      "@type": "chatPhoto"
    },
    "permissions": {
      "_extra": null,
      "can_send_messages": true,
      "can_send_media_messages": true,
      "can_send_polls": true,
      "can_send_other_messages": true,
      "can_add_web_page_previews": true,
      "can_change_info": false,
      "can_invite_users": false,
      "can_pin_messages": true,
      "@type": "chatPermissions"
    },
    "last_message": null,
    "order": 0,
    "is_pinned": true,
    "is_marked_as_unread": false,
    "is_sponsored": false,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "can_be_reported": false,
    "default_disable_notification": false,
    "unread_count": 0,
    "last_read_inbox_message_id": 123,
    "last_read_outbox_message_id": 12345,
    "unread_mention_count": 0,
    "notification_settings": {
      "_extra": null,
      "use_default_mute_for": false,
      "mute_for": 0,
      "use_default_sound": false,
      "sound": "default",
      "use_default_show_preview": false,
      "show_preview": true,
      "use_default_disable_pinned_message_notifications": true,
      "disable_pinned_message_notifications": false,
      "use_default_disable_mention_notifications": true,
      "disable_mention_notifications": false,
      "@type": "chatNotificationSettings"
    },
    "pinned_message_id": 0,
    "reply_markup_message_id": 0,
    "draft_message": null,
    "client_data": "",
    "@type": "chat"
  },
  "@type": "updateNewChat"
}
```