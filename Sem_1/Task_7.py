'''
Задача №7

Пользователь вводит чисто от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двухзначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двухзначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25 (ноль в начале не учитывается)
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print'''

LOWER_LIMIT = 1
UPPER_LIMIT = 9999
ONE = 1
TEN = 10
HUNDGRED = 100


num = LOWER_LIMIT - ONE
while num < LOWER_LIMIT or num > UPPER_LIMIT:
     num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
if num < TEN:
     result = f'Число {num} - цифра. Квадрат = {num ** num}'
elif num < HUNDGRED:
     fist_num = num // TEN
     second_num = num % TEN
     result = f'Число {num} - двухзначное. Произведение цифр = {fist_num * second_num}'
else:
     fist_num = num // HUNDGRED
     second_num = num // TEN % TEN
     third_num = num % TEN
     mirror = third_num * HUNDGRED + second_num * TEN + fist_num
     result = f'Число {num} - трехзначное. Зеркальное отображение = {mirror}'
print(result)