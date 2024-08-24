'''
Напишите функцию в шахматный модуль. 
Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

import random

def is_safe(queens):

    rows = set()
    cols = set()
    diag1 = set()  
    diag2 = set() 

    for (x, y) in queens:
        if x in rows or y in cols or (x - y) in diag1 or (x + y) in diag2:
            return False
        
        rows.add(x)
        cols.add(y)
        diag1.add(x - y)
        diag2.add(x + y)

    return True


def generate_random_queens():
    cols = random.sample(range(1, 9), 8)  # Случайные столбцы от 1 до 8
    queens = [(row, col) for row, col in enumerate(cols, start=1)]
    return queens


if __name__ == '__main__':
    successful_arrangements = []
    
    while len(successful_arrangements) < 4:
        queens = generate_random_queens()
        if is_safe(queens):
            successful_arrangements.append(queens)

    for i, arrangement in enumerate(successful_arrangements, start=1):
        print(f"Успешная расстановка {i}: {arrangement}")