# Задание №2
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция принимает на вход три целых числа: нижнюю и
# верхнюю границу и количество попыток.
# 📌 Внутри генерируется случайное число в указанных границах
# и пользователь должен угадать его за заданное число
# попыток.
# 📌 Функция выводит подсказки “больше” и “меньше”.
# 📌 Если число угадано, возвращается истина, а если попытки
# исчерпаны - ложь.

from Sem6_task2_random_mod import comparison as comp    # Импортируем модуль comparision из файла Sem6_task2_modul1.py

print(comp(1, 100, 3))