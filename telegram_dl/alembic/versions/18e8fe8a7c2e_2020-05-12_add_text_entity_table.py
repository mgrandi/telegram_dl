"""add text_entity table

Revision ID: 18e8fe8a7c2e
Revises: ca9904fadb92
Create Date: 2020-05-12 17:41:06.144130

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '18e8fe8a7c2e'
down_revision = 'ca9904fadb92'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('text_entity',
        sa.Column('text_entity_id', sa.Integer(), nullable=False),
        sa.Column('message_version_id', sa.Integer(), nullable=False),
        sa.Column('offset', sa.Integer(), nullable=False),
        sa.Column('length', sa.Integer(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('text_entity_type', sqlalchemy_utils.types.choice.ChoiceType(dbme.TextEntityTypeEnum, impl=Unicode(length=50)), nullable=False),
        sa.Column('text_entity_type', sa.Unicode(length=50), nullable=False),

        sa.ForeignKeyConstraint(
            ['message_version_id'],
            ['message_version.message_version_id'],
            name='FK-text_entity-message_version_id-message_version-message_version_id'),

        sa.PrimaryKeyConstraint(
            'text_entity_id',
            name='PK-text_entity-text_entity_id')
    )

    with op.batch_alter_table('text_entity', schema=None) as batch_op:

        batch_op.create_index(
            index_name='IX-text_entity-message_version_id',
            columns=['message_version_id'],
            unique=False)


def downgrade():

    with op.batch_alter_table('text_entity', schema=None) as batch_op:

        batch_op.drop_index('IX-text_entity-message_version_id')

    op.drop_table('text_entity')
