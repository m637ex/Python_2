# Задание №2
# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, lenght: int|float, width: int|float|None=None):
        self.lenght = lenght
        if width:               # Если есть ширина
            self.width = width
        else:
            self.width = lenght
    
    
    def get_perimetr(self):
        return (self.lenght + self.width) * 2
    
    def get_area(self):
        return self.lenght * self.width
    
if __name__ == '__main__':
    rectangle = Rectangle(10, 20)
    print(f'{rectangle.get_perimetr() = }')
    print(f'{rectangle.get_area() = }')
    
    rectangle = Rectangle(10)
    print(f'{rectangle.get_perimetr() = }')
    print(f'{rectangle.get_area() = }')