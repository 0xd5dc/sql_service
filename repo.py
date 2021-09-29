"""
Attempt use repository pattern to handle data transaction but this project doesn't use external APIs and SQLalchemy already functions like a repository with SQL database
"""
import logging

from sqlalchemy import update, select, delete
from sqlalchemy.exc import MultipleResultsFound, IntegrityError

from db import User, Event


def create_user(session, user):
    """
    create a user
    :param session:
    :param user:
    :return:
    """
    with session:
        session.begin()
        try:
            session.add(user)
        except Exception as e:
            logging.error(e)
            session.rollback()
            raise
        else:
            session.commit()


def create_event(session, event):
    """
    create an event
    :param session:
    :param event:
    :return:
    """
    with session:
        session.begin()
        try:
            session.add(event)
        except Exception as e:
            logging.error(e)
            session.rollback()
            raise
        else:
            session.commit()


def read_users(session):
    """
    read_users gets all users in the database
    :param session:
    :return:
    """
    return session.query(User).all()


def read_events(session):
    """
    read_events gets all events in the database
    :param session:
    :return:
    """
    return session.query(Event).all()


def update_user_name_by_email(session, email, name):
    """
    update user name by its email
    :param session:
    :param email:
    :param name:
    :return:
    """
    with session:
        user = session.execute(select(User).filter_by(email=email)).scalar_one()
        user.name = name
        session.commit()


def update_event_detail_by_name(session, name, detail):
    """
    update event detail by event name
    :param session:
    :param name:
    :param detail:
    :return:
    """
    with session:
        user = session.execute(select(User).filter_by(name=name)).scalar_one()
        user.detail = detail
        session.commit()


def delete_user_by_email(session, email):
    """
    delete user by email
    :param session:
    :param email:
    :return:
    """
    with session:
        session.execute(delete(User).where(User.email == email))
        session.commit()


def delete_event_by_name(session, name):
    """
    delete event by name
    :param session:
    :param name:
    :return:
    """
    with session:
        session.execute(delete(Event).where(Event.name == name))
        session.commit()
