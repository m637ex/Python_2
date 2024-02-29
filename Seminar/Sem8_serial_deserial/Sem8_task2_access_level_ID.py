# Задание №2
# 📌 Напишите функцию, которая в бесконечном циклезапрашивает имя, личный 
# идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавляйте новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.


from pathlib import Path
import json
__all__ = ['set_users']

level_max = 7

def set_users(user_file: Path) -> None:
    unique_id = set()
    if not user_file.is_file(): # если файл есть то открываем его
        data = {str(i):{} for i in range(1, level_max+1)} # генератор пустого словаря 
    else:
        with open(user_file, mode='r', encoding="UTF-8") as file:
            data = json.load(file)  # загрузим данные из файла
            for dict_level in data.values():
                unique_id.update(dict_level)
                print(f"{unique_id}")                
    while True:    
        name = input("Введите Name:")
        if not name:    # выход из цикла
            break
        user_id = input("Введите ID:")
        level = input("Введите Level от 1 до 7:")
        while level not in (str(i) for i in range(1, level_max+1)):
            print("некорректный ввод")            
            level = input("Введите Level от 1 до 7:")
        if user_id not in unique_id:
            data[level][user_id] = name # или  data[level].update({user_id: name})
            unique_id.add(user_id)
            with open(user_file, mode='w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4) # indent - отступ



if __name__ == '__main__':
    # work_directory = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial'
    # in_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem7_files\task3_result.txt'
    out_file = r'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem8_serial_deserial\task2_users.json'
    set_users(Path(out_file))