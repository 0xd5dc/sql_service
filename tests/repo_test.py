import unittest

from db import dal, User, Event
from repo import read_users, create_user, delete_user_by_email, update_user_name_by_email, create_event, read_events, \
    delete_event_by_name, update_event_detail_by_name


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
        self.assertEqual(len(users), 0)  # empty table should be 0

    def test_create_event(self):
        owner_id = create_user(dal.session, User(name="Kay Doe", password="password", email="key.doe@mail.com"))
        create_event(dal.session, Event(name="brithday party", detail="celebrate birthday", owner_id=owner_id))
        events = read_events(dal.session)
        self.assertEqual(len(events), 1)

    def test_delete_event_by_email(self):
        owner_id = create_user(dal.session, User(name="Kay Doe", password="password", email="key.doe@mail.com"))
        create_event(dal.session, Event(name="brithday party", detail="celebrate birthday", owner_id=owner_id))
        events = read_events(dal.session)
        self.assertEqual(len(events), 1)
        # create an user and expect 1 users in database
        delete_event_by_name(dal.session, name="brithday party")
        users = read_events(dal.session)
        self.assertEqual(len(users), 0)
        # delete the user and expect 0 users in database

    def test_update_event_name_by_email(self):
        owner_id = create_user(dal.session, User(name="Kay Doe", password="password", email="key.doe@mail.com"))
        create_event(dal.session, Event(name="brithday party", detail="celebrate birthday", owner_id=owner_id))
        events = read_events(dal.session)
        self.assertEqual(len(events), 1)
        # create an user and expect 1 users in database
        updated = update_event_detail_by_name(dal.session, name="brithday party", detail="blow candles and eat cakes")
        self.assertEqual(updated.detail, "blow candles and eat cakes")

    def test_read_events(self):
        users = read_events(dal.session)
        self.assertEqual(len(users), 0)  # empty table should be 0


if __name__ == '__main__':
    unittest.main()
