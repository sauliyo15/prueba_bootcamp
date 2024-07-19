import unittest
from operaciones import dividir

class TestDividir(unittest.TestCase):

    def test_dividir(self):
        self.assertEqual(dividir(5, 2), 2.5)
        self.assertEqual(dividir(10, 0), "No se puede dividir por cero")
        self.assertEqual(dividir(4, -2), -2)

if __name__ == '__main__':
    unittest.main()