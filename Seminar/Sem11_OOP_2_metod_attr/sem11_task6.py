# Задание №6
# 📌 Доработайте прошлую задачу.
# 📌 Добавьте сравнение прямоугольников по площади
# 📌 Должны работать все шесть операций сравнения


class Rectangle:
    def __init__(self, lenght: int|float, width: int|float|None=None):
        self.lenght = lenght
        if width:               # Если есть ширина
            self.width = width
        else:
            self.width = lenght    
    
    
    def get_perimeter(self):
        self.perimeter = (self.lenght + self.width) * 2
        return self.perimeter
    
    
    def get_area(self):
        return self.lenght * self.width
    
    
    def __add__(self, other):
        perimeter = self.get_perimeter() + other.get_perimeter()
        lenght = self.lenght + other.lenght
        widht = perimeter / 2 - lenght
        return Rectangle(lenght, widht)
    
    
    def __sub__(self, other):
        if self.get_perimeter() > other.get_perimeter():  
            perimeter = self.get_perimeter() - other.get_perimeter()
            lenght = abs(self.lenght - other.lenght)
            widht = abs(perimeter / 2 - lenght)
            return Rectangle(lenght, widht)
        return None
   
    
    def __eq__(self, other):
        first = sorted((self.lenght, self.width))
        second = sorted((other.lenght, other.width))
        return first == second
    
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()
    
    
    def __le__(self, other):
        return self.get_area() <= other.get_area()
    
    
    def __str__(self):
        return f' Длина нового прямоугольника = {self.lenght}, ширина нового прямоугольника = {self.width},\n \
Периметр: {self.get_perimeter()}, Площадь: {self.get_area()}'

    
if __name__ == '__main__':
    rectangle1 = Rectangle(50, 50)
    rectangle2 = Rectangle(60, 40)
    per_add = rectangle1 + rectangle2
    per_sub = rectangle1 - rectangle2
    print(f'{rectangle1.get_perimeter() = }')
    print(f'{rectangle2.get_perimeter() = }')
    print(f'{rectangle1.get_area() = }')    
    print(f'{rectangle2.get_area() = }')    
    print(per_add)  # Выводит def __str__(self):
    print(per_sub)  # Выводит def __str__(self):
    print(f'rectangle1 == rectangle2 -> {rectangle1 == rectangle2}')
    print(f'rectangle1 != rectangle2 -> {rectangle1 != rectangle2}')
    print(f'rectangle1 > rectangle2 -> {rectangle1 > rectangle2}')
    print(f'rectangle1 < rectangle2 -> {rectangle1 < rectangle2}')
    print(f'rectangle1 >= rectangle2 -> {rectangle1 >= rectangle2}')
    print(f'rectangle1 <= rectangle2 -> {rectangle1 <= rectangle2}')