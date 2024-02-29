# Задание №5
# 📌 Напишите функцию, которая ищет json файлы в указаннойдиректории и 
# сохраняет их содержимое в виде одноимённых pickle файлов.


import json
import pickle
from pathlib import Path

__all__ = ['json_to_pickle']


def json_to_pickle(path: Path) -> None:
    for obj in Path.iterdir(path):  # Перебираем все объекты в папке
        if obj.is_file() and obj.suffix == '.json': # если объект файл и с расширением .json
            with open(obj, 'r', encoding="UTF-8") as file_rd: # Читаем  содержимое файла в data
                data = json.load(file_rd)
            with open(f'{obj.stem}.pickle', mode='wb') as file_wr:
                pickle.dump(data, file_wr)
    
    
if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    sourse_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    json_to_pickle(Path(sourse_directory))