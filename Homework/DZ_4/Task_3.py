'''
Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''

import decimal

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
transaction_history = []

def check_richness_tax():  # проверка и удержание налога на богатство.
    global account
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержание налога на богатство {RICHNESS_TAX}% in size {percent} y.e \n'
              f'Общая сумма, оставшаяся на карте {account} y.e')

def deposit(amount): # пополнение счета
    global account, count
    account += amount
    count += 1
    print(f'Пополнение средств на карту {amount},\n'
          f'Общая сумма, оставшаяся на карте {account} y.e')
    transaction_history.append(('deposit', amount))

def withdraw(amount): # снятие средств со счета
    global account, count
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = (MIN_REMOVAL if withdraw_tax < MIN_REMOVAL 
                    else MAX_REMOVAL if withdraw_tax > MAX_REMOVAL else withdraw_tax)
    if account >= amount + withdraw_tax:
        count += 1
        account -= (amount + withdraw_tax)
        print(f'Снятие с карты {amount} y.e\n'
              f'комиссия за снятие {withdraw_tax} y.e\n'
              f'На карте всё ещё есть деньги {account} y.e')
        transaction_history.append(('withdraw', amount, withdraw_tax))
    else:
        print(f'Недостаточное средств на карте\n'
              f'Запрашиваемая сумма {amount + withdraw_tax} y.e, комиссия была {withdraw_tax}%\n'
              f'Баланс карты {account} y.e')

def add_bonus(): # начисление бонусного процента
    global account, count
    if count and count % COUNT_OPEN == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'На счет начислено {ADD_PERCENT}% составляющие {bonus_percent} y.e\n'
              f'Итог на карте {account} y.e')

while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Выйти - "{CMD_EXIT}"')
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой {account} y.e')
        break

    check_richness_tax()

    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, равную {MULTIPLICITY}: '))

    if command == CMD_DEPOSIT:
        deposit(amount)
    elif command == CMD_WITHDRAW:
        withdraw(amount)

    add_bonus()