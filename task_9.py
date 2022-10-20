salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
list_spend = [ ]

num_months = list(range(months))
for m in num_months:
    if m == 0:
        list_spend.append(spend)
    elif m + 1 <= 10:
        spend = spend * increase + spend
        list_spend.append(spend)
spend_all = sum(list_spend)
need_money = (salary * months - spend_all) * (-1)
print(round(need_money))
