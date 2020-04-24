# Photo notes

## types of photos

`updateChatPhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1update_chat_photo.html

`chatPhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1chat_photo.html

`photo`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo.html

`messagePhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1message_photo.html

`profilePhoto`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1profile_photo.html

`photoSize`: https://core.telegram.org/tdlib/docs/classtd_1_1td__api_1_1photo_size.html

## notes

```
chatPhoto class
    big
        (file obj)
    small
        (file obj)

```

```
profilePhoto class
    id

    small
        (file obj)

    big
        (file obj)

```

```
messagePhoto class
    photo
        (photo obj)
    caption

    is_secret

```

```
updateChatPhoto class

    chat_id

    photo
        (chatPhoto obj)
```

```
photo class

    has_stickers

    minithumbnail

    sizes



```

```
photoSize class
    type

    photo
        (file obj)

    width

    height

```


## table layout

```


photo_set

    <primary_key>

    <polymorphic_type>

    photos -> <list of photo objects>

profile_photo(photo_set)

    id

    tg_id

    ################################3
    # MAYBE DON'T NEED THE STUFF BELOW

    big_id -> int

    small_id -> int

    big -> photo
    small -> photo
    #################################

photo

    <primary key>

    <photo_set_id>

    thumbnail_type
    width
    height
    has_stickers

    <file_id> -> file



chat

    as_of
    ...
    ...

    chat_photo -> photo_set



user

    profile_photo

file
    ...
    ...



```