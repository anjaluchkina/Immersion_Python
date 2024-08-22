'''
Задание №5

Функция принимает на вход три списка одинаковой длины:
- имена str
- вставка int
- вставка  str с указанием процентов вида "10.25%""
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии.
'''

import decimal

'''def list_bonus(name: list[str], best: list[int], rewards: list[str])-> dict[str, decimal.Decimal]:
    result = {}
    for name, best, rewards in zip(name, best, rewards):
        result[name] = best * decimal.Decimal(rewards[:-1]) / 100
    return result


n = ['Alex', 'Anna', 'Ben']
b = [20000, 10000, 30000]
r = ['5.5%', '10.25%', '3.14%']

print(list_bonus(n, b, r))'''


# Через range

def list_bonus(name: list[str], best: list[int], rewards: list[str])\
      -> dict[str, decimal.Decimal]:
    result = {}
    for i in range(len(name)):
        result[name[i]] = best[i] * decimal.Decimal(rewards[i][:-1]) / 100
    return result

n = ['Alex', 'Anna', 'Ben']
b = [20000, 10000, 30000]
r = ['5.5%', '10.25%', '3.14%']

print(list_bonus(n, b, r))