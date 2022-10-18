money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital  >= 0:
    if salary + money_capital  >= spend:
        spend = spend * 0.05 + spend
        money_capital = money_capital + salary - spend
        month += 1
    else:
        break
print(month)
#почему в ответах 3, если это неверный ответ? верный 5 месяцев при таких условиях

