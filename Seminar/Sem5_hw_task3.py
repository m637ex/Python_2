# Создайте функцию генератор чисел Фибоначчи fibonacci. 
# На входе:
# f = fibonacci()
# for i in range(10):
#     print(next(f))
# На выходе: 0 1 1 2 3 5 8 13 21 34

def fibonacci():
    num1 = 0
    num2 = 1
    while True:        
        yield num1
        num1, num2 = num2, num1 + num2

f = fibonacci()
for i in range(10):
    print(next(f))