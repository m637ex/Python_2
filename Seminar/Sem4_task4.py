# Задание №4
# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def bubble_sort(arr: list[int]) -> list[int]: # Сортировка пузырьком
    len_arr = len(arr)
    for i in range(len_arr):
        swapped = True
        for j in range(len_arr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = False
        if swapped:
            return arr

data_list = [15,12,13,16,19,1,8,17,14,11,10,18,15,12,13]
print(bubble_sort(data_list))