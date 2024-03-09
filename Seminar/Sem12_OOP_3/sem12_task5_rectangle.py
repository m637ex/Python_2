# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров. Добавьте возможность изменять длину 
# и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

# Задание №5
# Доработаем прямоугольник и добавим экономию памяти для хранения свойств 
# экземпляра без словаря __dict__.

class Rectangle:
    __slots__ = ('_width', '_height') # Задание №5
    
    def __init__(self, width: int|float, height: int|float|None=None):
        self._width = width
        if height:               # Если есть ширина
            self._height = height
        else:
            self._height = width    
        
    
    @property
    def width(self):    # Защищенные значения
        return self._width 
    
    
    @width.setter       # Контроль вводимых параметров
    def width(self, value):
        if value < 0:
            raise ValueError('Длина прямоугольника должна быть положительной')
        self._width = value
        
    
    @property
    def height(self):   # Защищенные значения
        return self._height    
    
    
    @height.setter      # Контроль вводимых параметров
    def height(self, value):
        if value < 0:
            raise ValueError('Ширина прямоугольника должна быть положительной')
        self._height = value
    
    
    def perimeter(self):
        self.per = (self.width + self.height) * 2
        return self.per
    
    
    def area(self):
        return self.width * self.height
    
    
    def __add__(self, other):
        width = self.width + other.width
        height = self.height + other.height
        return Rectangle(width, height)
    
    
    def __sub__(self, other):
        width = abs(self.width - other.width)
        height = abs(self.height - other.height)
        return Rectangle(width, height)


    def __eq__(self, other):
        return self.area() == other.area()
    
    
    def __lt__(self, other):
        return self.area() < other.area()
    
    
    def __le__(self, other):
        return self.area() <= other.area()
   
    
    def __str__(self):
        return f'Прямоугольник со сторонами {self.width} и {self.height}'
    
    
    def __repr__(self) -> str:
        return f'Rectangle({self.width}, {self.height})'



if __name__ == '__main__':
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)
    
    # rect1.width = -1  # Ввод ошибочной ширины

    print(f"Периметр rect1: {rect1.perimeter()}")  
    print(f"Площадь rect2: {rect2.area()}")    
    print(f"rect1 < rect2: {rect1 < rect2}")        
    print(f"rect1 == rect2: {rect1 == rect2}")   
    print(f"rect1 <= rect2: {rect1 <= rect2}")     

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}") 
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")     