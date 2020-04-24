
import sys
import os
from logging.config import fileConfig
import logging
import pathlib

from sqlalchemy import engine_from_config, create_engine
from sqlalchemy import pool

from alembic import context

import pyhocon

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# NOTE:
# we set the telegram_dl directory (the package directory)
# to be in the python path, so that
# it can actually find the `telegram_dl` module, or else we just get
# `ModuleNotFoundError: No module named 'telegram_dl'` errors
# see https://stackoverflow.com/questions/32032940/how-to-import-the-own-model-into-myproject-alembic-env-py
telegram_dl_import_path = pathlib.Path(config.get_main_option("telegram_dl_import_path"))
resolved_path = telegram_dl_import_path.resolve()
if resolved_path not in sys.path:
    sys.path.insert(0, str(resolved_path))

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

from telegram_dl import db_model, utils, constants
target_metadata = db_model.CustomDeclarativeBase.metadata

logger = logging.getLogger(__name__)

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# NOTE:
# uncomment to debug logging issues with `alembic.ini`
# import logging_tree
# logger.info(logging_tree.format.build_description(node=None))


def get_our_own_sqla_url():

    # Load our own application config and use it to get the SQLAlchemy URL
    # TODO: maybe make this an option, like have it be in the `-x` arguments OR in alembic.ini?

    x_arguments  = context.get_x_argument(as_dictionary=True)

    if constants.ALEMBIC_CMD_X_ARGUMENT_NAME not in x_arguments.keys():
        raise Exception("you need to pass in `-x {}=/path/to/config``".format(constants.ALEMBIC_CMD_X_ARGUMENT_NAME))

    our_config_path = x_arguments[constants.ALEMBIC_CMD_X_ARGUMENT_NAME]

    logger.info("telegram_dl config file path: `%s`", our_config_path)
    our_config = utils.hocon_config_file_type(our_config_path)
    database_group_path = f"{constants.CONFIG_ROOT_GROUP}.{constants.CONFIG_DATABASE_GROUP}"
    sqla_url = utils.get_sqlalchemy_url_from_hocon_config(our_config.get_config(database_group_path))

    logger.info("SQLAlchemy URL: `%s`", sqla_url)
    return sqla_url

def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """

    # url = config.get_main_option("sqlalchemy.url")

    url = get_our_own_sqla_url()

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        render_as_batch=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """

    sqla_url = get_our_own_sqla_url()

    connectable = create_engine(sqla_url, poolclass=pool.NullPool)

    logger.info("Engine: `%s`", connectable)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            render_as_batch=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
