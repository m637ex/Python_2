# Задание №1
# 📌 Создайте класс Моя Строка, где:
# 📌 будут доступны все возможности str
# 📌 дополнительно хранятся имя автора строки и время создания (time.time)
# Задание №3  📌 Добавьте к задачам 1 и 2 строки документации для классов.

class MyString(str):    # 📌 будут доступны все возможности str
    """Класс, где доступны все возможности класса str и 
    дополнительно хранятся имя автора строки и время создания (time.time) """
    def __new__(cls, name, value):
        import time
        instance = super().__new__(cls, value) # создадим класс с элементами класса str и переменной value
        instance.name = name
        instance.time = time.time()
        print(f'Создал класс {cls = }, {name = }, {instance.time = } ') # Создал класс <class '__main__.MyString'
        return instance
    
    
if __name__ == '__main__':
    mystring  = MyString('Steve', 'Hello World')