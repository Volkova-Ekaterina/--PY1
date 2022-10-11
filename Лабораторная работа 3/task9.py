def money(months, salary, spend, increase=0.03):
    need_money = 0
    for i in range(months):
        need_money = need_money + spend - salary
        spend = spend * (1 + increase)
    return need_money


salar = 5000  # зарплата
spen = 6000  # траты
month = 10  # количество месяцев
increas = 0.03  # рост цен

print(round(money(month, salar, spen)))
