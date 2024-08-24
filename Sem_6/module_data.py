'''
Задание №7

Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
Функция возвращает истину, если дата может сузествовать или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999]
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високостность вывести в отдельную защищённую функцию.
'''
__all__ = ['cheak_date']

def _is_not_leap(year: int) -> bool:
    return not(year % 400 == 0 or year % 100 != 0 and year % 4 == 0)


def cheak_date(full_date: str) -> bool:
    day, mouth, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or mouth < 1 or mouth >12 or day < 1 or day > 31:
        return False
    if mouth in (4, 6, 9, 11) and day > 30:
        return False
    elif mouth == 2 and day > 29:
        return False
    elif mouth == 2 and day > 28 and _is_not_leap(year):
        return False
    else:
        return True


if __name__ == "__main__":
    date_input = input("Введите дату в формате DD.MM.YYYY: ")
    if cheak_date(date_input):
        print("Дата корректная.")
    else:
        print("Дата некорректная.")