import os
from pathlib import Path

def rename_files(desired_name, num_digits, source_ext, target_ext):
    """
    Функция для группового переименования файлов.
    
    Args:
        desired_name (str): Желаемое конечное имя файлов.
        num_digits (int): Количество цифр в порядковом номере.
        source_ext (str): Расширение исходного файла.
        target_ext (str): Расширение конечного файла.
    """
    
    folder_path = Path('C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Homework/DZ_7/DZ_files')
    
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Ошибка: путь '{folder_path}' не существует или не является директорией.")
        return
    
    # Счетчик для порядковых номеров
    counter = 1
    
    # Перебираем все файлы в папке с нужным расширением
    for file_path in folder_path.glob(f"*{source_ext}"):
        new_name = f"{desired_name}_{counter:0{num_digits}d}{target_ext}"
        
        # Создаем новый путь для переименованного файла
        new_file_path = folder_path / new_name
        
        # Проверка на существование файла с новым именем
        if new_file_path.exists():
            print(f"Предупреждение: файл '{new_file_path}' уже существует. Переименование не выполнено.")
            continue
        
        file_path.rename(new_file_path)
        print(f"Файл '{file_path.name}' переименован в '{new_name}'")
        
        counter += 1

rename_files(desired_name="photos", num_digits=1, source_ext=".jpg", target_ext=".png")
rename_files(desired_name="document", num_digits=1, source_ext=".txt", target_ext=".docx")