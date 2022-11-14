# TODO решить с помощью list comprehension и распечатать его

from pprint import pprint   # импортируем из модуля pprint функцию pprint

# пишем list comprehension, где сначала наш словарь, затем условие на него,
# что в списке словари должны быть для чисел от 0 до 15 включительно (range(16))
dictionary = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]
# красиво печатаем наш список словарей с помощью функции pprint модуля pprint
pprint(dictionary)
