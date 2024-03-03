# Задание №3
# 📌 Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, 
# который она возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# 📌 Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# 📌 Для декорирования напишите функцию, которая может принимать как позиционные,
# так и ключевые аргументы.
# 📌 Имя файла должно совпадать с именем декорируемой функции.


from random import randint
from os import chdir
from pathlib import Path
from typing import Callable
import json
__all__ = ['rand','save_to_json']
chdir(fr'g:\YandexDisk\GB\Python\Python_2\Seminar\Sem9_decorators')


def save_to_json(func: Callable):
    '''Export arguments to json file'''
    list_of_dicts = []  #
    file = Path(f'{func.__name__}.json')
    if file.is_file():
        with open(file, mode='r', encoding="UTF-8") as f:
            list_of_dicts = json.load(f)
    def get_arg(*args, **kwargs):
        json_dict = {'args': args, **kwargs}    # сохраянем в итоговый словарь все параметры
        result = func(*args, **kwargs)          # Получаем результат выполнения функции
        json_dict['result'] = result
        list_of_dicts.append(json_dict)               
        print(f"Получены параметры: {args = }, {kwargs = }, {json_dict = }")
        with open(file, mode='w', encoding="UTF-8") as f:
            json.dump(list_of_dicts, f)
        #return func(*args, **kwargs)
    return get_arg


@save_to_json
def rand (num1: int, num2:int) -> int:                 # Функция для декорирования
    return randint(num1, num2)


if __name__ == '__main__':
    num_min = 1
    num_max = 100
    print(rand(num_min, num2=num_max))