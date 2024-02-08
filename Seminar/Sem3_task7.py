# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


text = input("Введите текст: ") # Вводим текст 
print(text)

# Решение 1
dict_result = {}
for letter in text:                 # цикл по каждому символу
    if dict_result.get(letter):    # проверка наличия символа в словаре
        dict_result[letter] += 1    # вставляем счётчик
    else:
        dict_result[letter] = 1     # если символа нет в словаре, то вставляем 1
print(dict_result)                  # Вывести словарь с счётчиком        


# Решение 2
dict_result2 = {}
for letter in set(text):                 # цикл по каждому уникальному символу
    dict_result2[letter] = text.count(letter)    # вставляем счётчик
print(dict_result2)                   # Вывести словарь


#Решение 3
dict_result3 = {}
for letter in text:                 # цикл по каждому символу
    dict_result3[letter] = dict_result3.get(letter, 0) + 1    # вставляем счётч
print(dict_result3)  

print('Словари идентичны' if dict_result == dict_result2 == dict_result3 else 'Словари отличаются') # Вывести результат сравнения