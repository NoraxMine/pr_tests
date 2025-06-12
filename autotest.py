import unittest
import math as m

def equation(a, b):
    y = m.sqrt((a + b) ** 3 / (a - b) ** 2)
    return round(y, 4)

class TestAddFunction(unittest.TestCase):
    def test_integer_positive_numbers(self):
        self.assertEqual(equation(2, 1), 5.1962)

    def test_integer_negative_numbers(self):
        self.assertEqual(equation(2, -1), 0.3333)

    def test_integer_negative_numbers(self):
        self.assertEqual(equation(-1, -1), ZeroDivisionError)

    def test_zero(self):
        self.assertEqual(equation(0, 0), ZeroDivisionError)

    def test_abc(self):
        self.assertEqual(equation("rgv", "st"), TypeError)
        self.assertEqual(equation("rgv", "1"), TypeError)
        self.assertEqual(equation('10**-9', 0), TypeError)
        self.assertEqual(equation(" ", "st"), TypeError)

    def test_negativ(self):
        self.assertEqual(equation(-20, -10), ValueError)

    def test_part(self):
        self.assertEqual(equation(0.2, 0.1), 1.6432)

    def test_negative_root(self):
        self.assertEqual(equation(1, -2), 'Complex_namber')
    

if __name__ == "__main__":
    unittest.main()
