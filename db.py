"""Database definition
this file define database migration using sqlalchemy.
tables: users, events, guests
users to events: one-to-many
guests: many to many
"""
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, create_engine, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    user_id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(25), nullable=False)
    password = Column("password", String(25), nullable=False)
    phone = Column("phone", String(20), unique=True)
    email = Column("email", String(255), nullable=False, unique=True)
    token = Column("token", String(255))
    email_confirmed = Column("email_confirmed", Boolean, default=False)
    created_at = Column("created_at", DateTime(), default=datetime.now)
    updated_at = Column('updated_at', DateTime(), default=datetime.now, onupdate=datetime.now)
    deleted_at = Column("deleted_at", DateTime(), default=None)


class Event(Base):
    __tablename__ = "events"

    event_id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(255), nullable=False)
    intro = Column("intro", String(255), nullable=False)
    owner_id = Column("owner_id", ForeignKey("users.id"), nullable=False)
    is_virtual = Column("is_virtual", Boolean)
    is_private = Column("is_private", Boolean)
    created_at = Column("created_at", DateTime(), default=datetime.now)
    updated_at = Column('updated_at', DateTime(), default=datetime.now, onupdate=datetime.now)
    deleted_at = Column("deleted_at", DateTime(), default=None)
    start_at = Column("start_at", DateTime())
    end_at = Column("end_at", DateTime())
    user = relationship("User", backref=backref('events', order_by=event_id))


class Guest(Base):
    __tablename__ = "guests"

    guest_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column("user_id", ForeignKey("users.id"), nullable=False, index=True)
    event_id = Column("event_id", ForeignKey("events.id"), nullable=False, index=True)
    # explicit/composite unique constraint.  ensure duplicated users in the same event.
    UniqueConstraint('user_id', 'event_id')


class DataAccessLayer:

    def __init__(self):
        self.engine = None
        self.conn_string = 'sqlite:///db.sqlite'

    def connect(self):
        self.engine = create_engine(self.conn_string)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)


dal = DataAccessLayer()
if __name__ == '__main__':
    engine = create_engine('sqlite:///:memory:')

    # create tables
    Base.metadata.create_all(engine)
