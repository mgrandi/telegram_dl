"""add user table

Revision ID: 3326eb4a8333
Revises: 977a5c5a397c
Create Date: 2020-02-05 16:44:09.758691

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = '3326eb4a8333'
down_revision = '977a5c5a397c'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('user',
        sa.Column('user_id', sa.Integer(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('as_of', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.Column("as_of", sa.DateTime, nullable=False),

        sa.Column('tg_user_id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.Unicode(length=100), nullable=True),
        sa.Column('last_name', sa.Unicode(length=100), nullable=True),
        sa.Column('user_name', sa.Unicode(length=100), nullable=True),

        # Changing this custom column to its base type
        # sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(region="US", max_length=20), nullable=True),
        sa.Column("phone_number", sa.Unicode(length=20)),

        sa.Column('profile_photo_id', sa.Unicode(length=100), nullable=True),

        sa.Column('is_contact', sa.Boolean(), nullable=False),
        sa.Column('is_mutual_contact', sa.Boolean(), nullable=False)
        sa.Column('is_verified', sa.Boolean(), nullable=False),
        sa.Column('is_support', sa.Boolean(), nullable=False),
        sa.Column('restriction_reason', sa.Unicode(length=255), nullable=True),
        sa.Column('is_scam', sa.Boolean(), nullable=False),
        sa.Column('have_access', sa.Boolean(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('user_type', sqlalchemy_utils.types.choice.ChoiceType(dbme.UserTypeEnum, impl=sa.Integer()), nullable=True),
        sa.Column("user_type", sa.Integer()),

        sa.Column('language_code', sa.Unicode(length=20), nullable=True),
        sa.ForeignKeyConstraint(['profile_photo_id'], ['profile_photo.profile_photo_id'], name="FK-user-profile_photo_id-profile_photo-profile_photo_id"),
        sa.PrimaryKeyConstraint('user_id', name='PK-user-user_id')
    )


    op.create_index('IX-user-tg_user_id', 'user', ['tg_user_id'], unique=False)
    op.create_index('IX-user-phone_number', 'user', ['phone_number'], unique=False)
    op.create_index('IX-user-user_type', 'user', ['user_type'], unique=False)
    op.create_index('IXUQ-user-tg_user_id-as_of', 'user', ['tg_user_id', 'as_of'], unique=True)


def downgrade():

    op.drop_index('IXUQ-user-tg_user_id-as_of', table_name='user')
    op.drop_index('IX-user-user_type', table_name='user')
    op.drop_index('IX-user-phone_number', table_name='user')
    op.drop_index('IX-user-tg_user_id', table_name='user')
    op.drop_table('user')
