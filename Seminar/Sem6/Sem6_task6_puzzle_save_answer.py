# Задание №6
# 📌 Добавьте в модуль с загадками функцию, которая принимает на вход строку 
# (текст загадки) и число (номер попытки, с которой она угадана).
# 📌 Функция формирует словарь с информацией о результатах отгадывания.
# 📌 Для хранения используйте защищённый словарь уровня модуля.
# 📌 Отдельно напишите функцию, которая выводит результаты
# угадывания из защищённого словаря в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.


_data_answerse = {}   
__all__ = ['save_data_answerse', 'print_saved_answers', 'secrets']

def save_answers(puzzle: str, count: int) -> None:
    _data_answerse.update({puzzle: count})


def print_saved_answers() -> None:
    print(*(f'Загадка "{puzzle}" отгадана с {count} попытки.\n' if count
            else f'Загадку "{puzzle}" не удалось отгадать\n'
            for puzzle, count in _data_answerse.items()))



def secrets(puzzle: str, answers:list[str], count: int=3) -> int:
    print(f'Угадай загадку:\n{puzzle}')
    for n in range(1, count+1):
        answer = input(f'Попытка {n} из {count}. Введите отгадку: ').lower()
        if answer in answers:
#            print(f'Вы угадали загадку: {puzzle} с {n} попытки')
            return n
    return 0



def storage() -> None:
    puzzles = {
        'Зимой летом, одним цветом':['ёлка','елка','сосна','ель'],
        'Не лает, ни кусает, а охраняет':['замок','засов','запор'],
        'Висит груша, нельзя скушать':['лампа','лампочка','светильник'],
    }
    for puzzle, answer in puzzles.items():
        result = secrets(puzzle=puzzle, answers=answer, count=5)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадалось угадать')
        save_answers(puzzle=puzzle, count=result)
        #print(_data_answerse)


if __name__ == '__main__':
    storage()
    print_saved_answers()
    # result = secrets(puzzle='Зимой летом, одним цветом!!!', answers=['ёлка','елка','сосна','ель'], count=5)
    # print(f'Угадал с {result} попытки' if result > 0 else 'Не угадалось угадать')