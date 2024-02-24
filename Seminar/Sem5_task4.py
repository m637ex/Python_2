# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# Решение 1:
def even_number_generator(limit):
    for numbers in range(0, limit + 1, 2):
        if sum(int(digit) for digit in str(numbers)) != 8:
            yield numbers
            
print(list(even_number_generator(100)))

# Решение 2:
def even_number_generator1(limit):
    for numbers in range(0, limit + 1, 2):
        if numbers // 10 + numbers % 10 != 8:
            yield numbers
            
print(list(even_number_generator1(100)))

# Решение 3:
limit = 100
print(list(numbers for numbers in range(0, limit + 1, 2) if numbers // 10 + numbers % 10 != 8))