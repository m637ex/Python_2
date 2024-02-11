# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию

def fix_unicode(text: str) -> list[int]:
    current_text = set(text)
    print(current_text)
    code_list = []
    for char in current_text:
        code_list.append(ord(char))
    return sorted(code_list, reverse=True)


text: str = input("Введите текст: ") # Вводим текст
print(fix_unicode(text))