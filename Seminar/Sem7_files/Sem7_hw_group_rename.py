# Напишите функцию группового переименования файлов в папке test_folder под названием 
# rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце 
# имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать 
# только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] 
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное 
# имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории
# Пример использования.
# На входе: rename_files(desired_name="new_file_", num_digits=3, source_ext="txt", target_ext="doc")
# На выходе: new_file_008.doc, test.doc, new_file_004.doc, new_file_005.doc, new_file_007.doc, new_file_001.doc, new_file_006.doc, new_file_003.doc, new_file_002.doc, new_file_009.doc, new_file_010.doc

import os
from pathlib import Path

__all__ = ["rename_files"]


def rename_files(
        source_dir: Path=Path("test_folder"),
        desired_name: str="",   # a. принимать параметр желаемое конечное имя файлов.
        num_digits: int=3,     # b. принимать параметр количество цифр в порядковом номере.
        source_ext: str="txt", # c. принимать параметр расширение исходного файла. 
        target_ext: str="doc", # d. принимать параметр расширение конечного файла.
        orig_name_interval: list=[0, 0],   # e. принимать диапазон сохраняемого оригинального имени.
        ):
    count = 1
    for file in source_dir.iterdir():   # перебираем все файлы в дирректории
        if file.suffix == f".{source_ext}": # если находим нужное разрешение            
            name = file.name[:-len(file.suffix)]    # отбрасываем расширение
            name = name[orig_name_interval[0]: orig_name_interval[1]]      # e. принимать диапазон сохраняемого оригинального имени
            Path(file).rename(fr"{source_directory}\{name}{desired_name}{str(count).zfill(num_digits)}.{target_ext}") # zfill - заполнение нулями слева до нужной длины
            count += 1
            # print(fr"{file.name} -> {source_directory}\{name}{desired_name}{str(count).zfill(num_digits)}.{target_ext}")

if __name__ == "__main__":        
    os.chdir(r"G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files")     # Сменить текущий каталог 
    source_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files\test_folder'
    #sort_files(source_directory)
    rename_files(source_dir=Path(source_directory),desired_name="file_", num_digits=3, source_ext="txt", target_ext="jpg", orig_name_interval=[0, 0])