# Задание №6
# 📌 Доработайте задачу 5.
# 📌 Вынесите общие свойства и методы классов в класс Животное.
# 📌 Остальные классы наследуйте от него.
# 📌 Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, weight, color):
        self.name = name
        self.weight = weight
        self.color = color
        

class Fish(Animal):
    def __init__(self, name, area, weight, lenght, max_depht, color):
        super().__init__(name, weight, color)
        self.area = area
        self.lenght = lenght
        self.max_depht = max_depht
        
    def get_depths(self):
        if self.lenght < 10:
            return 'Мелководная'
        elif self.lenght > 100:            
            return 'Глубоководная'
        return 'Средневодная'


class Bird(Animal):
    def __init__(self, name, weight, wingspan, color):
        super().__init__(name, weight, color)
        self.wingspan = wingspan
        
    def get_wing_length(self):
        return self.wingspan / 2
    
    def get_color(self):
        return self.color
    

class Mammal(Animal):
    def __init__(self, name, weight, color, height):
        super().__init__(name, weight, color)
        self.height = height
        
    def get_category(self):
        if self.height < 10:
            return 'Карликовый'
        elif self.height > 200:            
            return 'Гигантский'
        return 'Среднерослый'
    

if __name__ == '__main__':
    penguin = Bird(name='Кавальский', weight=20, wingspan=60, color='black')
    clown = Fish(name='Немо', area='Hawai', weight=1, lenght=10, max_depht=5, color='orange')
    zebra = Mammal(name='Мартин', weight=150, color='white', height=120)

    print(f'Животное: {penguin.name}, длин крыла - {penguin.get_wing_length()}, цвет - {penguin.get_color()}') 
    print(f'Животное: {clown.name}, глубоководность - {clown.get_depths()}') 
    print(f'Животное: {zebra.name}, Размер - {zebra.get_category()}') 