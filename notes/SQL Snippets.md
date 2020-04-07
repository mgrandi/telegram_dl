# SQL Snippets

## show all of the profile photo files for a given user

```sql
select * from user
join profile_photo on (user.profile_photo_id == profile_photo.profile_photo_id)
join file on  (profile_photo.big_id == file.file_id)
where user.tg_user_id = 1234
```
