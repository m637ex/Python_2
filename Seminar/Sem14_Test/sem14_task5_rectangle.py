# Задание №5
# На семинарах по ООП был создан класс прямоугольник хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.

import unittest
class TestCaseName(unittest.TestCase):   
    def setUp(self) -> None:
        self.rect1 = Rectangle(5, 10)
        self.rect2 = Rectangle(3, 7)
        self.rect3 = Rectangle(2, 5)
        self.rect4 = Rectangle(10)   
    def test_craete(self): # Тест создания
        self.assertEqual(Rectangle(5, 10), self.rect1)
    def test_perimeter(self): # должно начинаться с "test_"
        self.assertEqual(self.rect1.perimeter(), 30)
        self.assertEqual(self.rect2.perimeter(), 20)
    def test_area(self):
        self.assertEqual(self.rect1.area(), 50)
        self.assertEqual(self.rect2.area(), 21)
    def test_less(self):
        self.assertLess(self.rect1, self.rect2)
    def test_equal(self):
        self.assertEqual(self.rect1, self.rect2)
    def test_less_equal(self):
        self.assertLessEqual(self.rect1, self.rect2)
    def test_greater(self):
        self.assertGreater(self.rect1, self.rect2)
    def test_greater_equal(self):
        self.assertGreaterEqual(self.rect1, self.rect2)
    def test_sum(self):
        rect3 = self.rect1 + self.rect2
        self.assertEqual(rect3.perimeter(), 50)
    def test_sub(self): # Вычитание
        rect3 = self.rect1 - self.rect2
        self.assertEqual(rect3.perimeter(), 10)

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
        return (self.width + self.height) * 2
    
    
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
    unittest.main(verbosity=2)
    