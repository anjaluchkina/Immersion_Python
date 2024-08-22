'''
Задание №7

Функция получает на вход словать с названием компании в качестве ключа и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании.
Если все компании прибыльные, верните истину, а если хотябы одна убыточная ложь.
'''

def final_income(my_dict: dict[str, list[int | float]]) -> bool:
    return all(map(lambda cur_list: sum(cur_list) > 0, my_dict.values()))

'''for generator
def final_income(my_dict: dict[str, list[int | float]]) -> bool:
    return all(sum(cur_list) > 0 for cur_list in my_dict.values())'''

data = {
    'Рога': [42, -73, 12, 85, -15, 2],
    'Копыта': [45, 25, -100, 22, 1],
    'Хвосты': [-500, 123, 52, 45, 93]
}

print(final_income(data))