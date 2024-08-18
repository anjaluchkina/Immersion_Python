'''
Задание №6

Напишите программу, которая запрашивает год и проверяет его на високостьность.
Распишите все возможности проверки в цепочки elif
Откажитесь от машических чисел
Обязательно учтите год ввода Григорианского календаря
В коде должны быть один input и один print'''

REFORM = 1582
BIG_LEAP_YERA = 400
SMALL_LEAP_YEAR = 4
LARGE_NONE_LEAP_YEAR = 100
MULTIPLE = 0

year = int(input("Ввeдите год: "))
if year < REFORM:
     result = "Год до ввода Григорианского календаря"
elif year % BIG_LEAP_YERA == MULTIPLE:
     result = f'{year} - Високосный год'
elif year % LARGE_NONE_LEAP_YEAR == MULTIPLE:
     result = f'{year} - Не високосный год'
elif year % SMALL_LEAP_YEAR == MULTIPLE:
     result = f'{year} - Високосный год'
else:
     result = f'{year} - Не високосный год'
print(result)