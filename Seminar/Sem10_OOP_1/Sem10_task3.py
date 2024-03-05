# Задание №3
# 📌 Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# 📌 У класса должны быть методы birthday для увеличения возраста на год, full_name
# для вывода полного ФИО и т.п. на ваш выбор.
# 📌 Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Human:
    def __init__(self, last_name, first_name, patronymic, age):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self._age = age
        
    def get_age(self):
        return self._age
    
    def birthday(self):
        self._age += 1
    
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
    

if __name__ == '__main__':
    human = Human('Фамилия', 'Имя', 'Отчество', 42)
    print(f'{human.full_name() = }')
    print(f'{human.get_age() = }')
    human.birthday
    print(f'{human._age = }')
    human._age = 32
    print(f'{human._age = }')