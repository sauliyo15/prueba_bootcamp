import unittest
from operaciones import restar

class TestRestar(unittest.TestCase):

    def test_restar(self):
        self.assertEqual(restar(5, 2), 3)
        self.assertEqual(restar(-7, -4), -3)
        self.assertEqual(restar(15, 7), 8)

if __name__ == '__main__':
    unittest.main()