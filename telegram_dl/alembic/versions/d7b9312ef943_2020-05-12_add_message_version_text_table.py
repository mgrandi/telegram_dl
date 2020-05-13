"""add 'message_version_text' table

Revision ID: d7b9312ef943
Revises: 18e8fe8a7c2e
Create Date: 2020-05-12 17:54:00.494962

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'd7b9312ef943'
down_revision = '18e8fe8a7c2e'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('message_version_text',
        sa.Column('message_version_text_id', sa.Integer(), nullable=False),
        sa.Column('text', sa.Unicode(), nullable=False),
        sa.Column('web_page_id', sa.Integer(), nullable=True),

        sa.ForeignKeyConstraint(
            ['message_version_text_id'],
            ['message_version.message_version_id'],
            name='FK-message_version_text.message_version_text_id-message_version-message_version_id'),

        sa.PrimaryKeyConstraint(
            'message_version_text_id',
            name='PK-message_version_text-message_version_text_id')
    )

def downgrade():

    op.drop_table('message_version_text')
