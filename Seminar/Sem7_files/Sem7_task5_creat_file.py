# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from os import chdir
from random import randint, choices
from pathlib import Path
from string import ascii_lowercase, digits          #Библиотека символов

__all__ = ["generate_file","generate_file_and_extensoin"]


chdir(r"Seminar\Sem7_files")                 # Сменить текущий каталог

def generate_file_and_extensoin(**kwargs):
    for ext, count in kwargs.items():
        generate_file(extension=ext, numfiles=count)


def generate_file(
        extension: str='bin',
        min_len: int=6, 
        max_len:int=30, 
        min_size: int=256, 
        max_size: int=4096, 
        numfiles: int = 2) -> None:
    for _ in range(numfiles):
        name = ''.join(choices(ascii_lowercase + digits + "_", k=randint(min_len, max_len))) + extension
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(fr"{name}.{extension}", mode='wb') as file:
            file.write(data)

if __name__ == "__main__":
    generate_file_and_extensoin(txt = 2, bin = 1)
    # generate_file()