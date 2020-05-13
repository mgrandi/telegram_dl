"""added message table

Revision ID: 43624ee83d2f
Revises: 817cc7f1f793
Create Date: 2020-05-12 17:10:37.416784

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '43624ee83d2f'
down_revision = '817cc7f1f793'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('message',
        sa.Column('message_id', sa.Integer(), nullable=False),
        sa.Column('sender_user_id', sa.Integer(), nullable=False),
        sa.Column('chat_id', sa.Integer(), nullable=False),
        sa.Column('reply_to_message_id', sa.Integer(), nullable=True),
        sa.Column('via_bot_user_id', sa.Integer(), nullable=True),
        sa.Column('is_outgoing', sa.Boolean(), nullable=False),
        sa.Column('is_channel_post', sa.Boolean(), nullable=False),
        sa.Column('can_edit', sa.Boolean(), nullable=False),
        sa.Column('can_forward', sa.Boolean(), nullable=False),
        sa.Column('can_be_deleted_only_for_self', sa.Boolean(), nullable=False),
        sa.Column('can_be_deleted_for_all_users', sa.Boolean(), nullable=False),
        sa.Column('restriction_reason', sa.Unicode(), nullable=True),

        sa.ForeignKeyConstraint(
            ['chat_id'],
            ['chat.chat_id'],
            name='FK-message-chat_id-chat-chat_id'),

        sa.ForeignKeyConstraint(
            ['sender_user_id'],
            ['user.user_id'],
            name='FK-message-sender_user_id-user-user_id'),

        sa.PrimaryKeyConstraint(
            'message_id',
            name='PK-message-message_id')
    )

    with op.batch_alter_table('message', schema=None) as batch_op:

        batch_op.create_index(
            index_name='IX-message-chat_id',
            columns=['chat_id'],
            unique=False)

        batch_op.create_index(
            index_name='IX-message-sender_user_id',
            columns=['sender_user_id'],
            unique=False)



def downgrade():

    with op.batch_alter_table('message', schema=None) as batch_op:

        batch_op.drop_index('IX-message-sender_user_id')
        batch_op.drop_index('IX-message-chat_id')

    op.drop_table('message')
