def get_count_char(str_):             # принимаем строку (текст) str_
    dict_symbols = {}                 # создаём пустой словарь
    DEFAULT_COUNT = 0                 # задаём счётчик для значения

    for symbols in str_.lower():      # для символов в строке нижнего регистра
        if symbols.isalpha():         # задаём условие, если символ буква, то считаем его
            dict_symbols[symbols] = dict_symbols.get(symbols, DEFAULT_COUNT) + 1
    return dict_symbols               # выводим получившийся словарь ключ(буква)-значение(количество)


def dict_symbols(dict_):              # принимаем словарь dict_
    dict_symbols_percent = {}         # создаём пустой словарь

    for key, value in dict_.items():  # для ключей в словаре dict_ вычисляем процентное отношение их элементов ко всем символам
        dict_symbols_percent[key] = str(round(value / sum(dict_.values()) * 100, 1))
    return dict_symbols_percent       # выводим получившийся словарь ключ(буква)-значение(процентное отношение)


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))                 # выводим результат первой функции
print(dict_symbols(get_count_char(main_str)))   # выводим результат второй функции
