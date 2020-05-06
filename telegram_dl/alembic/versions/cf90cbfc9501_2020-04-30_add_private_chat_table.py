"""add private_chat table

Revision ID: cf90cbfc9501
Revises: 5f433937f8b5
Create Date: 2020-04-30 02:10:38.034317

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'cf90cbfc9501'
down_revision = '5f433937f8b5'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('private_chat',
        sa.Column('private_chat_id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(
            ['private_chat_id'],
            ['chat.chat_id'],
            name='FK-private_chat-private_chat_id-chat-chat_id'),

        sa.ForeignKeyConstraint(
            ['user_id'],
            ['user.user_id'],
            name='FK-private_chat-user_id-user-user_id'),

        sa.PrimaryKeyConstraint(
            'private_chat_id',
             name='PK-private_chat-private_chat_id')
    )
    with op.batch_alter_table('private_chat', schema=None) as batch_op:

        batch_op.create_index(
            'IXUQ-private_chat-user_id',
            ['user_id'],
            unique=True)


def downgrade():

    with op.batch_alter_table('private_chat', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-private_chat-user_id')

    op.drop_table('private_chat')
