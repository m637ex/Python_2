# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него функцию rename_files

from os import chdir
from pathlib import Path
__all__ = ['create_init']


def create_init(source_dir: Path=Path.cwd()):
    files_list = []
    for file in source_dir.iterdir():
        if file.suffix == '.py':
            with open(file, 'r', encoding='utf8') as file_py:
                for line in file_py.readlines():
                    if line.startswith('def'):
                        files_list.append(file.name.split('.')[0])
                        break
    with open("__init__.py", mode="w", encoding="UTF-8") as init_py:
        init_py.write(f'__all__ = {files_list}')
                

            
            # print(file.name)
            
        

if __name__ == "__main__":        
    chdir(r"G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files")     # Сменить текущий каталог 
    source_directory = Path.cwd()
    create_init(source_dir=source_directory)