list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_value_index = 0                                 # выбираем первый индекс списка как максимальный
for current_element in range(len(list_numbers)):    # начинаем перебирать каждый элемент в списке
    max_element = list_numbers[max_value_index]     # указываем максимальный элемент в списке
    current_value = list_numbers[current_element]   # указываем текущее значение
    if current_value > max_element:                 # если текущий элемент больше того, который встречали ранее
        max_value_index = current_element           # то перезаписываем индекс максимального числа новым значением

# переставляем элементы с помощью множественного присваивания
list_numbers[-1], list_numbers[max_value_index] = list_numbers[max_value_index], list_numbers[-1]

print(list_numbers)
