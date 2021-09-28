import unittest

from db import dal, User
from repo import read_users, create_user, delete_user_by_email, update_user_name_by_email


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.conn_string = 'sqlite:///:memory:'
        dal.connect()
        dal.session = dal.Session()

    def setUp(self):
        dal.session = dal.Session()

    def tearDown(self):
        dal.session.rollback()
        dal.session.close()

    def test_create_user(self):
        create_user(dal.session, User(name="Kay Doe", password="password", email="key.doe@mail.com"))
        users = read_users(dal.session)
        self.assertEqual(len(users), 1)

    def test_delete_user_by_email(self):
        create_user(dal.session, User(name="Kay Doe", password="password", email="key.doe@mail.com"))
        users = read_users(dal.session)
        self.assertEqual(len(users), 1)
        # create an user and expect 1 users in database
        delete_user_by_email(dal.session, email="key.doe@mail.com")
        users = read_users(dal.session)
        self.assertEqual(len(users), 0)
        # delete the user and expect 0 users in database

    def test_update_user_name_by_email(self):
        create_user(dal.session, User(name="Kay Doe", password="password", email="key.doe@mail.com"))
        users = read_users(dal.session)
        self.assertEqual(len(users), 1)
        # create an user and expect 1 users in database
        updated = update_user_name_by_email(dal.session, email="key.doe@mail.com", name="John Doe")
        self.assertEqual(updated.name, "John Doe")
        # delete the user and expect 0 users in database

    def test_read_users(self):
        users = read_users(dal.session)
        self.assertEqual(len(users), 0)  # add assertion here


if __name__ == '__main__':
    unittest.main()
