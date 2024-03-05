# Задание №4
# 📌 Создайте класс Сотрудник.
# 📌 Воспользуйтесь классом человека из прошлого задания.
# 📌 У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


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
    

class Employee(Human):
    MAX_level = 7
    def __init__(self, user_id, last_name, first_name, patronymic, age):
        super().__init__(last_name, first_name, patronymic, age)    # берём методы родительского класса
        self.user_id = user_id
        self.level = sum(map(int, str(user_id))) % self.MAX_level
            
    def get_user_id(self):
        return self.user_id
    
    def get_level(self):
        return self.level
    

if __name__ == '__main__':
    worker = Employee(999999, 'Петров', 'Пётр', 'Петрович', 42)
    print(f'{worker.full_name() = }')
    print(f'{worker.get_age() = }')
    print(f'{worker._age = }')
    print(f'{worker.user_id = }')
    print(f'{worker.level = }')