import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-2, -5), -7)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(8, 3), 5)
        self.assertEqual(self.calc.subtract(-2, 3), -5)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6) 
        self.assertEqual(self.calc.multiply(-2, 3), -6) 
        self.assertEqual(self.calc.multiply(-2, -3), 6) 

    def test_division(self):
        self.assertEqual(self.calc.divide(5, 1), 5) 
        self.assertEqual(self.calc.divide(20, 2), 10)
        self.assertEqual(self.calc.divide(-5, 1), -5)
        self.assertEqual(self.calc.divide(-5, -1), 5) 
        self.assertEqual(self.calc.divide(5, 0), None)   