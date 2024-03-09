# Задание №2
# 📌 Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# 📌 При нового экземпляра класса, старые данные из ранее созданных экземпляров 
# сохраняются в пару списков-архивов
# 📌 list-архивы также являются свойствами экземпляра
# Задание №3: Добавьте к задаче строки документации для классов.
# Задание №4: Добавьте методы представления экземпляра для программиста и для пользователя.


class Archive:
    """Класс, который хранит свойства: число и строка.
    При нового экземпляра класса, старые данные из ранее созданных экземпляров 
    сохраняются в пару списков-архивов list-архивы также являются свойствами экземпляра"""
    
    _instance = None  # Статическая переменная для хранения единственного экземпляра класса
    
    def __init__(self, number, text):
        self.number = number  # Свойство для хранения числа
        self.text = text  # Свойство для хранения строки


    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # Создание нового экземпляра класса
            cls._instance.list_num = []  # Инициализация списка для чисел
            cls._instance.list_text = []  # Инициализация списка для строк
        else:
            # Если экземпляр уже существует, сохраняем данные в списки архивов
            cls._instance.list_num.append(cls._instance.number)
            cls._instance.list_text.append(cls._instance.text)
        return cls._instance
    
    def __str__(self):
        return f'Number: {self.number}, Text: {self.text}, List: {self.list_num}, List: {self.list_text}'
    
    def __perl__(self):
        return f'Archive({self.number}, "{self.text}")' # образец опредеелния класса - Archive(1, "First")
        

if __name__ == '__main__':
    # Пример использования класса Archive
    archive1 = Archive(1, "First")
    archive2 = Archive(2, "Second")
    archive3 = Archive(3, "Third")

    # Вывод данных для каждого архива
    print(archive1)
    print(archive2)
    print(archive3)
    print(archive1 is archive2)
    print(archive1 is archive3)
    print(archive1.__perl__()) # вызов представления для разработчика
