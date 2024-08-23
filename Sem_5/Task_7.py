'''
Задание №7

Создайте функцию-генератор.
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: "число является простым, если делиться нацело только на единицу и на себя"
'''

def primes(N):
    """
    -генератор, которая генерирует N простых чисел, начиная с числа 2.
    """
    primes = []
    num = 2
    while len(primes) < N:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

print(*primes(13))