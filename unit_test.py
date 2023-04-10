import unittest
from main import quadratic_equation

class TestQuadraticEquation(unittest.TestCase):
    def test_no_real_roots(self):
        self.assertEqual(quadratic_equation(1, 2, 3), "No real roots exist")

    def test_one_real_root(self):
        self.assertEqual(quadratic_equation(1, -2, 1), "The equation has one root: x = 1.0")

    def test_two_real_roots(self):
        self.assertEqual(quadratic_equation(1, -7, 10), "The equation has two roots: x1 = 5.0 and x2 = 2.0")

if __name__ == '__main__':
    unittest.main()