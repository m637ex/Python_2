# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from os import chdir
from pathlib import Path
from random import randint, choices
from string import ascii_lowercase, digits          #Библиотека символов

__all__ = ["create_file",'generate_file_and_extensoin']

# chdir(r"Seminar\Sem7_files")                 # Сменить текущий каталог


def generate_file_and_extensoin(path: str|Path, **kwargs):
    if isinstance(path, str):   # Если путь - строка, то
        path = Path(path)       # преобразуем строку в путь.
    if not path.is_dir():       # Если нет такой папки, то
        path.mkdir(parents=True)    # создадим её(с утётом создания родительских папок)
    chdir(path)                 # Сменить текущий каталог
        
    for ext, count in kwargs.items():
        create_file(extension=ext, numfiles=count)


def create_file(
        extension: str='bin',
        min_len: int=6, 
        max_len:int=30, 
        min_size: int=256, 
        max_size: int=4096, 
        numfiles: int = 2) -> None:
    for _ in range(numfiles):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + "_", k=randint(min_len, max_len)))
            name = f'{name}.{extension}'    # сохраним в имя: имя + расширение
            if not Path(name).is_file():    # если в каталоге нет файла c таким именем
                break   # выходим из цикла
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f"{name}", mode='wb') as file:
            file.write(data)

if __name__ == "__main__":    
    source_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files\test_folder'
    generate_file_and_extensoin(path=source_directory, jpg = 3, txt = 3, mkv = 3, bin = 3)
    