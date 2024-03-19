# Задание №4
# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

# pip install pytest
# pytest .\sem14_task4_pytest.py -v    из консоли
import pytest
from string import ascii_letters

def clear_text(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()
    
def test_original(): # должно начинаться с "test_"
    assert clear_text('hello world') == 'hello world', "Don't work!!!" # a == b, сообщение при False
def test_lower():
    assert clear_text('Hello World') == 'hello world', "Don't work!!!"
def test_punctuation():
    assert clear_text('Hello World!!!') == 'hello world', "Don't work!!!"
def test_lang():
    assert clear_text('HelloПривет WorldМир') == 'hello world', "Don't work!!!"
def test_all():
    assert clear_text('Hello(Привет), World(Мир)!!!') == 'hello world', "Don't work test_all!!!"


if __name__ == '__main__':
    pytest.main(['-vv']) # ['-vv'] - увидеть результат
    print(clear_text('Hello(Привет), World(Мир)!!!')) # -> hello world