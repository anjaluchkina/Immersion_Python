'''
Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
'''

import os


def file_info(file_path: str) -> tuple:
    filepath, filename = os.path.split(file_path)
    filename, fileextension = os.path.splitext(filename)
    return filepath, filename, fileextension

file_path = "C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Homework/DZ_5/Task_1.py"

print(file_info(file_path))