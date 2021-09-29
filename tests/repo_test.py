import unittest

from db import dal, User, Event
from db_seeder import run_seeder
from repo import read_users, create_user, delete_user_by_email, update_user_name_by_email, create_event, read_events, \
    delete_event_by_name, update_event_detail_by_name


class MyTestCase(unittest.TestCase):
    user_size, event_size, guest_size = 10, 30, 50
    user = User(name="Kay Doe", password="password", email="key.doe@mail.com")
    event = Event(name="birthday party", detail="celebrate birthday", owner_id=1)

    @classmethod
    def setUpClass(cls):
        dal.conn_string = 'sqlite:///:memory:'
        dal.connect()
        dal.session = dal.Session(future=True)
        run_seeder(dal.session, cls.user_size, cls.event_size, cls.guest_size)
        dal.session.close()

    def setUp(self):
        dal.session = dal.Session(future=True)

    def tearDown(self):
        dal.session.rollback()
        dal.session.close()

    def test_read_users(self):
        users = read_users(dal.session)
        self.assertEqual(len(users), self.user_size)  # length of user table should be user_size

    def test_read_events(self):
        events = read_events(dal.session)
        self.assertEqual(len(events), self.event_size)  # empty table should be 0

    def test_create_user(self):
        create_user(dal.session, user=self.user)
        users = read_users(dal.session)
        self.assertEqual(len(users), self.user_size + 1)  # length of user table should be user_size

    def test_create_event(self):
        create_event(dal.session, self.event)
        events = read_events(dal.session)
        self.assertEqual(len(events), self.event_size + 1)

    def test_update_user_name_by_email(self):
        user = dal.session.query(User).first()
        new_name = "John Doe"
        update_user_name_by_email(dal.session, email=user.email, name=new_name)
        self.assertEqual(user.name, new_name)

    def test_update_event_detail_by_name(self):
        event = dal.session.query(Event).first()
        new_detail = "blow candles and eat cakes"
        update_event_detail_by_name(dal.session, name=event.name, detail=new_detail)
        self.assertEqual(event.detail, new_detail)

    def test_delete_user_by_email(self):
        user = dal.session.query(User).first()
        delete_user_by_email(dal.session, user.email)
        self.assertIsNotNone(user.deleted_at)
        self.assertEqual(type(user.created_at), type(user.deleted_at))
        # soft delete touch the delete_at, which should be a not None datetime type

    def test_delete_event_by_name(self):
        event = dal.session.query(Event).first()
        delete_event_by_name(dal.session, event.name)
        self.assertIsNotNone(event.deleted_at)
        self.assertEqual(type(event.created_at), type(event.deleted_at))
        # soft delete touch the delete_at, which should be a not None datetime type


if __name__ == '__main__':
    unittest.main()
