"""
Attempt use repository pattern to handle data transaction but this project doesn't use external APIs and SQLalchemy already functions like a repository with SQL database
"""
from db import User, dal


def create_user():
    pass


def read_users(session):
    """
    read_users gets all users in the database
    """
    return session.query(User).all()


def update_users():
    pass


def delete_users():
    pass


if __name__ == '__main__':
    create_user()
    dal.connect()
    session = dal.Session()
    users = read_users(session)

    update_users()
    delete_users()
