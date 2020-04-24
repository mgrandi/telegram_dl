"""add photo table

Revision ID: cb38ff4e8b0a
Revises: 9cfe76bb0156
Create Date: 2020-04-23 16:13:20.969735

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'cb38ff4e8b0a'
down_revision = '9cfe76bb0156'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table('photo',
        sa.Column('photo_id', sa.Integer(), nullable=False),
        sa.Column('photo_set_id', sa.Integer(), nullable=False),

        # Changing this custom column to its base type
        # sa.Column('thumbnail_type', sqlalchemy_utils.types.choice.ChoiceType(), nullable=False),
        sa.Column('thumbnail_type', sa.Unicode(length=10), nullable=False),

        sa.Column('width', sa.Integer(), nullable=False),
        sa.Column('height', sa.Integer(), nullable=False),
        sa.Column('has_stickers', sa.Boolean(), nullable=False),
        sa.Column('file_id', sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(
            ['file_id'],
            ['file.file_id'],
            name='FK-photo-file_id-file-file_id'),

        sa.ForeignKeyConstraint(
            ['photo_set_id'],
            ['photo_set.photo_set_id'],
            name='FK-photo-photo_set_id-photo_set-photo_set_id'),

        sa.PrimaryKeyConstraint(
            'photo_id',
            name='PK-photo-photo_id')
    )

    op.create_index(
        index_name='IXUQ-photo-file_id',
        table_name='photo',
        columns=['file_id'],
        unique=True)



def downgrade():

    op.drop_index(
        index_name='IXUQ-photo-file_id',
        table_name='user')
    op.drop_table('photo')
