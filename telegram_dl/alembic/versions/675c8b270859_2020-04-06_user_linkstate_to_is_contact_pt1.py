"""user linkstate to is_contact pt1

Revision ID: 675c8b270859
Revises: 3326eb4a8333
Create Date: 2020-04-06 19:49:33.311403

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = '675c8b270859'
down_revision = '3326eb4a8333'
branch_labels = None
depends_on = None


# This is part 1 of a 3 part process to make modifications to the `user` table, where
# `incoming_link` and `outgoing_link` (an enumeration of 0,1,2) to `is_contact` and
# `is_mutual_contact`
#
# part 1: add `is_contact` and `is_mutual_contact`
# part 2: go through each `user` and translate `incoming/outcoming_link` ->
#   `is_contact/is_mutual_contact`
# part 3: drop `incoming_link` and `outgoing_link`
#

def upgrade():

    with op.batch_alter_table('user', schema=None, recreate="always") as batch_op:
        batch_op.add_column(sa.Column('is_contact', sa.Boolean(), nullable=True), insert_after="profile_photo_id")
        batch_op.add_column(sa.Column('is_mutual_contact', sa.Boolean(), nullable=True), insert_after="is_contact")


def downgrade():

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_mutual_contact')
        batch_op.drop_column('is_contact')

