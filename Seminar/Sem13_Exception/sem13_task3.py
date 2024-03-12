# Задание №3
# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class UserException(Exception):
    pass


class UserLevelError(UserException):
    pass


class UserAccessError(UserException):
    pass


