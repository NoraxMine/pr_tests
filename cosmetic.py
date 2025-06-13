import unittest
from function import func
import math as m

class TestAddFunction(unittest.TestCase):
    def test_1(self):
        self.assertNotEqual(func(1, 2, 3), 0)

    def test_2(self):
        self.assertLess(func(1, 2, 3), 0)

    def test_raises(self):
        self.assertEqual(func(1, 1, 0), m.inf)
           
    def test_fact(self):
        self.assertEqual(func(-1, 5, 3), 'Неверный тип')

    def test_word(self):
        with self.assertRaises(TypeError):
            func("cjn", "webh", 3)

    def test_coren(self):
        self.assertEqual(func(1, -5, 3), 'Невозможно найти корень отрицательного числа')
            
    def test_drob(self):
        self.assertEqual(func(1.1, 5, 3), 'Невозможно найти факториал дробногоо числа')

    def test_drob_nool(self):
        self.assertEqual(func(-0.1, 5, 3), 'Нельзя найти факториал')

if __name__ == "__main__":
    unittest.main()