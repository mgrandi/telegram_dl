"""add photo_set table

Revision ID: e617bbe46221
Revises: ccf4b069fbe3
Create Date: 2020-04-22 01:57:10.652938

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'e617bbe46221'
down_revision = 'ccf4b069fbe3'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('photo_set',
        sa.Column('photo_set_id', sa.Integer(), nullable=False),
        sa.Column('polytype', sa.Unicode(length=100), nullable=False),

        sa.PrimaryKeyConstraint('photo_set_id', name='PK-photo_set-photo_set_id')
    )


def downgrade():

    op.drop_table('photo_set')
