# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам
# дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


def is_attacking(q1, q2) -> bool:
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])


def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1 in queens[:-1]:
        for q2 in queens[1:]:
            if q1 >= q2:
                continue
            if is_attacking(q1, q2):
                return False


queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
print(check_queens(queens))
queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]
print(check_queens(queens))
queens = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)]
print(check_queens(queens))
queens = []
print(check_queens(queens))
queens = [(4, 4)]
print(check_queens(queens))
queens = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
print(check_queens(queens))





















# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True


# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] f

# queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)] f

# queens = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)] f

# queens = [] t

# queens = [(4, 4)]

# queens = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)] f