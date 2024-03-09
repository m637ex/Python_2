# Задание №1
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.


from collections import deque   # Очередь 

class Factorial:
    def __init__(self, k):
        self.memory = deque(maxlen=k) # двухсторонняя очередь
    
    def __call__(self, n, *args, **kwargs):
        res = 1
        for num in range(2, n+1):
            res *= num
        self.memory.append({n: res})
        return self.memory[-1]
    
    def old(self):
        return self.memory
    

f = Factorial(10) # длина очереди
for i in range(2, 20):
    print(f(i))     # обращение к  функции в классе
print(f'{f.old() = }') # Печать очереди