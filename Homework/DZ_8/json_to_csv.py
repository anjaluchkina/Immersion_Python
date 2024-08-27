'''
Задание №3

Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
'''

import json
import csv
from pathlib import Path

__all__ = ['json_to_csv']

path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')

def save_to_csv(json_file: Path, csv_file: Path) -> None:
    with open(json_file, 'r', encoding='utf-8') as f_read:
        data = json.load(f_read)

    with open(csv_file, 'w', newline='', encoding='utf-8') as f_write:
        writer = csv.writer(f_write)
        writer.writerow(['ID', 'Имя', 'Уровень'])

        for level, users in data.items():
            for user_id, user_name in users.items():
                writer.writerow([level, user_id, user_name])

if __name__ == '__main__':
    json_file = Path(path / 'users.json')
    csv_file = Path(path / 'users.csv')
    save_to_csv(json_file, csv_file)