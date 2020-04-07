"""user linkstate to is_contact pt3

Revision ID: f79b2f534252
Revises: 7e8216a14a06
Create Date: 2020-04-06 21:08:29.297591

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = 'f79b2f534252'
down_revision = '7e8216a14a06'
branch_labels = None
depends_on = None

# This is part 3 of a 3 part process to make modifications to the `user` table, where
# `incoming_link` and `outgoing_link` (an enumeration of 0,1,2) to `is_contact` and
# `is_mutual_contact`
#
# part 1: add `is_contact` and `is_mutual_contact`
# part 2: go through each `user` and translate `incoming/outcoming_link` ->
#   `is_contact/is_mutual_contact`
# part 3: drop `incoming_link` and `outgoing_link`
#

def upgrade():

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('incoming_link')
        batch_op.drop_column('outgoing_link')


def downgrade():

    # we can't really recreate the data though, but we can add the columns
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('outgoing_link', sa.INTEGER(), nullable=True))
        batch_op.add_column(sa.Column('incoming_link', sa.INTEGER(), nullable=True))

