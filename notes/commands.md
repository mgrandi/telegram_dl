# Commands

## Alembic Commands

alembic revision --autogenerate -m "add user, file, profile_photo tables"

alembic upgrade head

alembic revision --autogenerate -m "add profile_photo table"

alembic upgrade head


alembic revision --autogenerate -m "add user table"
alembic upgrade head


## Commands for running the app

python .\telegram_dl_cli.py "~\Temp\telegram_dl_scratch\config.conf" --logging-config  "~\Temp\telegram_dl_scratch\loggingcfg.json"