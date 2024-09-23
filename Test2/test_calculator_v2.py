import unittest
from calculator_v2 import Calculator

class TestCalculatorV2(unittest.TestCase):
    def test_add(self):
        calc1 = Calculator(3, 4)
        result = calc1.calc_add()
        self.assertEqual(result, 7)

    @unittest.skip("Skipping test for subtraction")
    def test_add_with_negative_numbers(self):
        calc1 = Calculator(-3, -4)
        result = calc1.calc_add()
        self.assertEqual(result, -7)