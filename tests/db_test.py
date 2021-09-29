import unittest

from db import dal


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.conn_string = 'sqlite:///:memory:'
        dal.connect()

    def setUp(self):
        dal.session = dal.Session()

    def tearDown(self):
        dal.session.rollback()
        dal.session.close()

    def test_tables(self):
        results = dal.session.execute("SELECT name FROM sqlite_master").fetchall()
        self.assertGreaterEqual(len(results), 3)
        # db.py created 3 tables and the results should be at least 3
        self.assertIn(('users',), results)
        self.assertIn(('events',), results)
        self.assertIn(('guests',), results)
        # check if table name exists


if __name__ == '__main__':
    unittest.main()
