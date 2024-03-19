# '''
# !!!doctest!!!
# Атотест встроен в документацию к фукции:
#     """
#     Checks the number P for simplicity using finding the
#     remainder of the division in the range [2, P).
#     >>> is_prime(42) # запуск работы функции
#     False               # Ожидаемый рузультат
#     >>> is_prime(73)
#     True
#     """
#     import doctest
#     doctest.testmod()   
#     doctest.testmod(verbose=True)

    
# Тестирование через файл документации    
# import doctest
# doctest.testfile('prime.md', verbose=True)
# prime.md - файл с автотестами

# Запуск тестов из командной строки
# PS C:\Users\PycharmProjects> python -m doctest .\prime.py
# PS C:\Users\PycharmProjects> python -m doctest .\prime.py -v    # -v - результат тестов показать
# PS C:\Users\PycharmProjects> python -m doctest .\prime.md
# PS C:\Users\PycharmProjects> python -m doctest .\prime.md -v


# !!!Основы тестирования с unittest!!!
# файл с тестами это отдельный файл
# import unittest
# class TestCaseName(unittest.TestCase):
#     def test_method(self):
#         self.assertEqual(2 * 2, 5, msg='Видимо и в этой вселенной не работает :-(')
# if __name__ == '__main__':
#     unittest.main()


# Подготовка теста и сворачивание работ
#     def setUp(self) -> None: # метод setUp выполняется перед запуском каждого теста
#     def tearDown(self) -> None: # метод tearDown выполняется, если был выполнен setUp
#         независимо от того пройден тест или провален

# Перечень доступных утверждений assert
# В списке ниже приведены доступные в unittest утверждения и пояснения о том что
# именно они проверяют.
# ● assertEqual(a, b) - a == b
# ● assertNotEqual(a, b) - a != b
# ● assertTrue(x) - bool(x) is True
# ● assertFalse(x) - bool(x) is False
# ● assertIs(a, b) - a is b
# ● assertIsNot(a, b) - a is not b
# ● assertIsNone(x) - x is None
# ● assertIsNotNone(x) - x is not None
# ● assertIn(a, b) - a in b
# ● assertNotIn(a, b) - a not in b
# ● assertIsInstance(a, b) - isinstance(a, b)
# ● assertNotIsInstance(a, b) - not isinstance(a, b)
# ● assertRaises(exc, fun, *args, **kwds) - функция fun(*args, **kwds) поднимает
# исключение exc
# ● assertRaisesRegex(exc, r, fun, *args, **kwds) - функция fun(*args, **kwds)
# поднимает исключение exc и сообщение совпадает с регулярным
# выражением r
# ● assertWarns(warn, fun, *args, **kwds) - функция fun(*args, **kwds) поднимает
# предупреждение warn
# ● assertWarnsRegex(warn, r, fun, *args, **kwds) - функция fun(*args, **kwds)
# поднимает предупреждение warn и сообщение совпадает с регулярным
# выражением r
# ● assertLogs(logger, level) - блок with записывает логи в logger с уровнем level
# 20
# ● assertNoLogs(logger, level) - блок with не записывает логи в logger с уровнем
# level
# ● assertAlmostEqual(a, b) - round(a-b, 7) == 0
# ● assertNotAlmostEqual(a, b) - round(a-b, 7) != 0
# ● assertGreater(a, b) - a > b
# ● assertGreaterEqual(a, b) - a >= b
# ● assertLess(a, b) - a < b
# ● assertLessEqual(a, b) - a <= b
# ● assertRegex(s, r) - r.search(s)
# ● assertNotRegex(s, r) - not r.search(s)
# ● assertCountEqual(a, b) - a и b содержат одни и те же элементы в одинаковом
# количестве независимо от их порядка в коллекциях

# !!!3. Основы тестирования с pytest



# '''
# # !!!doctest!!!
# # def is_prime(p: int) -> bool:
# #     """
# #     Checks the number P for simplicity using finding the
# #     remainder of the division in the range [2, P).
# #     >>> is_prime(42)
# #     False
# #     >>> is_prime(73)
# #     True
# #     """
# #     for i in range(2, p):
# #         if p % i == 0:
# #             return False    
# #     return True
# # if __name__ == '__main__':
# #     import doctest
# #     doctest.testmod()   
# #     doctest.testmod(verbose=True)




# # !!!unittest!!!
# import unittest
# class TestCaseName(unittest.TestCase):
#     def test_method(self):
#         self.assertEqual(2 * 2, 5, msg='Видимо и в этой вселенной не работает :-(')
# if __name__ == '__main__':
#     unittest.main(verbosity=2) # verbosity=2 расширенный вывод автотеста. 1 по умолчанию


# import io
# import unittest
# from unittest.mock import patch
# from prime import is_prime
# class TestPrime(unittest.TestCase):
#     def test_is_prime(self):
#         self.assertFalse(is_prime(42))
#         self.assertTrue(is_prime(73))
#     def test_type(self):
#         self.assertRaises(TypeError, is_prime, 3.14)    
#     def test_value(self):
#         with self.assertRaises(ValueError): # Используем менеджер контекста для утверждения ошибки
#             is_prime(-100)
#             is_prime(1)

#     @patch('sys.stdout', new_callable=io.StringIO) # Мы говорим что хотим перехватить поток ввода_вывода
#     def test_warning_false(self, mock_stdout):
#         self.assertFalse(is_prime(100_000_001))
#         self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, the check may take a long time. Working...\n')

#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_warning_true(self, mock_stdout):
#         self.assertTrue(is_prime(100_000_007))
#         self.assertEqual(mock_stdout.getvalue(), 'If the number P is prime, the check may take a long time. Working...\n')
# if __name__ == '__main__':
#     unittest.main()

# # Метод setUp и tearDown
# import unittest
# class TestSample(unittest.TestCase):
#     def setUp(self) -> None:
#         with open('top_secret.txt', 'w', encoding='utf-8') as f:
#             for i in range(10):
#                 f.write(f'{i:05}\n')
#     def test_line(self):
#         with open('top_secret.txt', 'r', encoding='utf-8') as f:
#             for i, line in enumerate(f, start=1):
#                 pass
#             self.assertEqual(i, 10)
#     def test_first(self):
#         with open('top_secret.txt', 'r', encoding='utf-8') as f:
#             first = f.read(5)
#             self.assertEqual(first, '00000')
#     def tearDown(self) -> None:
#         from pathlib import Path
#         Path('top_secret.txt').unlink()

# if __name__ == '__main__':
#     unittest.main()
