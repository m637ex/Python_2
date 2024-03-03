# Создайте функцию generate_csv_file(file_name, rows), которая будет генерировать по три случайных
# числа в каждой строке, от 100-1000 строк, и записывать их в CSV-файл. 
# Функция принимает два аргумента:
#     file_name (строка) - имя файла, в который будут записаны данные.
#     rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.
# Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения вида:
#     ax^2 + bx + c = 0. 
# Функция принимает три аргумента:
#     a, b, c (целые числа) - коэффициенты квадратного уравнения.
# Функция возвращает:
#     None, если уравнение не имеет корней (дискриминант отрицателен).
#     Одно число, если уравнение имеет один корень (дискриминант равен нулю).
#     Два числа (корни), если уравнение имеет два корня (дискриминант положителен).
# Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. 
# Декоратор выполняет следующие действия:
#     Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
#     Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
#     Сохраняет результаты в формате JSON в файл results.json. Каждая запись JSON содержит 
#     параметры a, b, c и результаты вычислений.
# Таким образом, после выполнения функций generate_csv_file и find_roots в файле results.json 
#     будет сохранена информация о параметрах и результатах вычислений для каждой строки данных 
#     из CSV-файла.

# Пример
# На входе:
# generate_csv_file("input_data.csv", 101)
# find_roots("input_data.csv")
# with open("results.json", 'r') as f:
#     data = json.load(f)
# if 100<=len(data)<=1000:
#     print(True)
# else:
#     print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
# print(len(data)==101)

# На выходе:
# True
# True

# Формат JSON файла определён следующим образом:
# [
#     {"parameters": [a, b, c], "result": result},
#     {"parameters": [a, b, c], "result": result},
#     ...
# ]


from random import randint
import csv
import json
from typing import Callable
from os import chdir
chdir(fr'g:\YandexDisk\GB\Python\Python_2\Seminar\Sem9_decorators')

COLUMNS = 3

def save_to_json(func: Callable):
    def wrapper(filename):
        with open(filename, 'r', encoding='UTF-8') as file:
            results = []
            csv_reader = csv.reader(file)
            for line in csv_reader:
                a, b, c = map(int, line)  
                roots = func(a, b, c)
                results.append({"parameters": [a, b, c], "result": roots})
        with open(f'results.json', 'w', encoding="UTF-8") as file:
            json.dump(results, file)
    return wrapper   


def generate_csv_file(file_name, rows):
    result_dict = {str(row):[str(randint(1, 100)) for _ in range(COLUMNS)] for row in range(rows)}
    # print (result_dict)
    with open(file_name, 'w', newline='', encoding="UTF-8") as f:
        csv_write = csv.writer(f)
        for _ in range(rows):
            row = [randint(1, 100) for _ in range(COLUMNS)]
            csv_write.writerow(row)


@save_to_json
def find_roots(a: int, b: int, c: int):    
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        return x
    return None


generate_csv_file("input_data.csv", 101)
find_roots("input_data.csv")
with open("results.json", 'r') as f:
    data = json.load(f)
if 100<=len(data)<=1000:
    print(True)
else:
    print(f"Количество строк в файле не находится в диапазоне от 100 до 1000.")
print(len(data)==101)