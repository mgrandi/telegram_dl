"""add basic_group_chat table

Revision ID: 5f433937f8b5
Revises: 38cbc596f142
Create Date: 2020-04-30 02:02:33.830261

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '5f433937f8b5'
down_revision = '6b46e5ae44da'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('basic_group_chat',
        sa.Column('basic_group_chat_id', sa.Integer(), nullable=False),
        sa.Column('tg_basic_group_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['basic_group_chat_id'],
            ['chat.chat_id'],
            name='FK-basic_group_chat-basic_group_chat_id-chat-chat_id'),
        sa.PrimaryKeyConstraint(
            'basic_group_chat_id',
            name='PK-basic_group_chat-basic_group_chat_id')
    )

    with op.batch_alter_table('basic_group_chat', schema=None) as batch_op:

        batch_op.create_index(
            'IXUQ-basic_group_chat-tg_basic_group_id',
            ['tg_basic_group_id'],
            unique=True)


def downgrade():

    with op.batch_alter_table('basic_group_chat', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-basic_group_chat-tg_basic_group_id')

    op.drop_table('basic_group_chat')
