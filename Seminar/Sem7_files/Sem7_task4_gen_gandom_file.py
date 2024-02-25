# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


from os import chdir
from random import randint, choices
from pathlib import Path
from string import ascii_lowercase, digits          #Библиотека символов

__all__ = ["generate_file"]

chdir(r"Seminar\Sem7_files")                 # Сменить текущий каталог

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
        with open(fr"Seminar\Sem7_files\{name}.{extension}", mode='wb') as file:
            file.write(data)

if __name__ == "__main__":
    generate_file()