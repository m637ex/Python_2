# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число) Сотрудники имеют также уникальный идентификационный номер (ID), 
# который должен быть шестизначным положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст). Класс должен проверять валидность входных данных и 
# генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID). Класс Employee также должен проверять валидность ID и 
# генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.
class InvalidNameError(BaseException):
    pass


class InvalidAgeError(BaseException):
    pass


class InvalidIdError(BaseException):
    pass


class Person:
    def __init__(self, last_name, first_name, patronymic, age):
        self.last_name = self.check_name(last_name)
        self.first_name = self.check_name(first_name)
        self.patronymic = self.check_name(patronymic)
        self._age = self.check_age(age)

    def check_name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
        return name
        
    def check_age(self, age):
        if not isinstance(age, int) or age < 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        return age
                
    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age
    
    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'
    

class Employee(Person):
    MAX_level = 7
    def __init__(self, last_name, first_name, patronymic, age, user_id):
        super().__init__(last_name, first_name, patronymic, age)    # берём методы родительского класса
        self.user_id = self.check_id(user_id)
        self.level = sum(map(int, str(user_id))) % self.MAX_level
        
    def check_id(self, user_id):
        if isinstance(user_id, int) == False or user_id < 100000 or user_id > 999999:
            raise InvalidIdError(f'Invalid id: {user_id}. Id should be a 6-digit positive integer between 100000 and 999999.')
        return user_id
    
    def get_level(self):
        return self.level
    

if __name__ == '__main__':
    worker = Employee(999999, 'Петров', 'Пётр', 'Петрович', 42)
    print(f'{worker.full_name() = }')
    print(f'{worker._age = }')
    print(f'{worker.user_id = }')
    print(f'{worker.level = }')
    # worker = Employee(99999, 'Петров', 'Пётр', 'Петрович', 42)
    # worker = Employee(-10000, 'Петров', 'Пётр', 'Петрович', 42)
    # worker = Employee(9900999, 'Петров', 'Пётр', 'Петрович', 42)
    # worker = Employee(999999, '', 'Пётр', 'Петрович', 42)
    # worker = Employee(999999, 45, 'Пётр', 'Петрович', 42)
    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.get_age())