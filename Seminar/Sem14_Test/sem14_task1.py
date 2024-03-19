# Задание №1
# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.

from string import ascii_letters

def clear_text(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()
       

if __name__ == '__main__':
    print(clear_text('STring.ascii_letters: Конкатенация ascii_lowercase и ascii_uppercase константы описаны ниже.'))