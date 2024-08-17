'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата.
'''

num = int(input('Введите десятичное число: '))
print('Проверка: ', hex(num))

NOTATION = 16
my_dict = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
res = ''
while num > 0:
    if num % NOTATION in my_dict:
        res = my_dict[num % NOTATION] + res
    else:
        res = str(num % NOTATION) + res
        num = num // NOTATION
print(res)