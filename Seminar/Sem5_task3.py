# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# sting = input('Введите строку: ')
# dict_1 = {char: ord(char) for char in sting }
# print(f'{dict_1 = }')
dict_1 = {'#': 35, ' ': 32, '✔': 10004, 'С': 1057, 'о': 1086, 'з': 1079, 'д': 1076, 'а': 1072, 'й': 1081, 'т': 1090, 'е': 1077, 'и': 1080, 'с': 1089, 'р': 1088, 'к': 1082, 'л': 1083, 'в': 1074, 'ь': 1100, ',': 44, 'г': 1075, 'ю': 1102, 'ч': 1095, '—': 8212, 'б': 1073, 'у': 1091, 'н': 1085, 'ы': 1099, '.': 46}
COUNT = 5

dict_iter = iter(dict_1.items())
for _ in range(COUNT):
    print(*next(dict_iter), sep=' : ')