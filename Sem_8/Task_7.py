'''
Задание № 7

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader
Распечатайте его как pickle строку.
'''

import pickle
import csv
from pathlib import Path

path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')

def csv_to_pickle(csv_file: Path) -> None:
    with open(path / csv_file, 'r', encoding='utf-8') as f_read:
        data = []
        reader = csv.reader(f_read, delimiter=',')
        
        headers = next(reader)
        
        for row in reader:
            data.append(dict(zip(headers, row)))

    # Сериализация данных в формат pickle
    pickle_data = pickle.dumps(data)
    
    # Печатаем pickle строку
    print(pickle_data)

if __name__ == '__main__':
    csv_to_pickle(Path('new_users.csv'))