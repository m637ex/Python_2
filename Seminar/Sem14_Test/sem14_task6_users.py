# Задание №6
# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта. Используйте фикстуры.


from pathlib import Path
from os import chdir
import json
import pytest
chdir(fr'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem14_Test')

@pytest.fixture
def new_set():
    data = {
        User('Petr', 1, 1),
        User('Ivan', 2, 3),
        User('Petr', 3, 3),
        User('Alexey', 5, 5)
    }
    return data

@pytest.fixture
def new_user():
    return User('Bill', 456, 5)

@pytest.fixture
def good_user():
    return User('Ivan', 2, 3)

def test_load(new_set):
    project = Repo()
    result = project.read_file(Path(r'task6_users.json'))
    assert result == new_set

def test_enter(good_user):
    project = Repo()
    project.read_file(Path(r'task6_users.json'))
    result = project.enter_user('Ivan', 2)
    assert result == good_user

def test_no_enter():
    project = Repo()
    project.read_file(Path(r'task6_users.json'))
    with pytest.raises(UserAccessError):
        project.enter_user('TTTT', 2)

def test_add_user(new_user):
    project = Repo()
    project.read_file(Path(r'task6_users.json'))
    project.enter_user('Ivan', 2)
    result = project.add_user('Bill', 456, 5)
    assert result == new_user

def test_not_add_user(new_user):
    project = Repo()
    project.read_file(Path(r'task6_users.json'))
    project.enter_user('Ivan', 2)
    with pytest.raises(UserLevelError):
        project.add_user('Bill', 456, 1)
        
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
        print(self.users)
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
        if level < self.user.level:
            raise UserLevelError('Уровень ниже положенного')
        new_user = User(name, user_id, level)
        self.users.add(new_user)
        # with open(out_file, mode='w', encoding='utf-8') as f:
        #     json.dump(self.users, f, indent=4)
        return new_user
            

if __name__ == '__main__':
    pytest.main(['-vv'])