'''
Задание №1

Вспоминаем задачу 3 из прошлого семинара. мы сформировали тестовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''

import json
from pathlib import Path

__all__ = ['convert']

path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')

def convert(file: Path) -> None:
    my_dict = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            name, number = line.split()
            my_dict[name.title()] = float(number)

    with open(path / f'{file.stem}.json', 'w', encoding='utf-8') as f_write:
            json.dump(my_dict, f_write, indent=2, ensure_ascii=False)

if __name__ == '__main__':
     convert(Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/results.txt'))