# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

BIN = 2
OCT = 8

def calc_translater(num: int, ss: int):
    if num < ss:
        return num
    # if not isinstance(num, int):
    #     return 'Число не целое'
    # test_num: int = num
    # res: str = ''
    # while test_num:
    #     cur_num = test_num % ss
    #     res = str(cur_num) + res
    #     test_num //= ss
    # return res
    return  str(calc_translater(num // ss, ss)) + str(num % ss)


value: int = int(input('Введите целое число:'))
print(f'Число {value} в двоичной системе будет равно - {calc_translater(value, BIN)}')
print(f'Число {value} в восьмеричной системе будет равно - {calc_translater(value, OCT)}')