"""add profile_photo_set table

Revision ID: 9cfe76bb0156
Revises: e617bbe46221
Create Date: 2020-04-22 01:58:45.081699

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '9cfe76bb0156'
down_revision = 'e617bbe46221'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('profile_photo_set',
        sa.Column('profile_photo_photo_set_id', sa.Integer(), nullable=False),
        sa.Column('tg_id', sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(
            ['profile_photo_photo_set_id'],
            ['photo_set.photo_set_id'],
            name='FK-profile_photo_set-profile_photo_set_id-photo_set-photo_set_id'),

        sa.PrimaryKeyConstraint(
            'profile_photo_photo_set_id',
            name='PK-profile_photo_set-profile_photo_photo_set_id')
    )


def downgrade():

    op.drop_table('profile_photo_set')
