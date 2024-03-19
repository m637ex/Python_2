# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
# возврат строки без изменений (without_changes)
# возврат строки с преобразованием регистра без потери символов (transformation_register)
# возврат строки с удалением знаков пунктуации (removal_punct)
# возврат строки с удалением букв других алфавитов (remov_oth_alph)
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1) (all)

import unittest
from string import ascii_letters

def clear_text(text: str) -> str:
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()
       

class TestCaseName(unittest.TestCase):
    def test_without_changes(self): # должно начинаться с "test_"
        self.assertEqual(clear_text('hello world'), 'hello world', "Don't work!!!")
    def test_transformation_register(self):
        self.assertEqual(clear_text('Hello World'), 'hello world', "Don't work!!!")
    def test_removal_punct(self):
        self.assertEqual(clear_text('Hello World!!!'), 'hello world', "Don't work!!!")
    def test_remov_oth_alph(self):
        self.assertEqual(clear_text('HelloПривет WorldМир'), 'hello world', "Don't work!!!")
    def test_all(self):
        self.assertEqual(clear_text('Hello(Привет), World(Мир)!!!'), 'hello world', "Don't work!!!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
    # text = 'STring.ascii_letters: Конкатенация ascii_lowercase и ascii_uppercase константы описаны ниже.'
    # print(clear_text(text))