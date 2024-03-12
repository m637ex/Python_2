# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.


def my_get(my_dict: dict, key, default=None):
    try:
        return my_dict[key]
    except KeyError:
        return default
    
    
if __name__ == '__main__':
    print(my_get({'a': 1, 'b': 2}, 'a'))
    print(my_get({'a': 1, 'b': 2}, 'c'))
    print(my_get({'a': 1, 'b': 2}, 'a', 100))
    print(my_get({'a': 1, 'b': 2}, 'b', 1000))
    print(my_get({'a': 1, 'b': 2}, 'c', 10000))
