# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.


class Range:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name # меняем имя
    
    def __get__ (self, instance, owner): # возвращаем в верхний класс значение с новым именем
        return getattr(instance, self.param_name) # Возвращаем экземпляр функции
        
        
    def __set__ (self, instance, value):    
        self.validate(value)    # вызываем валидатор
        setattr(instance, self.param_name, value)  # собираем параметры воедино
        
    def validate(self, value):  # проверка
        if not isinstance(value, (int, float)):
            raise TypeError('Длина должна быть числом')
        if value <= 0:
            raise ValueError('Длина должна быть больше 0')
        if value > 100:
            raise ValueError('Длина должна быть не более 100')
        

class Rectangle:
    width = Range()
    height = Range()
    
    def __init__(self, width: int|float, height: int|float|None=None):
        self.width = width
        if height:               # Если есть ширина
            self.height = height
        else:
            self.height = width    
     
    
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

    print(f"{rect1}")
    print(f"Периметр rect1: {rect1.perimeter()}")  
    print(f"Площадь rect2: {rect2.area()}")    
    print(f"rect1 < rect2: {rect1 < rect2}")        
    print(f"rect1 == rect2: {rect1 == rect2}")   
    print(f"rect1 <= rect2: {rect1 <= rect2}")     

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}") 
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")     