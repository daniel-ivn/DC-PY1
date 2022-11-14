# TODO написать функцию генерации случайных паролей

from random import sample           # из модуля random импортируем функцию sample
# из модуля string используем буквы верхнего регистра, нижнего регистра и цифры
from string import ascii_lowercase, ascii_uppercase, digits


# создаём функцию, которая будет возвращать случайную последовательность символов заданной длины n
def get_random_password(n: int = 8) -> str:    # по умолчанию количество символов равно 8
    # список всевозможных разрешённых по условию символов (valid_characters)
    valid_characters = ascii_uppercase + ascii_lowercase + digits
    # случайная сгенерированная выборка (password) из valid_characters с помощью функции sample из модуля random
    password = sample(valid_characters, n)
    return "".join(password)        # возвращаем готовый случайный пароль из n символов


print(get_random_password())        # печатаем пароль из функции get_random_password()
