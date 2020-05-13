"""add chat_version table

Revision ID: 6b46e5ae44da
Revises: 817cc7f1f793
Create Date: 2020-05-05 14:31:28.417406

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '6b46e5ae44da'
down_revision = '38cbc596f142'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('chat_version',
        sa.Column('chat_version_id', sa.Integer(), nullable=False),
        sa.Column('chat_id', sa.Integer(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('as_of', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.Column('as_of', sa.DateTime, nullable=False),

       sa.Column('title', sa.Unicode(), nullable=False),
        sa.Column('photo_set_id', sa.Integer(), nullable=True),
        sa.Column('is_sponsored', sa.Boolean(), nullable=False),

        sa.ForeignKeyConstraint(
            ['chat_id'],
            ['chat.chat_id'],
            name='FK-chat_version-chat_id-chat_chat_id'),

        sa.ForeignKeyConstraint(
            ['photo_set_id'],
            ['photo_set.photo_set_id'],
            name='FK-chat_version-photo_set_id-photo_set-photo_set_id'),

        sa.PrimaryKeyConstraint(
            'chat_version_id',
            name='PK-chat_version-chat_version_id')
    )

    with op.batch_alter_table('chat_version', schema=None) as batch_op:

        batch_op.create_index(
            index_name='IXUQ-chat_version-chat_id-as_of',
            columns=['chat_id', 'as_of'],
            unique=True)


def downgrade():

    with op.batch_alter_table('chat_version', schema=None) as batch_op:

        batch_op.drop_index('IXUQ-chat_version-chat_id-as_of')

    op.drop_table('chat_version')
