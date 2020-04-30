"""add super_group_chat table

Revision ID: 2a0538b361f0
Revises: cf90cbfc9501
Create Date: 2020-04-30 02:17:41.756579

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '2a0538b361f0'
down_revision = 'cf90cbfc9501'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('super_group_chat',
        sa.Column('super_group_chat_id', sa.Integer(), nullable=False),
        sa.Column('tg_super_group_id', sa.Integer(), nullable=False),
        sa.Column('is_channel', sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ['super_group_chat_id'],
            ['chat.chat_id'],
            name='FK-super_group_chat-super_group_chat_id-chat-chat_id'),
        sa.PrimaryKeyConstraint(
            'super_group_chat_id',
             name='PK-super_group_chat-super_group_chat_id')
    )

    with op.batch_alter_table('super_group_chat', schema=None) as batch_op:

        batch_op.create_index(
            'IXUQ-super_group_chat-tg_super_group_id',
            ['tg_super_group_id'],
            unique=True)


def downgrade():

    with op.batch_alter_table('super_group_chat', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-super_group_chat-tg_super_group_id')

    op.drop_table('super_group_chat')
