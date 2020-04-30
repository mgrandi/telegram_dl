"""add secret_chat table

Revision ID: 817cc7f1f793
Revises: 2a0538b361f0
Create Date: 2020-04-30 02:22:24.230957

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '817cc7f1f793'
down_revision = '2a0538b361f0'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('secret_chat',
        sa.Column('secret_chat_id', sa.Integer(), nullable=False),
        sa.Column('tg_secret_chat_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['secret_chat_id'],
            ['chat.chat_id'],
            name='FK-secret_chat-secret_chat_id-chat-chat_id'),
        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.user_id'],
            name='FK-secret_chat-user_id-user-user_id'),
        sa.PrimaryKeyConstraint('secret_chat_id',
            name='PK-secret_chat-secret_chat_id')
    )

    with op.batch_alter_table('secret_chat', schema=None) as batch_op:

        batch_op.create_index(
            'IXUQ-secret_chat-tg_secret_chat_id',
            ['tg_secret_chat_id'],
            unique=True)


def downgrade():

    with op.batch_alter_table('secret_chat', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-secret_chat-tg_secret_chat_id')

    op.drop_table('secret_chat')
