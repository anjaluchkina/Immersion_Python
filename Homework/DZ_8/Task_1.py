import os
import json
import csv
import pickle

def get_directory_info(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        parent_dir = os.path.basename(root)
        total_size = 0
        
        # Обработка директорий
        for d in dirs:
            dir_path = os.path.join(root, d)
            dir_size = sum(os.path.getsize(os.path.join(dir_path, f)) for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)))
            results.append({
                'name': d,
                'type': 'directory',
                'parent': parent_dir,
                'size': dir_size
            })
        
        # Обработка файлов
        for f in files:
            file_path = os.path.join(root, f)
            file_size = os.path.getsize(file_path)
            results.append({
                'name': f,
                'type': 'file',
                'parent': parent_dir,
                'size': file_size
            })
            total_size += file_size

        if parent_dir:
            parent_info = next((item for item in results if item['name'] == parent_dir and item['type'] == 'directory'), None)
            if parent_info:
                parent_info['size'] += total_size

    return results

def save_results(source_directory, save_directory):
    results = get_directory_info(source_directory)

    with open(os.path.join(save_directory, 'directory_info.json'), 'w', encoding='utf-8') as json_file:
        json.dump(results, json_file, ensure_ascii=False, indent=4)

    with open(os.path.join(save_directory, 'directory_info.csv'), 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)

    with open(os.path.join(save_directory, 'directory_info.pickle'), 'wb') as pickle_file:
        pickle.dump(results, pickle_file)

source_directory = 'C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Sem_8/Result'
save_directory = 'C:/Users/HYPERPC/Desktop/IT/Immersion_Python/Homework/DZ_8/Result'
save_results(source_directory, save_directory)