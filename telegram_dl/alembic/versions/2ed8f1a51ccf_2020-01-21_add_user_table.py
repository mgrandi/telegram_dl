"""add user table

Revision ID: 2ed8f1a51ccf
Revises: c854c0026859
Create Date: 2020-01-21 17:05:39.659666

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = '2ed8f1a51ccf'
down_revision = 'c854c0026859'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('tg_user_id', sa.Integer(), nullable=True),
        sa.Column('first_name', sa.Unicode(length=100), nullable=True),
        sa.Column('last_name', sa.Unicode(length=100), nullable=True),
        sa.Column('user_name', sa.Unicode(length=100), nullable=True),
        sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(length=20), nullable=True),
        sa.Column('profile_photo_id', sa.Unicode(length=100), nullable=True),
        sa.Column('outgoing_link', sqlalchemy_utils.types.choice.ChoiceType(dbme.LinkStateEnum, impl=sa.Integer()), nullable=True),
        sa.Column('incoming_link', sqlalchemy_utils.types.choice.ChoiceType(dbme.LinkStateEnum, impl=sa.Integer()), nullable=True),
        sa.Column('is_verified', sa.Boolean(), nullable=True),
        sa.Column('is_support', sa.Boolean(), nullable=True),
        sa.Column('restriction_reason', sa.Unicode(length=255), nullable=True),
        sa.Column('is_scam', sa.Boolean(), nullable=True),
        sa.Column('have_access', sa.Boolean(), nullable=True),
        sa.Column('user_type', sqlalchemy_utils.types.choice.ChoiceType(dbme.UserTypeEnum, impl=sa.Integer()), nullable=True),
        sa.Column('language_code', sa.Unicode(length=20), nullable=True),
        sa.ForeignKeyConstraint(['profile_photo_id'], ['profile_photo.tg_profile_photo_id'], ),
        sa.PrimaryKeyConstraint('user_id')
    )

    op.create_index('IX-user-phone_number', 'user', ['phone_number'], unique=False)
    op.create_index('IX-user-user_type', 'user', ['user_type'], unique=False)
    op.create_index('IXUQ-user-tg_user_id', 'user', ['tg_user_id'], unique=True)


def downgrade():
    op.drop_index('IXUQ-user-tg_user_id', table_name='user')
    op.drop_index('IX-user-user_type', table_name='user')
    op.drop_index('IX-user-phone_number', table_name='user')
    op.drop_table('user')
