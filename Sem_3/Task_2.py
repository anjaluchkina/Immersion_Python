'''
Задание №2

Пользователь вводит данные. Сделать проверку данных и преобразуйте, 
если возможно в один из вариантов:

- Целое положительное число
- Вещественное положительное или отрицательное число
- Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква.
- Строку в нижнем регистре в остальных случаях
'''

data = input('Введите данные: ')

if data.isdigit():
    new_data = int(data)
elif data.count('.') == 1 and data.count('-') < 2 and \
        data[1:].count('-') == 0 and data.replace('.', '').replace('-', ''):
    new_data = float(data)
elif not data.islower():
    new_data = data.lower()
else:
    new_data = data.upper()

print([new_data])