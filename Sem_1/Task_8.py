'''
Задача №8

Нарисовать в консоли ёлку спросив у пользотеля кол-во рядов.
Пример результата:
Сколько рядов у ёлки? 5
     *
    ***
   *****
  *******
 *********
'''

SPACE = ' '
STAR = '*'
ONE = 1
TWO = 2

rows = int(input('Сколько рядов у ёлки: '))
spaces = rows - ONE
stars = ONE

for i in range(rows):
    print(spaces * SPACE + stars * STAR)
    spaces -= ONE
    stars += TWO