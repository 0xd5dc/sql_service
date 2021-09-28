"""
Attempt use repository pattern to handle data transaction but this project doesn't use external APIs and SQLalchemy already functions like a repository with SQL database
"""
from sqlalchemy.exc import MultipleResultsFound, IntegrityError

from db import User, dal


def create_user(session, user):
    try:
        session.add(user)
        session.commit()
    except IntegrityError as error:
        print("ignore for now")
    return user.user_id


def read_users(session):
    """
    read_users gets all users in the database
    """
    return session.query(User).all()


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


if __name__ == '__main__':
    pass
