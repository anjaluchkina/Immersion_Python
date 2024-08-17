'''
Задача №6

Напишите программу банкомат.

Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е
Процент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е
После каждой третьей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богаство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег
'''

import decimal

#decimal.getcontext().prec = 2

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = decimal.Decimal(50)
MAX_REMOVAL = decimal.Decimal(600)
MIN_REMOVAL = decimal.Decimal(30)
COUNT_OPEN = decimal.Decimal(3)


account = decimal.Decimal(0)
count = 0

while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}"')
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой {account} y.e')
        break

    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержание налога на богатство {RICHNESS_TAX}% in size {percent} y.e \n'
                f'Общая сумма, оставшаяся на карте {account} y.e')
        
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, равную {MULTIPLICITY}: '))

    if command == CMD_DEPOSIT:
        account += amount
        count += 1
        print(f'Пополнение средств на карту {amount},\n'
                f'Общая сумма, оставшаяся на карте {account} y.e')
        
    elif command == CMD_WITHDRAW:
        withdraw_tax = amount * WITHDRAW_PERCENT
        withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL 
                        else MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
        if account >= amount + withdraw_tax:
            count += 1
            account -= (amount + withdraw_tax)
            print(f'Снятие с карты {amount} y.e\n'
                  f'комиссия за снятие {withdraw_tax} y.e\n'
                  f'На карте всё ещё есть деньги {account} y.e')
        else:
            print(f'Недостаточное средств на карте\n'
                   f'Запрашиваемая сумма {amount + withdraw_tax} y.e, комиссия была {withdraw_tax}%\n'
                   f'Баланс карты {account} y.e')
            
    if count and count % COUNT_OPEN == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счет начислено {ADD_PERCENT}% составляющие {bonus_percent} y.e\n'
              f'Итог на карте {account} y.e')