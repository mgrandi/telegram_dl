# `chat` notes


## class references

`chat`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat.html

`ChatType`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1_chat_type.html

`chatTypeBasicGroup`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_type_basic_group.html


`chatTypePrivate`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_type_private.html


`chatTypeSecret`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_type_secret.html


`chatTypeSupergroup`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_type_supergroup.html


## class documentation copy paste

### chat


```plaintext
std::int64_t  id_
  Chat unique identifier.

object_ptr< ChatType >  type_
  Type of the chat.

object_ptr< ChatList >  chat_list_
  A chat list to which the chat belongs; may be null.

std::string   title_
  Chat title.

object_ptr< chatPhoto >   photo_
  Chat photo; may be null.

object_ptr< chatPermissions >   permissions_
  Actions that non-administrator chat members are allowed to take in the chat.

object_ptr< message >   last_message_
  Last message in the chat; may be null.

std::int64_t  order_
  Descending parameter by which chats are sorted in the main chat list. If the order number of two chats is the same, they must be sorted in descending order by ID. If 0, the position of the chat in the list is undetermined.

bool  is_pinned_
  True, if the chat is pinned.

bool  is_marked_as_unread_
  True, if the chat is marked as unread.

bool  is_sponsored_
  True, if the chat is sponsored by the user's MTProxy server.

bool  has_scheduled_messages_
  True, if the chat has scheduled messages.

bool  can_be_deleted_only_for_self_
  True, if the chat messages can be deleted only for the current user while other users will continue to see the messages.

bool  can_be_deleted_for_all_users_
  True, if the chat messages can be deleted for all users.

bool  can_be_reported_
  True, if the chat can be reported to Telegram moderators through reportChat.

bool  default_disable_notification_
  Default value of the disable_notification parameter, used when a message is sent to the chat.

std::int32_t  unread_count_
  Number of unread messages in the chat.

std::int64_t  last_read_inbox_message_id_
  Identifier of the last read incoming message.

std::int64_t  last_read_outbox_message_id_
  Identifier of the last read outgoing message.

std::int32_t  unread_mention_count_
  Number of unread messages with a mention/reply in the chat.

object_ptr< chatNotificationSettings >  notification_settings_
  Notification settings for this chat.

object_ptr< ChatActionBar >   action_bar_
  Describes actions which should be possible to do through a chat action bar; may be null.

std::int64_t  pinned_message_id_
  Identifier of the pinned message in the chat; 0 if none.

std::int64_t  reply_markup_message_id_
  Identifier of the message from which reply markup needs to be used; 0 if there is no default custom reply markup in the chat.

object_ptr< draftMessage >  draft_message_
  A draft of a message in the chat; may be null.

std::string   client_data_
  Contains client-specific data associated with the chat. (For example, the chat position or local chat notification settings can be stored here.) Persistent if the message database is used.

```

### chatTypeBasicGroup

```plaintext
std::int32_t  basic_group_id_

```


### chatTypeSecret


```plaintext
std::int32_t  secret_chat_id_
  Secret chat identifier.

std::int32_t  user_id_
  User identifier of the secret chat peer.

```

### chatTypePrivate


```plaintext
std::int32_t  user_id_
  User identifier.
```

### chatTypeSupergroup


```plaintext
std::int32_t  supergroup_id_
  Supergroup or channel identifier.

bool  is_channel_

```

## database layout notes

Chat
  chat_id (PK) -> integer

  poly_type (for table class inheritance) -> string

  tg_chat_id -> integer

  title -> Unicode

  photo -> PhotoSet
    NOTE: this is a `chatPhoto`, which is different than our other photo types
    (`profilePhoto` and `photo`) but it only has `big` and `small` as the fields
    so its basically the same as `profilePhoto` but without the extra id, so we'll make it
    like `ProfilePhotoSet` with just a PhotoSet with 2 photos, maybe make a table that has nothing in it? i dunno...

  sponsored -> boolean

BasicGroup(Chat)

  basic_group_chat_id(PK, FK to chat) -> integer

  tg_basic_group_id -> integer


PrivateChat(Chat)

  private_chat_id(PK, FK to chat) -> integer

  user_id -> integer, FK to user

SupergroupChat(Chat)

  supergroup_chat_id(PK, FK to chat) -> integer

  tg_supergroup_id -> integer

  is_channel -> boolean


SecretChat(Chat)

  secret_chat_id(PK, FK to chat) -> integer

  tg_secret_chat_id -> integer

  user_id -> integer, FK to user



## examples

### `chatTypeBasicGroup`

Notice how the chat's ID is `-356102` but then the `chatTypeBasicGroup.basic_group_id` is `356102`

so i guess to get the 'general chat' id for a basic group, it is  `-1` + `chatTypeSupergroup.supergroup_id` (as strings)
```json
{
  "_extra": null,
  "chat": {
    "_extra": null,
    "id": -356102,
    "type": {
      "_extra": null,
      "basic_group_id": 356102,
      "@type": "chatTypeBasicGroup"
    },
    "chat_list": null,
    "title": "PenguinTestGroup",
    "photo": null,
    "permissions": {
      "_extra": null,
      "can_send_messages": true,
      "can_send_media_messages": true,
      "can_send_polls": true,
      "can_send_other_messages": true,
      "can_add_web_page_previews": true,
      "can_change_info": true,
      "can_invite_users": true,
      "can_pin_messages": true,
      "@type": "chatPermissions"
    },
    "last_message": null,
    "order": 0,
    "is_pinned": false,
    "is_marked_as_unread": false,
    "is_sponsored": false,
    "has_scheduled_messages": false,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "can_be_reported": false,
    "default_disable_notification": false,
    "unread_count": 0,
    "last_read_inbox_message_id": 0,
    "last_read_outbox_message_id": 0,
    "unread_mention_count": 0,
    "notification_settings": {
      "_extra": null,
      "use_default_mute_for": true,
      "mute_for": 0,
      "use_default_sound": true,
      "sound": "default",
      "use_default_show_preview": true,
      "show_preview": true,
      "use_default_disable_pinned_message_notifications": true,
      "disable_pinned_message_notifications": false,
      "use_default_disable_mention_notifications": true,
      "disable_mention_notifications": false,
      "@type": "chatNotificationSettings"
    },
    "action_bar": null,
    "pinned_message_id": 0,
    "reply_markup_message_id": 0,
    "draft_message": null,
    "client_data": "",
    "@type": "chat"
  },
  "@type": "updateNewChat"
}
```

### `chatTypePrivate`

```json
{
  "_extra": null,
  "chat": {
    "_extra": null,
    "id": 678406,
    "type": {
      "_extra": null,
      "user_id": 678406,
      "@type": "chatTypePrivate"
    },
    "chat_list": null,
    "title": "Me",
    "photo": {
      "_extra": null,
      "small": {
        "_extra": null,
        "id": 1,
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
          "id": "AQADAQADqacxGwZaCgAJYUnskC4AAwIAAwZaCgAFGxDFS-Z_vYrjBAACGAQ",
          "unique_id": "AQADYUnskC4AA-MEAAI",
          "is_uploading_active": false,
          "is_uploading_completed": true,
          "uploaded_size": 0,
          "@type": "remoteFile"
        },
        "@type": "file"
      },
      "big": {
        "_extra": null,
        "id": 2,
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
          "id": "AQADAQADqacxGwZaCgAJYUnskC4AAwMAAwZaCgAFGxDFS-Z_vYrlBAACGAQ",
          "unique_id": "AQADYUnskC4AA-UEAAI",
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
    "is_pinned": false,
    "is_marked_as_unread": false,
    "is_sponsored": false,
    "has_scheduled_messages": false,
    "can_be_deleted_only_for_self": true,
    "can_be_deleted_for_all_users": false,
    "can_be_reported": false,
    "default_disable_notification": false,
    "unread_count": 0,
    "last_read_inbox_message_id": 9437184,
    "last_read_outbox_message_id": 0,
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
    "action_bar": null,
    "pinned_message_id": 0,
    "reply_markup_message_id": 0,
    "draft_message": null,
    "client_data": "",
    "@type": "chat"
  },
  "@type": "updateNewChat"
}
```

### `chatTypeSecret`

```plaintext

std::int32_t  secret_chat_id_
  Secret chat identifier.

std::int32_t  user_id_
  User identifier of the secret chat peer.

```

### `chatTypeSupergroup`

Notice how the chat's ID is `-1000010597257` but then the `chatTypeSupergroup.supergroup_id` is `10597257`

so i guess to get the 'general chat' id for a supergroup, it is  `-10000` + `chatTypeSupergroup.supergroup_id` (as strings)

```json
{
  "_extra": null,
  "chat": {
    "_extra": null,
    "id": -1000010597257,
    "type": {
      "_extra": null,
      "supergroup_id": 10597257,
      "is_channel": true,
      "@type": "chatTypeSupergroup"
    },
    "chat_list": null,
    "title": "`TestingChannel",
    "photo": null,
    "permissions": {
      "_extra": null,
      "can_send_messages": false,
      "can_send_media_messages": false,
      "can_send_polls": false,
      "can_send_other_messages": false,
      "can_add_web_page_previews": false,
      "can_change_info": false,
      "can_invite_users": false,
      "can_pin_messages": false,
      "@type": "chatPermissions"
    },
    "last_message": null,
    "order": 0,
    "is_pinned": false,
    "is_marked_as_unread": false,
    "is_sponsored": false,
    "has_scheduled_messages": false,
    "can_be_deleted_only_for_self": false,
    "can_be_deleted_for_all_users": false,
    "can_be_reported": false,
    "default_disable_notification": false,
    "unread_count": 0,
    "last_read_inbox_message_id": 0,
    "last_read_outbox_message_id": 2251799812636672,
    "unread_mention_count": 0,
    "notification_settings": {
      "_extra": null,
      "use_default_mute_for": true,
      "mute_for": 0,
      "use_default_sound": true,
      "sound": "default",
      "use_default_show_preview": true,
      "show_preview": true,
      "use_default_disable_pinned_message_notifications": true,
      "disable_pinned_message_notifications": false,
      "use_default_disable_mention_notifications": true,
      "disable_mention_notifications": false,
      "@type": "chatNotificationSettings"
    },
    "action_bar": null,
    "pinned_message_id": 0,
    "reply_markup_message_id": 0,
    "draft_message": null,
    "client_data": "",
    "@type": "chat"
  },
  "@type": "updateNewChat"
}
```
