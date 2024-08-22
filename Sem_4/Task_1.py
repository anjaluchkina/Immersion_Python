'''
Задание №1

Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы.
Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.
'''

def print_words(text: str) -> None: 
    words_list = sorted(text.split())
    max_len = len(max(words_list, key = len))

    for nn, word in enumerate(words_list, 1):
        print(f'{nn} {word:>{max_len}}')


print_words('каждый охотник желает знать, где сидит фазан')