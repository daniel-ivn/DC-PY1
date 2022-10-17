salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
month = 1                               # первый месяц жизни по схеме
monthly_increase_percentage = 1.03      # ежемесячный прирост цен в долях единицы

# денежный остаток 
required_cash_balance = spend - salary

# Цикл должен повторяться до тех пор, пока счётчик не дойдёт до 10 месяца:
while month != 11:                             # указываем условие (стоит != 11, так как считаем до 10 месяца)
    need_money += required_cash_balance        # увеличиваем подушку безопасности на денежный остаток (1 месяц)
    spend *= monthly_increase_percentage       # увеличиваем расходы на 3%
    required_cash_balance = spend - salary     # снова увеличиваем денежный остаток со второго месяца
    month += 1                                 # увеличиваем счётчик месяцев

print(round(need_money))
