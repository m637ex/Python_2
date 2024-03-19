# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)


from string import ascii_letters

def clear_text(text: str) -> str:
    '''
    >>> clear_text('hello world')
    'hello world'
    >>> clear_text('Hello World')
    'hello world'
    >>> clear_text('hello world!!!')
    'hello world'
    >>> clear_text('helloПривет worldМир')
    'hello world'
    >>> clear_text('Hello(Привет), World(Мир)!!!')
    'hello world'
    '''
    
    return ''.join(char for char in text if char in ascii_letters + ' ').lower()


if __name__ == '__main__':
    help(clear_text)
    import doctest  # импортирыем библиотеку тестов
    doctest.testmod(verbose=True) # Вызываем тест с verbose=True - расширенный вывод
    # text = 'STring.ascii_letters: Конкатенация ascii_lowercase и ascii_uppercase константы описаны ниже.'
    # print(clear_text(text))