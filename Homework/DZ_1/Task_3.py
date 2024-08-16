'''
Программа загадывает число от 0 до 1000. 
Необходимо угадать число за 10 попыток. 
Программа должна подсказывать “больше” или “меньше” после каждой попытки. 
Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
RANDOM_NUMBER = randint(LOWER_LIMIT, UPPER_LIMIT)
COUNT_TRY = 10

print("Я загадал число от 0 до 1000. Угадайте его за 10 попыток!")


for test in range(1, COUNT_TRY + 1):
    try:
        guess = int(input(f"Попытка {test}: Введите ваше число: "))
        
        if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
            print(f"Число должно быть в пределах от {LOWER_LIMIT} до {UPPER_LIMIT}. Попробуйте снова.")
            continue
        
        if guess < RANDOM_NUMBER:
            print("Больше!")
        elif guess > RANDOM_NUMBER:
            print("Меньше!")
        else:
            print(f"Поздравляем! Вы угадали число {RANDOM_NUMBER} за {test} попыток!")
            break
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")

if test == COUNT_TRY and guess != RANDOM_NUMBER:
    print(f"К сожалению, вы не угадали. Загаданное число было {RANDOM_NUMBER}.")