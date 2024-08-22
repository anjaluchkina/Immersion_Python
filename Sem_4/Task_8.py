'''
Задание №8

Создайте несколько переменных заканчивающихся и не оканчивающихся на "s",
Напишите функцию, которая при запуске заменяет содержимое переменных оканчиваюзихся на "s" (кроме переменной из одной буквы "s") на None.
Значения не удаляются, а помещаются в одномёрнные переменные без "s" на конце.
'''

def value_changer():
    globals_variables = globals()
    new_dict = {}
    for key, values in globals_variables.items():
        if key.endswith('s') and key != 's':
            new_dict[key[:-1]] = values
            globals_variables[key] = None
    for key, values in new_dict.items():
        globals_variables[key] = values


datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

value_changer()
print(globals())