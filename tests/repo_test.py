import unittest

from db import dal
from repo import read_users


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.conn_string = 'sqlite:///db.sqlite'
        dal.connect()

    def test_create_user(self):
        session = dal.Session()

    def test_read_users(self):
        session = dal.Session()
        users = read_users(session)
        session.commit()
        self.assertEqual(len(users), 50)  # add assertion here


if __name__ == '__main__':
    unittest.main()
