'''
Задание №2

Напишите фукцию, которая в бесконечном цикле запрашивает имя, личный индетификатор и уровень доступа (от 1 до 7)
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от увроня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.
'''

import json
from pathlib import Path

path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result')


def set_users(file: Path) -> None:
    uids = set()

    if not file.is_file():
        data = {str(i): {} for i in range(1, 7 + 1)}
    else:
        with open(file, 'r', encoding='utf=8') as f_read:
            data = json.load(f_read)
        for value in data.values():
            uids.update(value.keys())
    
    while True:
        name = input('Введите имя: ')
        if not name:
            break
        id = input('Введите id: ')
        lvl = input('Введите уровень от 1 до 7: ')
        if ~ (id in uids and data[lvl].get(id) is None):
            data[lvl].update({id: name})
            with open(file, 'w', encoding='utf-8') as f_write:
                json.dump(data, f_write, indent=2, ensure_ascii=False)

if __name__ == '__main__':    
    set_users(Path(path / 'users.json'))
