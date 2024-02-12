# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def balance(finance: dict[str, list[int | float]]) -> bool:
    return all(map(lambda numbers: sum(numbers) >= 0 , finance.values()))
    
    
data = {
"Рога": [42, -73, 12, 85, -15, 2],
"Копыта": [45, 25, -100, 22, 1],
"Хвосты": [-500, 123, 52, 45, 93],
}

print(balance(data))