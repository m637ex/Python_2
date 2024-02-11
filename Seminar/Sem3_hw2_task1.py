# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Предметы не должны дублироваться.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.
# Пример
# На входе:

items = {
    "спальник": 1.5,
    "палатка": 3.2,
    "термос": 0.6,
    "карта": 0.1,
    "фонарик": 0.3,
    "котелок": 0.8,
    "еда": 2.5,
    "одежда": 1.7,
    "обувь": 1.2,
    "нож": 0.2
}
max_weight = 1.0
# На выходе, например, один из допустимых вариантов может быть таким:
# {'ключи': 0.3, 'кошелек': 0.2, 'зажигалка': 0.1}
backpack = {}
backpack_weight = 0.0

while items:                   # гоним цикл по ка в items есть вещи
    max_one_weight = 0
    for thing in items:         # находим максимальный вес 
        if items[thing] > max_one_weight:
            max_one_weight = items[thing]
            max_name = thing
            print(f'На входе {max_name} = {items[thing]}')
    print(f'Добавляемая вещь весит {max_one_weight} Допустимый вес в рюкзаке = {max_weight - backpack_weight}')
    if max_one_weight <= round(max_weight - backpack_weight, 1):    #tck d рюкзаке ест ьместо для этой вещи добавляем в него её
        backpack[max_name] = max_one_weight
        backpack_weight += max_one_weight
        print(f'Добавили в backpack {max_name} = {max_one_weight}, вес рюкзака {backpack_weight}')
    items.pop(max_name, '')    # удаляем проработанную вещь 
    print(f'Удалили из items {max_name}')
    
print(items)
print(backpack) 
print(backpack_weight)  
