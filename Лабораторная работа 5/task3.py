# TODO написать функцию для получения списка уникальных целых чисел

from random import randint      # из модуля random импортируем функцию randint


# создаём функцию, которая будет возвращать уникальный случайный целочисленный список
def get_unique_list_numbers() -> list[int]:

    start_list = -10            # по условию начало диапазона от -10 включительно
    stop_list = 10              # по условию конец диапазона до 10 включительно
    count_list = 15             # по условию размер списка 15 чисел

    # создаём целочисленный (int) список (list) из случайных (randint) и уникальных (set) чисел с учётом условия
    list_numbers = list(set([randint(start_list, stop_list) for i in range(count_list)]))
    return list_numbers         # возвращаем этот список


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
