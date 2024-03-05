# Задание №5
# 📌 Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# 📌 У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# 📌 Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.


class Fish():
    def __init__(self, name, area, weight, lenght, max_depht, color):
        self.name = name
        self.area = area
        self.weight = weight
        self.lenght = lenght
        self.max_depht = max_depht
        self.color = color
        
    def get_depths(self):
        if self.lenght < 10:
            return 'Мелководная'
        elif self.lenght > 100:            
            return 'Глубоководная'
        return 'Средневодная'


class Bird:
    def __init__(self, name, weight, wingspan, color):
        self.name = name
        self.weight = weight
        self.wingspan = wingspan
        self.color = color
        
    def get_wing_length(self):
        return self.wingspan / 2
    
    def get_color(self):
        return self.color
    

class Mammal:
    def __init__(self, name, weight, color, height):
        self.name = name
        self.weight = weight
        self.color = color
        self.height = height
        
    def get_category(self):
        if self.height < 1:
            return 'Малявка'
        elif self.height > 200:            
            return 'Гигант'
        return 'Обычный'
    

if __name__ == '__main__':
    penguin = Bird(name='Кавальский', weight=20, wingspan=60, color='black')
    clown = Fish(name='Немо', area='Hawai', weight=1, lenght=10, max_depht=5, color='orange')
    zebra = Mammal(name='Мартин', weight=150, color='white', height=120)

    print(f'Животное: {penguin.name}, длин крыла - {penguin.get_wing_length()}, цвет - {penguin.get_color()}') 
    print(f'Животное: {clown.name}, глубоководность - {clown.get_depths()}') 
    print(f'Животное: {zebra.name}, Размер - {zebra.get_category()}') 
    