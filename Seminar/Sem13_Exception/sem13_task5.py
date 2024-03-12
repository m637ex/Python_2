# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# * загрузка данных (функция из задания 4)
# * вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве 
#   используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, 
#   вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# * добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

from pathlib import Path
from os import chdir
import json
chdir(fr'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem13_Exception')


class UserException(Exception):
    pass

class UserLevelError(UserException):
    pass

class UserAccessError(UserException):
    pass

class User:
    def __init__(self, name, user_id, level):
        self.name = name
        self.user_id = user_id
        self.level = level
        
    def __str__(self):
        return f'{self.name = } {self.user_id = } {self.level = }'
    
    def __eq__(self, other) -> bool:    # магический метод проверки на равенство пользователей
        return self.name == other.name and self.user_id == other.user_id
        
    # def __lt__(self, other): # для оператора меньше <
    #     return self.level < other.level
    
    def __hash__(self):
        return hash((str(self.name), str(self.user_id)))
    
    
class Repo:
    def __init__(self):
        self.user = None
        self.users = set()       
            
            
    def read_file(self, user_file: Path) -> set[User]:
        with open(user_file, mode='r', encoding='utf-8') as f:
            data_json = json.load(f)  # загрузим данные из файла
        for dict_level, dict_value in data_json.items():
            for user_id, name in dict_value.items():
                self.users.add(User(name, int(user_id), int(dict_level)))
        return self.users


    def enter_user(self, name, user_id):
        current_user = User(name, user_id, level=0)
        if current_user not in self.users:
            raise UserAccessError('В доступе отказано')
        
        for user in self.users:
            if user == current_user:
                self.user = user
                return self.user
        
        
    def add_user(self, name, user_id, level):
        if level > self.user.level:
            raise UserLevelError('Уровень ниже положенного')
        new_user = User(name, user_id, level)
        self.users.add(new_user)
        # with open(out_file, mode='w', encoding='utf-8') as f:
        #     json.dump(self.users, f, indent=4)
        return new_user
            

if __name__ == '__main__':
    repo = Repo()
    out_file = r'task2_users.json'
    repo.read_file(Path(out_file))
    print(repo.enter_user('Андрей5', 51))
    print(repo.add_user('Shilo', 123456, 3))
    print(*repo.users, sep='\n')
    