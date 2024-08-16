'''
Задача №9

Введите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
'''
LOWER_LIMIT = 2
UPPER_LIMET = 10
COLUMN = 4

for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMN):
    for num_2 in range(LOWER_LIMIT, UPPER_LIMET):
        for num_1 in range(row , row  + COLUMN):
            print(f'{num_1 : > 2} x {num_2 : > 2} = {num_1 * num_2 : > 2}', end='\t')
        print()
    print()