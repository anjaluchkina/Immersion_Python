'''
Задание №4

Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования
встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком.
'''

def sort_list(my_list: list[int]):
    count = 1
    while count < len(my_list):
        is_sorted = True
        for i in range(len(my_list) - count):
            if my_list[i] > my_list[i + 1]:
                is_sorted = False
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        count += 1

        
data_list = [8, 15, 42, 4, 23, 16, 9]

sort_list(data_list)
print(data_list)