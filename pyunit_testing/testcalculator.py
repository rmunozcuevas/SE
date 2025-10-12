import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(3,2), 5)
        self.assertEqual(Calculator.add(-1, 5), 4)

    def test_sub(self):
        self.assertEqual(Calculator.subtract(3,2), 1)
        self.assertEqual(Calculator.subtract(10, 5), 5)
    
    def test_div(self):
        self.assertEqual(Calculator.divide(3,2), 1.5)
        self.assertEqual(Calculator.divide(10, 5), 2)
    
    def test_mult(self):
        self.assertEqual(Calculator.multiply(10,2), 20)
        self.assertEqual(Calculator.multiply(4, -3), -12)


if __name__ == "__main__":
    unittest.main()

