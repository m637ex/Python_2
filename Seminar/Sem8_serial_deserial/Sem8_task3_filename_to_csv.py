# Задание №3
# 📌 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

import csv
import json
from pathlib import Path

__all__ = ['json_to_csv']

def json_to_csv(input_file: Path, output_file: Path):
    data = {}
    with open(input_file, mode='r', encoding="UTF-8") as file_in:
        data = json.load(file_in)
        rows = []
        for level, dict_level in data.items():
            for user_id, name in dict_level.items():
                rows.append({'Level':int(level), 'Id':int(user_id), 'Name':str(name)})
    with open(f"{output_file}", mode='w', newline='', encoding="UTF-8") as file_ex:
        csv_write = csv.DictWriter(file_ex, fieldnames=['Level', 'Id', 'Name'], \
            dialect='excel-tab') # создадим переменную с параметрами csv файла
        csv_write.writeheader()   # Загрузим заголовки в файл csv
        csv_write.writerows(rows)   # Загрузим список словарей в файл csv
        
            
if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    in_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task2_users.json'
    out_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task3_users.csv'
    json_to_csv(Path(in_file), Path(out_file))