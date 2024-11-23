from itertools import count

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 1 # начинаем с первого месяца
while spend < money_capital:
    if months == 1:
        months +=1
        money_capital += salary - spend
    else:
        months += 1
        spend *= (1 + increase) # увеличение расходов на 5%
        money_capital += salary - spend
print("Количество месяцев, которое можно протянуть без долгов:", months)


