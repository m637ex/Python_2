# Задание №5
# 📌 Добавьте в модуль с загадками функцию, которая хранит
# словарь списков.
# 📌 Ключ словаря - загадка, значение - список с отгадками.
# 📌 Функция в цикле вызывает загадывающую функцию, чтобы
# передать ей все свои загадки.


def secrets(puzzle: str, answers:list[str], count: int=3) -> int:
    print(f'Угадай загадку:\n{puzzle}')
    for n in range(1, count+1):
        answer = input(f'Попытка {n} из {count}. Введите отгадку: ').lower()
        if answer in answers:
#            print(f'Вы угадали загадку: {puzzle} с {n} попытки')
            return n
    return 0



def storage():
    puzzles = {
        'Зимой летом, одним цветом':['ёлка','елка','сосна','ель'],
        'Не лает, ни кусает, а  охраняет':['замок','засов','запор'],
        'Висит груша, нельзя скушать':['лампа','лампочка','светильник'],
    }
    for puzzle, answer in puzzles.items():
        result = secrets(puzzle=puzzle, answers=answer, count=5)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадалось угадать')
        

if __name__ == '__main__':
    storage()
    # result = secrets(puzzle='Зимой летом, одним цветом!!!', answers=['ёлка','елка','сосна','ель'], count=5)
    # print(f'Угадал с {result} попытки' if result > 0 else 'Не угадалось угадать')