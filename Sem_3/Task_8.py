'''
Задание №8
#-----------

Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
Ответьте на вопросы:
Какие вещи взяли все три друга
Какие вещи уникальны, есть только у одного друга
Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсуствует
Для решения используйте операции с множествами. 
Код должен расшираться на любое большие количество друзей.
'''

hike = { 
    'Aaz' : ("спички", "спальник", "дрова", "топор"),
    'Skeeve' : ("спальник", "спички", "вода", "еда"),
    'Tananda' : ("вода", "спички", "косметичка", "топор"),
}

all_things = set()
for things in hike.values():
    # for thing in things:
    #     all_things.add(things)
    all_things.update(things)

print(f'Полный список всех вещей: {all_things}')

unique_things = {}

for master_friend, master_things in hike.items():
    for slave_friend, slave_things in hike.items():
        if master_friend != slave_friend:
            if master_friend not in unique_things:
                unique_things[master_friend] = set(master_things) - set(slave_things)
            else:
                unique_things[master_friend] -= set(slave_things)

print(f'Список уникальных вещей: {unique_things}')

double_things = set(all_things)

for things in unique_things.values():
    double_things -= things

print(f'Список дублирующихся вещей: {double_things}')

for friend, things in hike.items():
    print(f'{friend} отсутсвует {double_things - set(things)}')
   # print(f' Второй вариант : {friend} отсутсвует {(set(things) ^ double_things) - set(unique_things[friend])}')
