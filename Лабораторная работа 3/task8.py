def surv(money_capital, salary, spend, increase=0.05):
    month = 0
    critpoint = spend
    while money_capital > critpoint:
        money_capital = money_capital + salary - spend
        spend = spend * (1 + increase)
        month += 1
        critpoint = spend
        if month > 1200:
            print("something probably went wrong, check input numbers")
            break
    return month

money_cap = 10000
sal = 5000
sp = 6000
#month = 0

month = surv(money_cap, sal, sp)
print(month)
