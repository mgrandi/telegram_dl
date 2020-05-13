"""added message_version table

Revision ID: ca9904fadb92
Revises: 43624ee83d2f
Create Date: 2020-05-12 17:17:25.000649

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'ca9904fadb92'
down_revision = '43624ee83d2f'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('message_version',

        sa.Column('message_version_id', sa.Integer(), nullable=False),
        sa.Column('message_id', sa.Integer(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('as_of', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.Column('as_of', sa.DateTime, nullable=False),

        # Changing this custom column to its base type
        # sa.Column('date', sqlalchemy_utils.types.arrow.ArrowType(), nullable=False),
        sa.Column('date', sa.DateTime, nullable=False),

        # Changing this custom column to its base type
        # sa.Column('edit_date', sqlalchemy_utils.types.arrow.ArrowType(), nullable=True),
        sa.Column('edit_date', sa.DateTime, nullable=True),


        sa.Column('author_signature', sa.Unicode(), nullable=True),
        sa.Column('ttl', sa.Integer(), nullable=True),

        sa.ForeignKeyConstraint(
            ['message_id'],
            ['message.message_id'],
            name='FK-message_version-message_id-message-message_id'),

        sa.PrimaryKeyConstraint(
            'message_version_id',
            name='PK-message_version-message_version_id')
    )

    with op.batch_alter_table('message_version', schema=None) as batch_op:

        batch_op.create_index(
            index_name='IX-message_version-as_of',
            columns=['as_of'],
            unique=False)


def downgrade():

    with op.batch_alter_table('message_version', schema=None) as batch_op:

        batch_op.drop_index('IX-message_version-as_of')

    op.drop_table('message_version')
