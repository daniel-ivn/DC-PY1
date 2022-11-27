# импортируем модуль json
import json

# файл, из которого берём данные
INPUT_FILE = "input.csv"

# создаём функцию с названием файла, разделителями значений и строк в её аргументе, которая выдаёт список словарей
def csv_to_list_dict(file_name, delimiter=',', new_line='\n') -> list[dict]:
    # задаём пустой список
    list_ = []
    # открываем файл с помощью менеджер контекста with на чтение в текстовом виде и называем его input_file
    with open(file_name, "rt") as input_file:
        # далее считываем построчно headers и rows из файла input_file и приводим к необходимому виду
        headers = (input_file.readline().replace(new_line, "")).split(delimiter)
        for row in input_file:
            row = row.replace(new_line, "").split(delimiter)
            list_.append(dict(zip(headers, row)))
    # возвращаем заполненный список словарей
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
