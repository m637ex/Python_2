# Задание №5
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.


LIMIT_LOW = 1
LIMIT_UP = 101
DIV1 = 3
DIV2 = 5

for num in range(LIMIT_LOW, LIMIT_UP):
    result = ''
    if num % (DIV1*DIV2) == 0:
        print('FizzBuzz')
    elif num % DIV1 == 0:
        print('Fizz')
    elif num % DIV2 == 0:
        print('Buzz')
    else:
        print(num)
        
# Решение генератором
print(*(
    'FizzBuzz' if num % (DIV1*DIV2) == 0 
    else 'Fizz' if num % DIV1 == 0 
    else 'Buzz' if num % DIV2 == 0 
    else num 
    for num in range(LIMIT_LOW, LIMIT_UP)
), sep='\n')   

    
        