# Alembic Notes

## passing in our configuration

By default alembic wants to use a sqlalchemy url provided in alembic.ini, which is
annoying since telegram_dl has its own configuration to provide the sqlalchemy
URL. So I edited env.py to load our configuration to get the sqlalchemy URL,
but we need to provide where the configuration file is to alembic first

We do this by using the `-x` argument:

before:

```plaintext

alembic upgrade head
```

after:

```plaintext

alembic -x "telegram_dl_config=~\Temp\somefolder\config.conf" upgrade head
```

Note that you need to provide the `-x` command after `alembic` , but before other alembic
arguments such as `revision` or `upgrade`. This is just how it was set up in the
ArgumentParser that alembic uses

## generating the first 3 tables, user, file, profile_photo

the ideal situation is to only do one thing in a database revision, like only
create one table, remove one column, etc, so that way if something goes wrong,
the likelyhood of something being half completed is low

so if you add 2 tables, and 1 suceeds but one fails, when you rerun the
revision, the first table is already there, which requires manual intervention


so with that in mind, we have 3 starting tables, user, file, and profile_photo

user has a FK to profile_photo, and profile_photo has a FK to file, so if we want
to stick to the 'one operation per revision' mantra, we need to run the alembic
autogenerate commands like this:


```plaintext

cd telegram_dl
# make sure alembic.ini is correct

# comment out all the model definitions in db_model.py except for File
alembic -x "telegram_dl_config=~\Temp\telegram_dl_scratch\config.conf" revision --autogenerate -m "add file table"
# edit revision file to your liking...
alembic -x "telegram_dl_config=~\Temp\telegram_dl_scratch\config.conf" upgrade head

# uncomment the definition for 'profile_photo' in db_model.py...
alembic -x "telegram_dl_config=~\Temp\telegram_dl_scratch\config.conf" revision --autogenerate -m "add profile_photo table"
# edit revision file to your liking...
alembic -x "telegram_dl_config=~\Temp\telegram_dl_scratch\config.conf" upgrade head

# uncomment the definition for 'user' in db_model.py...
alembic -x "telegram_dl_config=~\Temp\telegram_dl_scratch\config.conf" revision --autogenerate -m "add user table"
# edit revision file to your liking...
alembic -x "telegram_dl_config=~\Temp\telegram_dl_scratch\config.conf" upgrade head

```

this prevents you from getting errors such as:

```plaintext
sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column 'user.profile_photo_id' could not find table 'profile_photo' with which to generate a foreign key to target column 'tg_profile_photo_id'
```

also, you need to do `alembic upgrade head` every time, because it looks at the
database to see what the differences are between the sqlalchemy declarative
model Metadata and the actual database, so if you don't do `upgrade head`, you
will be adding the 'file' table in all 3 revisions rather than just the first
