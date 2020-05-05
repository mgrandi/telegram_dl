"""add chat table

Revision ID: 38cbc596f142
Revises: 3326eb4a8333
Create Date: 2020-04-30 01:55:44.943260

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '38cbc596f142'
down_revision = 'f16029a36600'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('chat',
        sa.Column('chat_id', sa.Integer(), nullable=False),
        sa.Column('polytype', sa.Unicode(), nullable=False),
        sa.Column('tg_chat_id', sa.Integer(), nullable=False),

        sa.PrimaryKeyConstraint('chat_id',
            name='PK-chat-chat_id')
    )

    with op.batch_alter_table('chat', schema=None) as batch_op:

        batch_op.create_index(
            'IXUQ-chat-tg_chat_id',
            ['tg_chat_id'],
            unique=True)


def downgrade():

    with op.batch_alter_table('chat', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-chat-tg_chat_id')

    op.drop_table('chat')
