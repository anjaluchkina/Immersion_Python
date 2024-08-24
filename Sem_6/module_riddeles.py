'''
Задание №7

Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.
'''
__all__ = ['riddle', 'storage', 'show_results']

def riddle(riddle_text: str, answers: list[str], count: int = 5) -> int:
    print(f'Отгадай загадку:\n{riddle_text}')
    for nn in range(1, count + 1):
        ans = input(f'Попытка: №{nn}: ').lower()
        if ans in answers:
            return nn        
    return 0

def storage():
    puzzels = {
        'Сидит дед во 100 шуб одет' : ['лук', 'луковица'],
        'Чистая, но не вода, Белая, но снег боб, Сладкая, но не мороженое' : ['sugar', 'сахар'],
        'Не лает, не кусает, а в дом не пускает' : ['замок', 'домофон'],
    }
    for puzzels, answers in puzzels.items():
        result = riddle(puzzels, answers)
        print(f'Угадал с {result}й попытки!' if result > 0 else 'Не угадал!')
    return(puzzels, result)




_data = {}

def save_results(puzzle: str, nn: int) -> None:
    _data[puzzle] = nn

def show_results():
    res = (f'Загадку "{puzzle}" разгадали с {nn}й попытки' if nn > 0 else\
            f'Загадку "{puzzle}" не разгадали'\
                for puzzle, nn in _data.items())
    print(*res, sep='\n')


if __name__ == '__main__':
    storage()
    show_results()