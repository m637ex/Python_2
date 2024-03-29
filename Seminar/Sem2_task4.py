# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
import decimal

decimal.getcontext().prec = 50    # Задаём точность 50 знаков после запятой для decimal
PI = decimal.Decimal(math.pi)

d = decimal.Decimal(input('Введите диаметр окружности: '))  
l = d * PI
s = PI * (d/2)**2
print(f'Длина окружности: {l}\nПлощадь круга: {s}')
