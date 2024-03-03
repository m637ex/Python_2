# Пакет для работы с файлами 3
# Из созданных на уроке и в рамках домашнего задания функций, соберите пакет для работы с файлами.
# Создайте файл __init__.py и запишите в него все функции:
# save_to_json,
# find_roots,
# generate_csv_file.

text = '''
def save_to_json():
    return True
def find_roots():
    return True
def generate_csv_file():
    return True
'''

with open("__init__.py", mode="w", encoding="UTF-8") as file:
    file.write(text)