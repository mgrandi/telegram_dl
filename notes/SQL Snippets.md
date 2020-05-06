# SQL Snippets

## show all of the profile photo files for a given user

```sql
select file.* from user
join profile_photo on (user.profile_photo_id == profile_photo.profile_photo_id)
join file on  (profile_photo.big_id == file.file_id or profile_photo.small_id == file.file_id)
where user.tg_user_id = 1234
```

## show all the `user_version` columns for a given user

```sql
select * from user
join user_version on (user.user_id == user_version.user_id)
where user.user_id = 1234
```

## show all the `chat_version` columns for a given chat

```sql
select * from chat
join chat_version on (chat.chat_id == chat_version.chat_id)
where chat.chat_id = 1234
```