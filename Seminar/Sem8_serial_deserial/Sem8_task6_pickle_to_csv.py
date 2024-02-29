# Задание №6
# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv
from pathlib import Path

__all__ = ['pickle_to_csv']

def pickle_to_csv(input_file: Path, output_file: Path) -> None:
    with (
        open(input_file, mode='rb') as file_rd,
        open(output_file, mode='w', newline='', encoding="UTF-8") as file_wr
    ):
        data = pickle.load(file_rd)
        keys = data[0].keys()   # список заголовков
        csv_writer = csv.DictWriter(file_wr, fieldnames=keys, dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)        
        

if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    in_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task4_users.pickle'
    out_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task6_users.csv'
    pickle_to_csv(Path(in_file), Path(out_file))