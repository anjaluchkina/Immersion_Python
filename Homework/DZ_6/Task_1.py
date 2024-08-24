'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

from sys import argv
from module_data import cheak_date as cy  # Убедитесь, что название функции правильное

if __name__ == '__main__':
    if len(argv) != 2:
        print("Используйте: python Task_1.py dd.mm.yyyy")
    else:
        date_input = str(argv[1])
        try:
            day, month, year = map(int, date_input.split('.'))
            full_date = f'{day:02d}.{month:02d}.{year}'
            result = cy(full_date)
            if result:
                print(f"{full_date} високосный год.")
            else:
                print(f"{full_date} не високосный год.")
        except ValueError:
            print("Ошибка: Введите дату в формате dd.mm.yyyy.")