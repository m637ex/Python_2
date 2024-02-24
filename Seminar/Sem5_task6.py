# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

LOW_LIMIT = 2
UP_LIMIT = 10
COLUMN = 4

tables = (
    f'{num_1:>2} X {num_2:>2} = {(num_1 * num_2):^2}\t' if num_1 != row + COLUMN - 1 else
    f'{num_1:>2} X {num_2:>2} = {(num_1 * num_2):^2}\n' if num_2 != UP_LIMIT else
    f'{num_1:>2} X {num_2:>2} = {(num_1 * num_2):^2}\n\n' 
    for row in (LOW_LIMIT, LOW_LIMIT + COLUMN)
    for num_2 in range(LOW_LIMIT, UP_LIMIT + 1)
    for num_1 in range(row, row + COLUMN)
)
print(*tables)