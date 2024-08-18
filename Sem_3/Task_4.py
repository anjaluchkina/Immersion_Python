'''
Задание №4

Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.
'''

data = [42, 73, 5, 1, 42, 42, 2, 1, 2, 5, 3, 7, 1, 73, 42]
COUNT = 2

for item in set(data):
    if data.count(item) == COUNT:
        for _ in range(COUNT):
            data.remove(item)

print(data)