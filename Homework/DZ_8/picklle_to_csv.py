'''
Задание № 6

Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
Для тестирования возьмите pickle версию файла из задачи 4-того семинара.
Функция должна извлекать ключи словаря для заголовков столбца из преданного файла.
'''

import pickle
import csv
from pathlib import Path

__all__ = ['pickl_to_csv']

path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')


def pickl_to_csv(picl_file: Path) -> None:
    with (open(path / picl_file, 'rb') as f_read,
        open(path / f'{picl_file.stem}.csv', 'w', encoding='utf-8', newline='') as f_write
    ):
        data = pickle.load(f_read)
        headers_list = list(data[0].keys())
        csv_write = csv.DictWriter(f_write, fieldnames=headers_list,\
                                   dialect='excel-tab', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickl_to_csv(Path('new_users.pickle'))