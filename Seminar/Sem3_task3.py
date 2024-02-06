
# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.


data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
result = {}
for item in data:    
    item_type = type(item)
    if item_type not in result:     # Если ключа нет
        result[item_type] = [item]  # Создаем ключ и значение по этому ключу
    else:   
        result[item_type].append(item)
print(result)


result2 = {}
for item in data:    
    item_type = type(item)
    if item_type not in result2:     # Если ключа нет
        result2[item_type] = [el for el in data if type(el) == item_type]
print(result2)


result3 = {}
for item in data:    
    key = result3.setdefault(type(item), [])
    key.append(item)
print(result3)


print(result == result2)
print(result == result3)