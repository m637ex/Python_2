# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

import random
from pathlib import Path

MIN_LIMIT = -1000
MAX_LIMIT = 1000

def write_random_to_file(num_pairs: int, filename: str):
    with open(f'Seminar\Sem7_files\{filename}', 'a', encoding="utf-8") as f:
        for _ in range(num_pairs):
            f.write(f'{random.randint(MIN_LIMIT, MAX_LIMIT):<5}|{random.uniform(MIN_LIMIT, MAX_LIMIT)}\n')


write_random_to_file(15, "gen_num.txt")

   