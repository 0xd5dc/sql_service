import unittest

from db import dal


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.conn_string = 'sqlite:///:memory:'
        dal.connect()

    def test_tables(self):
        session = dal.Session()
        results = session.execute("SELECT name FROM sqlite_master").fetchall()
        self.assertGreaterEqual(len(results), 3)  # db.py created 3 tables and the results should be at least 3


if __name__ == '__main__':
    unittest.main()
