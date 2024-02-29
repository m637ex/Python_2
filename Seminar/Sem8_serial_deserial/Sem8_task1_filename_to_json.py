# Задание №1
# 📌 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
#   текстовый файл с псевдо именами и произведением чисел.
# 📌 Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# 📌 Имена пишите с большой буквы.
# 📌 Каждую пару сохраняйте с новой строки.

import json
from pathlib import Path

__all__ = ['convert_to_json']

def convert_to_json(input_file: Path, output_file: Path):
    data = {}
    with open(input_file, 'r') as file:
        for line in file:
            name, number = line.split()
            print(name + '|' + number)
            data[name.capitalize()] = float(number)     # capitalize - C заглавной буквы
    with open(output_file, 'w', encoding="UTF-8") as file_ex:
        json.dump(data, file_ex, ensure_ascii=False)   # отменяем обязательную ensure_ascii         
            
if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    in_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files\task3_result.txt'
    out_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task1_result.json'
    convert_to_json(Path(in_file), Path(out_file))