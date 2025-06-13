import math as m

def func(a, b, c):
    try:
        y = ((m.factorial(a) - (m.sqrt(b)))/(c ** 3))
        return round(y, 4)
    except ZeroDivisionError:
        return m.inf
    
    except TypeError:
        if a <= 0:
            return "Нельзя найти факториал"
        elif isinstance(a, float):
            return "Невозможно найти факториал дробногоо числа"
        else:
            return "Неизвестная ошибка"
    except ValueError:
        if b < 0:
            return "Невозможно найти корень отрицательного числа"
        else:
            return "Неверный тип"
# print(func(1, 2, 3))