money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

# TODO Оформить решение
month = 0                               # количество месяцев, которое можно прожить
monthly_increase_percentage = 1.05      # ежемесячный прирост цен в долях единицы

# денежный остаток без учёта подушки безопасности
cash_balance = salary - spend

# Цикл должен повторяться до тех пор, пока не закончатся все накопления:
while money_capital + cash_balance >= spend:   # указываем условие
    money_capital += cash_balance              # увеличиваем подушку безопасности на денежный остаток
    spend *= monthly_increase_percentage       # увеличиваем расходы на 5%
    month += 1                                 # увеличиваем счётчик месяцев

print(month)
