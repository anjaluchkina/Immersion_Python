'''
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
где ключ — значение переданного аргумента, 
а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.
'''

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except TypeError:
            result[str(value)] = key
    return result

result = create_dict(a=1, b=2.5, c='hello', d=[1, 2, 3])
print(result)