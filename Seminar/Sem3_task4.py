# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

COUNT = 2

data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
print(data)        
for i in data:
    if data.count(i) == COUNT:
        data.remove(i)
        data.remove(i)
print(data)        

# Решенеие 2
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
print(data)        
unique_list = [item for item in data if data.count(item) != COUNT]
print(unique_list)   