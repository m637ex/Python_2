'''
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним, только если треугольник существует .
Пример: На входе:
a = 4
b = 4
c = 4
На выходе:
1.Треугольник существует
Треугольник равносторонний
2.Теугольник существует
Треугольник равнобедренный
3.Треугольник существует
Треугольник разносторонний
4.Треугольник не существует
'''

a = 3
b = 5
c = 6
if a + b > c and b + c > a and a + c > b:
    print("Треугольник существует")
    if a == b == c:
        print("Треугольник равносторонний")
    elif a == b or b == c or a == c:
        print("Треугольник равнобедренный")
    else:
        print("Треугольник разносторонний")
else:
    print("Треугольник не существует")