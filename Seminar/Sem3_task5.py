# Задание №5
# Погружение в Python | Коллекции
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы

# Решенеие 1
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
print(data)        
list1 = [item for index, item in enumerate(data, 1) if index % 2 == 0]  # enumeration data list
print(list1)

# Решенеие 2
data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
unique_list =[]
print(data)        
for index, item in enumerate(data, 1):
    if index % 2 == 0:  # enumeration data list
        unique_list.append(item)
print(unique_list)