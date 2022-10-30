def delete(list_, index=None):                      # принимаем список (list_) и индекс (index)
    if index is None:                               # если index is None, то
        return list_[:-1]                           # по умолчанию удаляем последний элемент
    else:                                           # иначе,
        return list_[:index] + list_[index + 1:]    # удаляем элемент, находящийся на index


print(delete([0, 0, 1, 2], index=0))  # [0, 1, 2]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2, 3]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3, 4]
