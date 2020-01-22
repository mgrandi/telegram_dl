"""add profile_photo table

Revision ID: c854c0026859
Revises: 047a6b389b38
Create Date: 2020-01-21 17:02:35.113955

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = 'c854c0026859'
down_revision = '047a6b389b38'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('profile_photo',
        sa.Column('profile_photo_id', sa.Integer(), nullable=False),
        sa.Column('tg_profile_photo_id', sa.Integer(), nullable=True),
        sa.Column('big_id', sa.Integer(), nullable=True),
        sa.Column('small_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['big_id'], ['file.tg_file_id'], ),
        sa.ForeignKeyConstraint(['small_id'], ['file.tg_file_id'], ),
        sa.PrimaryKeyConstraint('profile_photo_id')
    )

    op.create_index('IXUQ-profile_photo-tg_profile_photo_id', 'profile_photo', ['tg_profile_photo_id'], unique=False)


def downgrade():
    op.drop_index('IXUQ-profile_photo-tg_profile_photo_id', table_name='profile_photo')
    op.drop_table('profile_photo')
