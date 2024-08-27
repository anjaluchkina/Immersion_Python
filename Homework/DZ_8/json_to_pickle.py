'''
Задание № 5

Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
'''

import pickle
import json
from pathlib import Path

__all__ = ['json_to_pickle']

path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')


def json_to_pickle(js_path: Path) -> None:
    for file in js_path.iterdir():
        if file.is_file() and file.suffix == '.json':
            with open(path / file, 'r', encoding='utf-8') as f_read:
                data =json.load(f_read)
            with open(path / f'{file.stem}.pickle', 'wb') as f_writebyte:
                pickle.dump(data, f_writebyte)


if __name__ == '__main__':
    json_to_pickle(Path(path))