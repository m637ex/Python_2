# Задание №7
# 📌 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатайте его как pickle строку.


import csv
from pathlib import Path
import pickle

__all__ = ['csv_as_pickle']

def csv_as_pickle(input_file: Path) -> None:
    pickle_list = []
    with open(input_file, mode='r', newline='', encoding="UTF-8") as file_rd:
        csv_reader = csv.reader(file_rd, dialect='excel-tab')
        for i, row in enumerate(csv_reader):
            if i == 0:
                keys = row
            else:
                pickle_dict = dict(zip(keys, row))
                pickle_list.append(pickle_dict)
    print(pickle.dumps(pickle_list))
    

if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    in_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task6_users.csv'
    csv_as_pickle(Path(in_file))