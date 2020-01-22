"""add file table

Revision ID: 047a6b389b38
Revises:
Create Date: 2020-01-21 17:00:12.181156

"""

# NOTE:
# it seems that some `alembic` commands don't run `env.py`, like `alembic history`,
# so since this is the root changeset, we run the same snippet that we run at the
# top of env.py where we set the current working dir (the top level directory,
# containing the `telegram_dl` folder) to be in the python path, so that
# it can actually find the `telegram_dl` module, or else we just get
# `ModuleNotFoundError: No module named 'telegram_dl'` errors when running
# `alembic history` , or any other commands that don't use env.py
# see # see https://stackoverflow.com/questions/32032940/how-to-import-the-own-model-into-myproject-alembic-env-py
import sys, os;sys.path.insert(0, os.getcwd())

from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = '047a6b389b38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('file',
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column('tg_file_id', sa.Integer(), nullable=True),
        sa.Column('size', sa.Integer(), nullable=True),
        sa.Column('expected_size', sa.Integer(), nullable=True),
        sa.Column('remote_file_id', sa.Unicode(length=100), nullable=True),
        sa.PrimaryKeyConstraint('file_id')
    )

    op.create_index('IX-file-remote_file_id', 'file', ['remote_file_id'], unique=False)
    op.create_index('IXUQ-file-tg_file_id', 'file', ['tg_file_id'], unique=True)


def downgrade():
    op.drop_index('IXUQ-file-tg_file_id', table_name='file')
    op.drop_index('IX-file-remote_file_id', table_name='file')
    op.drop_table('file')
