'''
Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
'''

my_list = [42, 1, 73, 5, 42, 42, 1, 2, 2, 5, 5, 2, 1, 2, 3, 7, 1, 73, 42]
result_list = []


def remove_duplicates(list1):
    temp = set(list1)
    return list(temp)

result = remove_duplicates(my_list)
print(result)