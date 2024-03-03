# Задание №2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.


#from typing import Callable
from random import randint
__all__ = ['guess_game','guess_num']


def guess_num (func):
    NUM_MIN = 1
    NUM_MAX = 100
    COUNT_MIN = 1
    COUNT_MAX = 10
    def wrapper (num: int, count: int):
        if num < NUM_MIN or num > NUM_MAX:
            num = randint(NUM_MIN, NUM_MAX)
        if count < COUNT_MIN or count > COUNT_MAX:
            count = randint(COUNT_MIN, COUNT_MAX)
        return func(num, count)
    return wrapper


@guess_num
def guess_game (num: int, count: int) -> None:
    for i in range(1, count+1):
        print(f'Попытка {i} из {count}', end=' ')
        user_input_number = int(input("Введите отгадку: "))
        if user_input_number == num:
            print(f'Вы угадали. Было загадо число {num}.')
            return 
    print(f'Все попытки исчерпаны. Вы не угадали.')


if __name__ == '__main__':
    count = int(input("Введите колличество попыток угадывания от 1 до 10: "))
    number = int(input("Введите загадываемое число от 1 до 100: "))
    guess_game(number, count)