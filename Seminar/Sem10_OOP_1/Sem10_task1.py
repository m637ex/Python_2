# Задание №1
# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.


from math import pi 

class Circle:
    def __init__(self, radius): # Инициализируем принимаемые аргументы
        self.radius = radius
        
    def perimetr(self):         # готовим метод длина окружности
        return 2 * pi * self.radius
        
    def area(self):      # Готовим метож площадь круга
        return pi * self.radius ** 2
        

if __name__ == '__main__':
    circle = Circle(10)     # Передаём в класс значение
    print(f'{circle.perimetr() = }')
    print(f'{circle.area() = }')
