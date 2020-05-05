"""add user table

Revision ID: 3326eb4a8333
Revises: cb38ff4e8b0a
Create Date: 2020-02-05 16:44:09.758691

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '3326eb4a8333'
down_revision = 'cb38ff4e8b0a'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('user',

        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('tg_user_id', sa.Integer(), nullable=False),

        sa.PrimaryKeyConstraint('user_id', name='PK-user-user_id')
    )

    with op.batch_alter_table('user', schema=None) as batch_op:

        batch_op.create_index(
            index_name='IX-user-tg_user_id',
            columns=['tg_user_id'],
            unique=False)


def downgrade():

    with op.batch_alter_table('user', schema=None) as batch_op:

        batch_op.drop_index('IX-user-tg_user_id')

    op.drop_table('user')
