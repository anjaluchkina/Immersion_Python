'''
Задание №7

Создайте функцию для сортировки файлов по директориям:  видео, изображения, текст и т.п
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
'''

import os
import shutil
from pathlib import Path

def sort_files(source_dir, target_dir):

    # Определяем типы файлов и их расширения
    file_types = {
        'video': ['.mp4', '.avi', '.mov', '.mkv'],
        'image': ['.jpg', '.png', '.gif', '.bmp'],
        'document': ['.doc', '.docx', '.pdf', '.txt', '.odt'],
        'audio': ['.mp3', '.wav', '.flac', '.ogg'],
        'archive': ['.zip', '.rar', '.tar', '.gz', '.bin']
    }

    # Создаем директории для каждого типа файлов
    for dir_name in file_types:
        dir_path = os.path.join(target_dir, dir_name)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    # Перемещаем файлы по директориям
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            for dir_name, extensions in file_types.items():
                for ext in extensions:
                    if filename.endswith(ext):
                        new_file_path = os.path.join(target_dir, dir_name, filename)
                        shutil.move(file_path, new_file_path)
                        break

    # Собираем список файлов, которые не были отсортированы
    unsorted_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]
    return unsorted_files


source_dir = 'C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_7/Result'
target_dir = 'C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_7/Sorting'
unsorted_files = sort_files(source_dir, target_dir)
print("Файлы, которые не были отсортированы:", unsorted_files)