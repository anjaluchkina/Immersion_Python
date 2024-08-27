'''
Задание №4

Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader
Дополните id до 10 цифр незначащими нулями.
В именах первую букву сделайте прописной.
Добавьте поле хеш на основе имени и индентификатора.
Получившиеся записи созраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
Имя исходного и конечного файлов передайте как аргументы функции.
'''

import json
import csv
import hashlib
from pathlib import Path

def process_csv_to_json(csv_file: Path, json_file: Path):
    data = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Пропускаем заголовок
        for row in reader:
            level, user_id, user_name = row
            user_id = f"{int(user_id):010d}"
            user_name = user_name.capitalize()
            user_hash = hashlib.sha256((user_id + user_name).encode()).hexdigest()
            data.append({
                "level": level,
                "id": user_id,
                "name": user_name,
                "hash": user_hash
            })

    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')
    csv_file = Path(path / 'users.csv')
    json_file = Path(path / 'new_users.json')
    process_csv_to_json(csv_file, json_file)