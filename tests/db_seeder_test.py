import unittest

from db_seeder import user_seeder, event_seeder, guest_seeder


class MyTestCase(unittest.TestCase):
    def test_user_seeder(self):
        self.assertEqual(len(user_seeder(10)), 10)

    def test_user_seeder(self):
        self.assertEqual(len(event_seeder(3, 30)), 3)

    def test_user_seeder(self):
        self.assertEqual(len(guest_seeder(5, 10, 5)), 5)


if __name__ == '__main__':
    unittest.main()
