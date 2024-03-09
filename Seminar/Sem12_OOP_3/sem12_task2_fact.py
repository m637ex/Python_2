# Задание №2 Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.

from collections import deque   # Очередь 
import time
import json
from os import chdir

chdir(fr'G:\YandexDisk\GB\Python\Python_2\Seminar\Sem12_OOP_3')

class Factorial:
    def __init__(self, k):
        self.memory = deque(maxlen=k) # двухсторонняя очередь
        # self.memory.append(k)
        # print(self.memory)
    
    def __call__(self, n, *args, **kwargs):
        res = 1
        for num in range(2, n+1):
            res *= num
        self.memory.append({n: res})
        return self.memory[-1]
    
    def old(self):
        return self.memory
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        dump_dict = {} 
        while self.memory:
            dump_dict.update(self.memory.popleft())
        with open(f'{int(time.time())}_fact.json', 'w', encoding="UTF-8") as file:
            json.dump(dump_dict, file)
        return
    

    

fact = Factorial(10) # длина очереди
for i in range(2, 20):
        print(fact(i)) 
        print(fact.old())     # обращение к  функции в классе
        
with fact as fd:
    fd(5)