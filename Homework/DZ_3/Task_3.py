'''
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.

*Верните все возможные варианты комплектации рюкзака.
'''

camping_stuff = {
    'Палатка': 2,
    'Спальный мешок': 1,
    'Рюкзак': 0.5,
    'Котелок': 0.3,
    'Еда': 5,
    'Вода': 1,
    'Спички': 0.1,
    'Фляга с водой': 0.8,
    'Косметичка': 0.5,
    'Походная посуда': 4
}

# Максимальная грузоподъёмность рюкзака
MAX_CAPACITY = 5

def check_weight(camping_stuff, max_weight):
    valid_camping_stuff = []

    for thing in camping_stuff:
        if camping_stuff[thing] <= max_weight:
            valid_camping_stuff.append(thing)

    return valid_camping_stuff

print("Допустимые вещи:", check_weight(camping_stuff, MAX_CAPACITY))