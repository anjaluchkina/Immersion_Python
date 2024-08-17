'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions
'''

import fractions

frac1 = input("Введите первую дробь в виде 'a/b': ")
frac2 = input("Введите вторую дробь в виде 'c/d': ")


def sum(frac1, frac2):
    f1 = fractions.Fraction(int(frac1.split('/')[0]), int(frac1.split('/')[1]))
    f2 = fractions.Fraction(int(frac2.split('/')[0]), int(frac2.split('/')[1]))

    sum = f1 + f2
    prod = f1 * f2

    return (str(sum), str(prod))

result = sum(frac1, frac2)
print("Сумма дробей:", result[0])
print("Произведение дробей:", result[1])