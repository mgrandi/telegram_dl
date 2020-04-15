"""add file table

Revision ID: ccf4b069fbe3
Revises:
Create Date: 2020-02-05 16:38:34.152505

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = 'ccf4b069fbe3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('file',
        sa.Column('file_id', sa.Integer(), nullable=False),
        sa.Column('tg_file_id', sa.Integer(), nullable=False),
        sa.Column('size', sa.Integer(), nullable=False),
        sa.Column('expected_size', sa.Integer(), nullable=False),
        sa.Column('remote_file_id', sa.Unicode(length=100), nullable=False),
        sa.PrimaryKeyConstraint('file_id', name='PK-file-file_id')
    )

    op.create_index('IXUQ-file-remote_file_id', 'file', ['remote_file_id'], unique=True)


def downgrade():

    op.drop_index('IXUQ-file-remote_file_id', table_name='file')
    op.drop_table('file')
