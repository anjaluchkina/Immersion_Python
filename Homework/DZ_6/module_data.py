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


if __name__ == '__main__':
    print(cheak_date('29.02.2023'))