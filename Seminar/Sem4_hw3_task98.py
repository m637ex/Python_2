# Напишите функцию key_params, принимающую на вход только ключевые параметры и 
# возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример использования.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе: {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}


def key_params(**kwargs):   # принимаем ключевые параметры в словарь kwargs
    result = {}
    for key, value in kwargs.items():   # Прогоняем все ключи и значения в словаре kwargs
        if value is None:
            result[value] = key
        elif isinstance(value, (int, str, float, bool, tuple)): # Если ключ хешируем, используем строковое представ
            result[value] = key
        else:   # Если ключ не хешируем, используем строковое представление
            result[str(value)] = key
    return result


        
    
    


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)