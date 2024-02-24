# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для
# случайной расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и
# выведите 4 успешных расстановки.

import random

all_generate_queens = []
result = []

    
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


def generate_board():
    # Генерируем случайную доску
    while True:
        queens = []
        while len(queens) < 9:
            queen = (random.randint(1, 8), random.randint(1, 8))
            if queen not in queens:
                queens.append(queen)
        if queens not in all_generate_queens:       
            all_generate_queens.append(queens)            
            return queens            
        # else:
        #     print(f"{queens} is Dublicate")
    
    
def generate_boards():
    # Генерируем доски, пока не получим 4 успешные расстановки
    count = 1
    while count < 4:
        queens = generate_board()
        if check_queens(queens):
            print(f"{queens} is Success")
            result.append(queens)
            count += 1


# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)]
# print(check_queens(queens))

generate_boards()
print(f"{all_generate_queens = }", sep="\n")
print(f"{result = }", sep="\n")






























# def generate_board():
#     # Генерируем случайную доску
#     board = []

#     for i in range(1, 8+1):
#         queen = (i, random.randint(1, 8))
#         board.append(queen)
#     return board

# def is_attacking(q1, q2):
#     # Проверяем, бьют ли ферзи друг друга
#     return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

# def check_queens(queens):
#     # Проверяем все возможные пары ферзей
#     for q1, q2 in combinations(queens, 2):
#         if is_attacking(q1, q2):
#             return False
#     return True

# def generate_boards():
#     # Генерируем доски, пока не получим 4 успешные расстановки
#     count = 0
#     board_list = []
#     while count < 4:
#         board = generate_board()
#         if check_queens(board):
#             count += 1
#             board_list.append(board)
#     return board_list


# queens = [(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)] f

# queens = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)] f

# queens = [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)] f

# queens = [] t

# queens = [(4, 4)]

# queens = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)] f