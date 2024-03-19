# Обработка исключений в Archive
# Допишите в вашу задачу Archive обработку исключений.
# Добавьте исключение в ваш код InvalidTextError, которые будет вызываться, когда текст не является строкой или является пустой строкой.
# Текст ошибки: Invalid text: {введенный текст}. Text should be a non-empty string.'
# И InvalidNumberError, которое будет вызываться, если число не является положительным целым числом или числом с плавающей запятой.
# Текст ошибки: 'Invalid number: {введенное число}. Number should be a positive integer or float.'

from typing import Union
class Archive:
    """
    Класс, представляющий архив текстовых и числовых записей.

    Атрибуты:
    - archive_text (list): список архивированных текстовых записей.
    - archive_number (list): список архивированных числовых записей.
    - text (str): текущая текстовая запись для добавления в архив.
    - number (int или float): текущая числовая запись для добавления в архив.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance


    def __init__(self, text: str, number: Union[int, float]):
        if not isinstance(text, str) or len(text) == 0:
            raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        else:
            self.text = text
        if not isinstance(number, (int, float)) or number <= 0:
            raise InvalidNumberError(f'Invalid number: {number}. Number should be a positive integer or float.')
        else:
            self.number = number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'


# Введите ваше решение ниже
class InvalidTextError(BaseException):
    pass


class InvalidNumberError(BaseException):
    pass


if __name__ == '__main__':
    archive = Archive('Привет мир!!!', 107)
    archive = Archive('Сорок два', 42)
    archive = Archive("", -5)
    archive = Archive("Sample text", -5)
    print(archive)