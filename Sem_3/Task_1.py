'''
Задание №1

Вручную создайте список с целыми числами которые повторяются. 
Получите новый спиисок, который содержит уникальные (без повтора) элементы исходного списка.

*Подготовьте два решения, короткое и длинное которое не использует другие колекции помимо списков.
'''

'''# Вариант 1
data = [42, 73, 5, 42, 42, 2, 3, 7, 73, 42]
my_list = list(set(data))

print(my_list)'''

data = [42, 73, 5, 42, 42, 2, 2, 5, 5, 2, 2, 3, 7, 73, 42]
new_list = []

for item in data:
    if item not in new_list:
        new_list.append(item)

print(new_list)