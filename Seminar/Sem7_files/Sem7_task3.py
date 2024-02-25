# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


from pathlib import Path
from typing import TextIO
    

def read_or_begin(fd: TextIO) -> str:   # крутис майл покургу
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip() # убираем пробелы в начале и конце строки


def converte(f_num_file: str | Path, f_name_file: str | Path, file: str | Path = 'task3.txt') -> None:
    with (
        open(f'Seminar\Sem7_files\{f_num_file}', mode='r', encoding='utf-8') as f_num,
        open(f'Seminar\Sem7_files\{f_name_file}', mode='r', encoding='utf-8') as f_name,
        open(f'Seminar\Sem7_files\{file}', mode='w', encoding='utf-8') as f_result,
        ):
        len_list_f_num = sum(1 for _ in f_num)
        len_list_f_name = sum(1 for _ in f_name)
        print(f'{len_list_f_num = }, {len_list_f_name = }')
        for _ in range(max(len_list_f_num, len_list_f_name)):
            nums_str = read_or_begin(f_num)
            name_str = read_or_begin(f_name)
            num_i, num_f = nums_str.split("|")
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_result.writelines(f'{name_str.lower()} {-mult}\n')
            else:
                f_result.writelines(f'{name_str.upper()} {int(mult)}\n')
    

converte('gen_num.txt', 'gen_name.txt', 'task3_result.txt')
        

        

        