'''
Задание №1

Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
Первое число int, второе float разделены вертикальной чертой.
Минимальное число -1000, максимальное число +1000.
Количество строк и имя файла передаются как аргументы функции.
'''

from random import randint, uniform
from pathlib import Path

MIN_NUMBER = -1000
MAX_NUMBER = 1000

def fill_num(filename: str | Path, count: int) -> None:
    with open(filename, 'a', encoding='utf-8') as f:
        for _ in range(count):
            num_int = randint(MIN_NUMBER, MAX_NUMBER)
            num_float = uniform(MIN_NUMBER, MAX_NUMBER)
            f.write(f'{num_int}|{num_float}\n')

if __name__ == '__main__':
    fill_num(Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_7/Result/numbers.txt'), 256)