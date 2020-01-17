from sqlalchemy import Column, Index, Integer, Unicode, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_repr import RepresentableBase

from sqlalchemy_utils import PhoneNumber

CustomDeclarativeBase = declarative_base(cls=RepresentableBase)


class User(CustomDeclarativeBase):

    __tablename__ = 'user'

    userid = Column(Integer, primary_key=True)

    # telegram fields
    tg_user_id = Column(Integer)
    first_name = Column(Unicode(length=100))
    last_name = Column(Unicode(length=100))
    user_name = Column(Unicode(length=100))
    phone_number = Column(PhoneNumber)

    # status = Column()
    # profile_photo = Column()
    # outgoing_link = Column()
    # incoming_link = Column()

    is_verified = Column(Boolean)
    is_support = Column(Boolean)
    restriction_reason = Column(Unicode(length=255))
    is_scam = Column(Boolean)
    have_access = Column(Boolean)

    # user_type = Column()

    language_code = Column(Unicode(length=20))

    __table_args__ = (

        # FIXME: does this create an index, or do i need to create a
        # index as well as a unique constraint?
        UniqueConstraint("tg_user_id", name="UQ-tg_user_id")
    )