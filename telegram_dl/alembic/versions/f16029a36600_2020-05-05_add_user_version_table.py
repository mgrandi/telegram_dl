"""add user_version table

Revision ID: f16029a36600
Revises: 817cc7f1f793
Create Date: 2020-05-05 15:17:04.469766

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'f16029a36600'
down_revision = '3326eb4a8333'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('user_version',

        sa.Column('user_version_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('as_of', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.Column("as_of", sa.DateTime, nullable=False),

        sa.Column('first_name', sa.Unicode(length=100), nullable=True),
        sa.Column('last_name', sa.Unicode(length=100), nullable=True),
        sa.Column('user_name', sa.Unicode(length=100), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('phone_number', sqlalchemy_utils.types.phone_number.PhoneNumberType(region="US", max_length=20), nullable=True),
        sa.Column("phone_number", sa.Unicode(length=20), nullable=True),

        sa.Column('profile_photo_set_id', sa.Integer(), nullable=True),
        sa.Column('is_contact', sa.Boolean(), nullable=False),
        sa.Column('is_mutual_contact', sa.Boolean(), nullable=False),
        sa.Column('is_verified', sa.Boolean(), nullable=False),
        sa.Column('is_support', sa.Boolean(), nullable=False),
        sa.Column('restriction_reason', sa.Unicode(length=255), nullable=True),
        sa.Column('is_scam', sa.Boolean(), nullable=False),
        sa.Column('have_access', sa.Boolean(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('user_type', sqlalchemy_utils.types.choice.ChoiceType(dbme.UserTypeEnum, impl=sa.Unicode()), nullable=True),
        sa.Column("user_type", sa.Unicode(length=50), nullable=False),

        sa.Column('language_code', sa.Unicode(length=20), nullable=True),

        sa.ForeignKeyConstraint(
            ['profile_photo_set_id'],
            ['photo_set.photo_set_id'],
            name='FK-user_version-profile_photo_set_id-photo_set-photo_set_id'),

        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.user_id'],
            name='FK-user_version-user_id-user-user_id'),

        sa.PrimaryKeyConstraint(
            'user_version_id',
            name='PK-user_version-user_version_id')
    )

    with op.batch_alter_table('user_version', schema=None) as batch_op:

        batch_op.create_index(
            index_name='IX-user_version-phone_number',
            columns=['phone_number'],
            unique=False)

        batch_op.create_index(
            index_name='IX-user_version-user_type',
            columns=['user_type'],
            unique=False)

        batch_op.create_index(
            index_name='IXUQ-user_version-user_id-as_of',
            columns=['user_id', 'as_of'],
            unique=True)



def downgrade():

    with op.batch_alter_table('user_version', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-user_version-user_id-as_of')
        batch_op.drop_index('IX-user_version-user_type')
        batch_op.drop_index('IX-user_version-phone_number')

    op.drop_table('user_version')
