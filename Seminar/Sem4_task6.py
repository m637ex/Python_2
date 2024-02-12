# Задание №6
# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

s = [73, 42, 7, 3, 5, 2, 11, 100, 500, 1, -750]

def func_sum(numbers: list[int], num1: int, num2: int) -> int:
    size = len(numbers)
    min_i, max_i = sorted([num1, num2])
    min_i = min_i if min_i > 0 else 0
    max_i = max_i if max_i < size else size
    return sum(numbers[min_i:max_i])

print(func_sum(s, 3, 8))