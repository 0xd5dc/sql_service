"""
Attempt use repository pattern to handle data transaction but this project doesn't use external APIs and SQLalchemy already functions like a repository with SQL database
"""
from sqlalchemy.exc import MultipleResultsFound, IntegrityError

from db import User, dal, Event


def create_user(session, user):
    try:
        session.add(user)
        session.commit()
    except IntegrityError as error:
        print("ignore for now")
    return user.user_id


def create_event(session, event):
    try:
        session.add(event)
        session.commit()
    except IntegrityError as error:
        print("ignore for now")
    return event.event_id


def read_users(session):
    """
    read_users gets all users in the database
    """
    return session.query(User).all()


def read_events(session):
    """
    read_events gets all events in the database
    """
    return session.query(Event).all()


def update_user_name_by_email(session, email, name):
    to_update = None
    try:
        query = session.query(User)
        query = query.filter(User.email == email)
        query.update({User.name: name})
        session.commit()
        to_update = query.first()
    except MultipleResultsFound as error:
        print('We found too many users... is that even possible?')
    return to_update


def update_event_detail_by_name(session, name, detail):
    to_update = None
    try:
        query = session.query(Event)
        query = query.filter(Event.name == name)
        query.update({Event.detail: detail})
        session.commit()
        to_update = query.first()
    except MultipleResultsFound as error:
        print('We found too many users... is that even possible?')
    return to_update


def delete_user_by_email(session, email):
    to_delete = None
    try:
        query = session.query(User)
        query = query.filter(User.email == email)
        to_delete = query.one()
        session.delete(to_delete)
        session.commit()
        to_delete = query.first()
    except MultipleResultsFound as error:
        print('We found too many users... is that even possible?')
    return to_delete


def delete_event_by_name(session, name):
    to_delete = None
    try:
        query = session.query(Event)
        query = query.filter(Event.name == name)
        to_delete = query.one()
        session.delete(to_delete)
        session.commit()
        to_delete = query.first()
    except MultipleResultsFound as error:
        print('We found too many users... is that even possible?')
    return to_delete


if __name__ == '__main__':
    create_event()
    read_events()
    delete_event_by_name()
    update_event_detail_by_name()
