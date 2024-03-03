# Задание №6
# 📌 Доработайте прошлую задачу добавив декоратор wraps в каждый из декораторов.

from random import randint
from os import chdir
from pathlib import Path
from typing import Callable
from functools import wraps
import json
__all__ = ['guess_game','save_to_json']
chdir(fr'g:\YandexDisk\GB\Python\Python_2\Seminar\Sem9_decorators')


def save_to_json(func: Callable):
    '''Read arguments from json file'''
    list_of_dicts = []  #
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, mode='r', encoding="UTF-8") as f:
            list_of_dicts = json.load(f)
    @wraps(func)
    def get_arg(*args, **kwargs):
        '''Get arguments from func and export them to json file'''
        json_dict = {'args': args, **kwargs}    # сохраянем в итоговый словарь все параметры
        result = func(*args, **kwargs)          # Получаем результат выполнения функции
        json_dict['result'] = result
        list_of_dicts.append(json_dict)               
        print(f"Получены параметры: {args = }, {kwargs = }, {json_dict = }")
        with open(file, mode='w', encoding="UTF-8") as f:
            json.dump(list_of_dicts, f)
        #return func(*args, **kwargs)
    return get_arg 

def number_of_launches(count:int):      # Параметры
    def start_function(func: Callable): # Функция
        @wraps(func)
        def start(*args, **kwargs):     # Аргументы
            for i in range(count):
                func(*args, **kwargs)
        return start
    return start_function


def check_arg(func: Callable):
    NUM_MIN = 1
    NUM_MAX = 100
    COUNT_MIN = 1
    COUNT_MAX = 10
    @wraps(func)
    def wrapper (num: int, count: int):
        if num < NUM_MIN or num > NUM_MAX:
            num = randint(NUM_MIN, NUM_MAX)
        if count < COUNT_MIN or count > COUNT_MAX:
            count = randint(COUNT_MIN, COUNT_MAX)
        return func(num, count)
    return wrapper
    
@number_of_launches(3)
@check_arg
@save_to_json
def guess_game (num: int, count: int):
    '''Игра с угадываением числа'''
    for i in range(1, count+1):
        print(f'Попытка {i} из {count}', end=' ')
        user_input_number = int(input("Введите отгадку: "))
        if user_input_number == num:
            print(f'Вы угадали. Было загадо число {num}.')
            return True
    else:
        print(f'Все попытки исчерпаны. Вы не угадали.')
        return False


if __name__ == '__main__':
    print(help(guess_game))
    count = int(input("Введите колличество попыток угадывания от 1 до 10: "))
    number = int(input("Введите загадываемое число от 1 до 100: "))
    guess_game(number, count)