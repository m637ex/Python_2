"""Простое или составное
Напишите код, который анализирует число num и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если это число натуральное и делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. Если подается отрицательное число или число более ста тысяч, выведите на экран сообщение: "Число должно быть больше 1 и меньше 100000".
Внимание! Число 1 — не является ни простым, ни составным числом, так как у него только один делитель — 1.
Пр: На входе:   num = 2
    На выходе:  Простое
    На входе:   num = 1000001
    На выходе:  Не является простым
"""

num = int(input('Введите натуральное число от 2 до 100000: '))
if num == 1:
    print("Число 1 — не является ни простым, ни составным числом")
elif num < 1 or num > 100000:
    print('Число должно быть больше 1 и меньше 100000')
elif num == 2 or num == 3:
    print("Простое")
else:
    i = 1
    while i < num / 2 + 1:
        i += 1
        if num % i == 0:
            print("Не является простым")
            break
    else:
        print("Простое")
    