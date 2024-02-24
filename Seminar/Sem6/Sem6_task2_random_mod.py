from random import randint as rnd


def comparison(lower_limit: int=0, upper_limit: int=100, count: int=10) -> bool:
    num_rand = rnd(lower_limit, upper_limit)
    for _ in range(count):
        num_user = int(input(f'Введите число от {lower_limit} до {upper_limit}: '))
        if num_user == num_rand:
            return True
        elif num_user < num_rand:
            print(f'Загаданное число больше')
        elif num_user > num_rand:
            print(f'Загаданное число меньше')
    else:
        return False
    
if __name__ == '__main__':  # Запуск программы проверки из данного 
    print(comparison())