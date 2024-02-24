# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».


# Решение 1
def isprime(num):
    prime_number = 2
    count = 1
    yield prime_number
    prime_number += 1
    while count < num:
        for div in range(3, prime_number, 2):
            if prime_number % div == 0:
                break
        else:
            count += 1
            yield prime_number
        prime_number += 2
        
        
# Решение 2
def isprime_2(num):
    prime_number = 2
    yield prime_number
    prime_number = 3
    count = 2
    yield prime_number
    while count < num:
        prime_number += 2
        for div in range(3, int(prime_number**0.5)+1, 2):
            if prime_number % div == 0:
                break
        else:
            count += 1
            yield prime_number
            

print(*isprime(20))
for num in isprime_2(20):
    print(num, end=', ' )