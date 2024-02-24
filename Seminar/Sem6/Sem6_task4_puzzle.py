# Задание №4
# 📌 Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была
# отгадана загадка или ноль, если попытки исчерпаны.


def secrets(puzzle: str, answers:list[str], count: int=3) -> int:
    print(f'Угадай загадку:\n{puzzle}')
    for n in range(1, count+1):
        answer = input(f'Попытка {n} из {count}. Введите отгадку: ').lower()
        if answer in answers:
#            print(f'Вы угадали загадку: {puzzle} с {n} попытки')
            return n
    return 0

if __name__ == '__main__':
    result = secrets(puzzle='Зимой летом, одним цветом', answers=['ёлка','елка','сосна','ель'], count=5)
    print(f'Угадал с {result} попытки' if result > 0 else 'Не угадалось угадать')