# Задание №7
# 📌 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# 📌 Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# 📌 Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# 📌 Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# 📌 Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['is_valid_date','is_leap']

data_day_in_month = {
    1:31,     2:28,    3:31,    4:30,    5:31,    6:30,    
    7:31,    8:31,    9:30,    10:31,    11:30,    12:31
}


def is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def is_valid_date(date: str) -> bool:
    if date.count('.') != 2:
        return False
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 1999:
        if 1 <= month <= 12:
            if 1 <= day <= (data_day_in_month[month] + is_leap(year)):
                return True
    return False


if __name__ == "__main__":
    date = input('Введите дату в формате DD.MM.YYYY: ')        
    print(f'Date {date} is valid' if is_valid_date(date) 
        else f'Date {date} is not valid')
    
    print("Test:\nTrue:")
    date_to_prov = '29.02.1996'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = '29.01.1996'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = '01.01.0001' 
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')   
    date_to_prov = '31.12.1999'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    print("False:")
    date_to_prov = '29.02.1995'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = '30.02.1996'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = '29.13.1996'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = '28.02.2000'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = 'test'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = '12.12'
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')
    date_to_prov = ''
    print(f'Date {date_to_prov} is valid' if is_valid_date(date_to_prov) 
      else f'Date {date_to_prov} is not valid')