# Задача 7а
# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


HEX: int = 16
res: str = ''
list_hex: str = '0123456789ABCDEF'


num = int(input("Введите число: "))
test_num: int = num
if num == 0:
    res = '0'
while test_num:
    current = test_num % HEX
    res = list_hex[current] + res
    test_num //= HEX

print(f'Шестнадцатеричное представление числа: {res}')
print(f'Проверка результата: {hex(num)}')