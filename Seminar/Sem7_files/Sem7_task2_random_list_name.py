# Задание №2
# ✔ Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
# среди которых обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


import random
from pathlib import Path

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7

def generate_name(count: int = 10, file_name: str | Path = 'gen_name.txt') -> None:
    for _ in range(count):
        name = ''
        chr_is_vowel = random.choice([True, False])
        for _ in range(random.randint(MIN_LEN,MAX_LEN)):
            if chr_is_vowel:
                name += random.choice(VOWELS)
            else:
                name += random.choice(CONSONANTS)
            chr_is_vowel = not chr_is_vowel
        with open(f'Seminar\Sem7_files\{file_name}', mode="a", encoding='utf-8') as f:
            f.writelines(f'{name.title()}\n')
        

generate_name(10, Path('gen_name.txt'))
      