# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os 
from pathlib import Path

__all__ = ["sort_files",'sort_files_2']


def sort_files(source_dir: str|Path):
    video_ext = ['.mov', '.mp4', '.mkv']
    image_ext = ['.png','.jpg','.jpeg']
    text_ext = ['.txt','.doc','.pdf']
    
    for file in os.listdir(source_dir):    # Перебрать все объекты в каталоге поиска
        if os.path.isfile(os.path.join(source_dir, file)):  # Если файл действительно файл, то
            file_ext = os.path.splitext(file)[1].lower()
            if not os.path.exists(dist_folder):
                os.mkdir(dist_folder)
            if file_ext in video_ext:
                dist_folder = os.path.join(source_dir,"Video_sort")   # папка назначения
            elif file_ext in image_ext:
                dist_folder = os.path.join(source_dir,"Image_sort")   # папка назначения
            elif file_ext in text_ext:
                dist_folder = os.path.join(source_dir,"Text_sort")   # папка назначения
            os.replace(os.path.join(source_dir, file), os.path.join(dist_folder, file))  
            
            
def sort_files_2(path: Path, groups: dict[Path, list[str]] = None) -> None: # без None не работает
    os.chdir(path)
    if groups is None:  # группы по умолчанию, если не переданы
        groups = {
            Path("Video") : ['mov', 'mp4', 'mkv'],
            Path("Images") : ['png','jpg','jpeg'],
            Path("Text") : ['txt','doc','pdf'],
        }
    reverse_group = {}
    for target_dir, ext_lst in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir(parents=True)
        for ext in ext_lst:     # Каждому расширению соответсвует своя папка
            reverse_group[f'.{ext}'] = target_dir
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_group:     # Если файл это файл и если расширение файла есть в словаре
            file.replace(reverse_group[file.suffix]/file.name)  # переметисть файл во вложенный каталог

if __name__ == "__main__":     
    source_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files\Task7_sort'
    #sort_files(source_directory)
    sort_files_2(Path(source_directory))