# Задание №8
# ✔✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔✔ Какие вещи взяли все три друга
# ✔✔ Какие вещи уникальны, есть только у одного друга
# ✔✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.


hike = {
'Aaz': ("спички", "спальник", "дрова", "топор"),
'Skeeve': ("спальник", "спички", "вода", "еда"),
'Tananda': ("вода", "спички", "косметичка"),
}
print(hike.values())


# ✔✔ Какие вещи взяли все три друга
all_things = []
for values in hike.values():
    for sub_values in values:
        all_things.append(sub_values)
print(f'Все вещи друзей: {all_things}')


# ✔✔ Какие вещи уникальны, есть только у одного друга
unique_things = list(set(all_things))   # Создадим список для вывода всех уникальных вещей 
print(f'Уникальные вещи друзей: {unique_things}')


# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
without_things = []
for values in unique_things:
    if all_things.count(values) == (len(hike) - 1):
        for item in hike:
            if values not in hike[item]:
                without_things.append([values, item])
print(f'Без одной вещи: {without_things}')


# ✔✔ Какие вещи уникальны, есть только у одного друга. Метод педагога.
unique = {}
for main_friend, main_thing in hike.items():
    for slave_friend, slave_thing in hike.items():
        if main_friend != slave_friend:
            if main_friend not in unique:
                unique[main_friend] = set(main_thing) - set(slave_thing)
            else:
                unique[main_friend] -= set(slave_thing)
print(f'Уникальные вещи друзей: {unique}')
