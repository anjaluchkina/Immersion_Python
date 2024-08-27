'''
Задание №5

Доработка предыдущей задачи.
Создайте новую функцию которая генерирует файлы с разными расширениями.
Расширения и количество файлов функция принимает в качестве параметров.
Количество переданных расширений может быть любым.
Количество файлов для каждого расширения различно.
Внутри используйте вызов функции из прошлой задачи.
'''

from Task_4 import create_file as cf
from pathlib import Path



def generate_file(file_path: str | Path, **kwargs) -> None:
    for extension, amount in kwargs.items():
        cf(file_path, extension, count=amount)


if __name__ == '__main__':
    path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_7/Result/')
    generate_file(path, bin=2, jpg=3, txt=1)