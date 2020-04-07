"""user linkstate to is_contact pt2

Revision ID: 7e8216a14a06
Revises: 675c8b270859
Create Date: 2020-04-06 19:52:53.478024

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import select
from sqlalchemy.orm.session import Session

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme

# revision identifiers, used by Alembic.
revision = '7e8216a14a06'
down_revision = '675c8b270859'
branch_labels = None
depends_on = None

# This is part 2 of a 3 part process to make modifications to the `user` table, where
# `incoming_link` and `outgoing_link` (an enumeration of 0,1,2) to `is_contact` and
# `is_mutual_contact`
#
# part 1: add `is_contact` and `is_mutual_contact`
# part 2: go through each `user` and translate `incoming/outcoming_link` ->
#   `is_contact/is_mutual_contact`
# part 3: drop `incoming_link` and `outgoing_link`
#


# here is the definition of LinkStateEnum which is the 'enum' in
# `outgoing_link` and `incoming_link`, for reference
#
# class LinkStateEnum(enum.Enum):
#     LINK_STATE_NONE = 0
#     LINK_STATE_IS_CONTACT = 1
#     LINK_STATE_KNOWS_PHONE_NUMBER = 2
#

def bool_to_int(bool_val):
    if bool_val:
        return 1
    else:
        return 0

def upgrade():

    # NOTE: I cannot rely on the 'mapped' declarative classes here
    # because that will probably work NOW, but once i delete LinkStateEnum
    # because it is no longer needed, this code would not work, and it would
    # get confused when accessing those fields in User.
    # so we are going to do this with raw-ish SQL, using the "SQLAlchemy expression language"
    # see https://docs.sqlalchemy.org/en/14/core/tutorial.html#inserts-updates-and-deletes

    bind = op.get_bind()
    session = Session(bind=bind)
    conn = session.connection()

    u_table = dbm.User.__table__
    select_stmt = select([u_table])

    with op.batch_alter_table('user', schema=None) as batch_op:

        select_result = conn.execute(select_stmt)

        for row in select_result:

            # outgoing link seems to be 1 if WE have their phone number
            # , the only person with 2 is the telegram bot
            # incoming link seems to be 1 if the other person has our phone number
            # but i don't see any 2 entries

            # Here, i am imagining a instance where this migration script runs but
            # we have already deleted the `LinkStateEnum` class, so we need to handle
            # if we get a int back or a LinkStateEnum object
            outgoing_link = row["outgoing_link"]
            if not isinstance(outgoing_link, int):
                outgoing_link = outgoing_link.value

            incoming_link = row["incoming_link"]
            if not isinstance(incoming_link, int):
                incoming_link = incoming_link.value

            new_is_contact = outgoing_link in (1,2)
            new_is_mutual_contact = incoming_link in (1,2) and outgoing_link in (1,2)

            update_stmt = u_table.update().where(u_table.c.user_id == row["user_id"]).values(
                is_contact=bool_to_int(new_is_contact),
                is_mutual_contact=bool_to_int(new_is_mutual_contact))

            conn.execute(update_stmt)

        session.commit()


def downgrade():

    # we don't do anything because the next revision up deletes the columns we are
    # modifying here
    with op.batch_alter_table('user', schema=None) as batch_op:
        pass