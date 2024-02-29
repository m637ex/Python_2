# Задание №4
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополните id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделайте прописной.
# 📌 Добавьте поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавайте как аргументы функции.

import csv
import json
from pathlib import Path

__all__ = ['csv_to_json']

count_nules = 10

def csv_to_json(input_file: Path, output_file: Path) -> None:
    data = []
    with open(input_file, mode='r', newline='', encoding="UTF-8") as csv_file:
        csv_read = csv.reader(csv_file, dialect='excel-tab')
        for i, line in enumerate(csv_read):
            if i:                   # пропускаем 1 строку с заголовками
                json_dict = {}
                level, user_id, name = line
                json_dict['level'] = int(level)
                json_dict['id'] = f'{int(user_id):010}' # добаавляем нули до 10 символов
                json_dict['name'] = name.title() # c заглавной буквы
                json_dict['has'] = hash(f'{json_dict['name']}{json_dict['id']}')
                data.append(json_dict)
    with open(output_file, mode='w', encoding="UTF-8") as file_out:
        json.dump(data, file_out, indent=4, ensure_ascii=False)

        
            
if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    in_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task3_users.csv'
    out_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task4_users.json'
    csv_to_json(Path(in_file), Path(out_file))