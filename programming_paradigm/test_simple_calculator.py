import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Regular addition
        self.assertEqual(self.calc.add(-1, 1), 0)  # Adding negative and positive number
        self.assertEqual(self.calc.add(-2, -3), -5)  # Adding two negative numbers
        self.assertEqual(self.calc.add(0, 0), 0)  # Edge case: adding zeros

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Regular subtraction
        self.assertEqual(self.calc.subtract(2, 5), -3)  # Subtracting larger from smaller
        self.assertEqual(self.calc.subtract(-3, -5), 2)  # Subtracting negative numbers
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Edge case: subtracting zeros

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Regular multiplication
        self.assertEqual(self.calc.multiply(-2, 3), -6)  # Multiplying a negative number
        self.assertEqual(self.calc.multiply(0, 10), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, -3), 6)  # Multiplying two negative numbers

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Regular division
        self.assertEqual(self.calc.divide(-6, 3), -2)  # Division with a negative number
        self.assertEqual(self.calc.divide(0, 5), 0)  # Dividing zero by a number
        self.assertEqual(self.calc.divide(5, 0), None)  # Division by zero (edge case)

    def test_invalid_inputs(self):
        """Test invalid inputs for division and other operations."""
        # Test if the calculator correctly handles invalid inputs
        self.assertEqual(self.calc.divide('a', 2), None)  # Invalid input (string instead of number)
        self.assertEqual(self.calc.divide(5, 'b'), None)  # Invalid input (string instead of number)

if __name__ == "__main__":
    unittest.main()
