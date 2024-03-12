# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.


from pathlib import Path
from os import chdir
import json
chdir(fr'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem13_Exception')

__all__ = ['read_file']

class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level
        
    def __str__(self):
        return f'{self.name = } {self.user_id = } {self.level = }'
    
        
def read_file(user_file: Path) -> set[User]:
    with open(user_file, mode='r', encoding='utf-8') as f:
        data_json = json.load(f)  # загрузим данные из файла
    users = set()
    for dict_level, dict_value in data_json.items():
        for user_id, name in dict_value.items():
            users.add(User(name, user_id, dict_level))
    return users        
    

if __name__ == '__main__':
    out_file = r'task2_users.json'
    print(*read_file(Path(out_file)), sep='\n')