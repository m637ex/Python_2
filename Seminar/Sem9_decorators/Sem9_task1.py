# Задание №1
# 📌 Создайте функцию-замыкание, которая запрашивает два целых числа:
#     от 1 до 100 для загадывания,
#     от 1 до 10 для количества попыток
# 📌 Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from typing import Callable
__all__ = ['guess_num']

def guess_num (num: int, count:int) -> Callable:
    def guess_game () -> None:
        for i in range(1, count+1):
            print(f'Попытка {i}.', end=' ')
            user_input_number = int(input("Введите отгадку: "))
            if user_input_number == num:
                print(f'Вы угадали')
                return
    return guess_game


if __name__ == '__main__':
    count = int(input("Введите колличество попыток угадывания от 1 до 10: "))
    number = int(input("Введите загадываемое число от 1 до 100: "))
    game = guess_num(number, count) # Вызываем 1 функцию которая вернёт функцию
    game()  # Вызовем 2 функцию внутри функции
    game()  # Вызовем 2 функцию внутри функции 2 раз и 3-ий и сколько угодна раз. в функции уже зугружено число и попытки