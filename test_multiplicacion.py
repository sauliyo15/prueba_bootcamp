import unittest
from operaciones import multiplicar

class TestMultiplicar(unittest.TestCase):

    def test_restar(self):
        self.assertEqual(multiplicar(5, 2), 10)
        self.assertEqual(multiplicar(-7, -4), 28)
        self.assertEqual(multiplicar(5, 7), 35)

if __name__ == '__main__':
    unittest.main()