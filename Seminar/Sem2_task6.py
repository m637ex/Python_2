# Задание №6
# Напишите программу банкомат.
# ✔✔ Начальная сумма равна нулю
# ✔✔ Допустимые действия: пополнить, снять, выйти
# ✔✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔✔ Любое действие выводит сумму денег


MULTIPLICITY = 50   # Крастность суммы пополнения и снятия
INTEREST_ON_WITHDRAWAL = 0.015  # Процент за снятие
MIN_SUM_INTEREST_ON_WITHDRAWAL = 30 # Минимальная сумма процента за снятие
MAX_SUM_INTEREST_ON_WITHDRAWAL = 600 # Максимальная сумма процента за снятие
SUM_WEALTH = 5_000_000      # Сумма от которой платится налог на богатство
TAX_WEALTH = 0.1            # величина налога 10%
INTEREST_ON_BALANCE = 0.03  # Процент на остаток - 3%
deposit = 1000

        
def put_money(deposit):
    print(f'Будем пополнять.')
    print(f'Ваш баланс равен {deposit}у.е.')
    item_money = int(input('Внесите сумму пополнения: '))
    deposit = deposit + item_money // MULTIPLICITY * MULTIPLICITY       
    print(f'На счёт внесено {item_money // MULTIPLICITY * MULTIPLICITY}у.е.')   
    return deposit


def get_money(deposit):
    print(f'Будем снимать.')
    print(f'Ваш баланс равен {deposit}у.е.')
    desired_amount = int(input('Укажите сумму для снятия: '))
    withdrawal_amount = desired_amount // MULTIPLICITY * MULTIPLICITY   # Сумма для снятия кратная заданной кратности
    if withdrawal_amount * INTEREST_ON_WITHDRAWAL < MIN_SUM_INTEREST_ON_WITHDRAWAL:    # Вычисляем коммисию банка
        current_interest_on_withdrawal = MIN_SUM_INTEREST_ON_WITHDRAWAL
    else:
        current_interest_on_withdrawal = withdrawal_amount * INTEREST_ON_WITHDRAWAL
    if current_interest_on_withdrawal > MAX_SUM_INTEREST_ON_WITHDRAWAL:
        current_interest_on_withdrawal = MAX_SUM_INTEREST_ON_WITHDRAWAL
    if withdrawal_amount + current_interest_on_withdrawal <= deposit:
        deposit -= withdrawal_amount + current_interest_on_withdrawal
        print(f"Выдано {withdrawal_amount}y.e., Списано {withdrawal_amount + current_interest_on_withdrawal}y.e")
    else:
        print("Недостаточно денег на балансе.")
    return deposit


def put_tax(deposit):
    deposit -= deposit * TAX_WEALTH
    print(f'Списан налог на богатство: {deposit * TAX_WEALTH}y.e., Ваш баланс после операции: {deposit}')
    return deposit


def work(deposit):
    count = 0
    while True :
        if count == 3:
            deposit += deposit * INTEREST_ON_BALANCE     # начисляются проценты - 3%
            print(f'Поздравляем, вам начислены проценты на остаток: {deposit * INTEREST_ON_BALANCE}')
            count = 0           # Обнуляем счётчик
        print(f'Ваш баланс: {deposit}у.е.')
        print("п - Пополнить\nс - Снять\nв - Выйти")
        mode = input('Введите для действия: ')
        match mode:
            case "п": # Пополнить
                if deposit >= SUM_WEALTH:
                    deposit = put_tax(deposit) 
                deposit = put_money(deposit)
            case "с": # Снять
                if deposit >= SUM_WEALTH:
                    deposit = put_tax(deposit) 
                deposit = get_money(deposit)
            case "в": # Выйти
                print(f'С вами было приятно работать. Возвращайтесь')
                return
            case _: # Выйти
                print(f'Ошиблись вводом, попробуй еще')
                return
        count += 1


work(deposit)