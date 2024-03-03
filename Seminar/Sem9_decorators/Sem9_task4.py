# Задание №4
# 📌 Создайте декоратор с параметром.
# 📌 Параметр - целое число, количество запусков декорируемой функции


from random import randint
from os import chdir
from pathlib import Path
from typing import Callable
import json
__all__ = ['count_save_to_json','rand']
chdir(fr'g:\YandexDisk\GB\Python\Python_2\Seminar\Sem9_decorators')


def count_save_to_json(count: int):    
    def save_to_json(func: Callable):
        '''Read arguments from json file'''
        list_of_dicts = []  #
        file = Path(f'{func.__name__}.json')
        if file.is_file():
            with open(file, mode='r', encoding="UTF-8") as f:
                list_of_dicts = json.load(f)
        def get_arg(*args, **kwargs):
            '''Get arguments from func and export them to json file'''
            for i in range(count):
                json_dict = {'args': args, **kwargs}    # сохраянем в итоговый словарь все параметры
                result = func(*args, **kwargs)          # Получаем результат выполнения функции
                json_dict['result'] = result
                list_of_dicts.append(json_dict)               
                print(f"Получены параметры: {args = }, {kwargs = }, {json_dict = }")
                with open(file, mode='w', encoding="UTF-8") as f:
                    json.dump(list_of_dicts, f)
            #return func(*args, **kwargs)
        return get_arg
    return save_to_json    


@count_save_to_json(3)
def rand (num1: int, num2:int) -> int:                 # Функция для декорирования
    return randint(num1, num2)


if __name__ == '__main__':
    num_min = 1
    num_max = 100
    print(rand(num_min, num2=num_max))