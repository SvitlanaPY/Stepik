# Дано нечетное число n. Создайте двумерный массив из n×n элементов, заполнив его символами "."
# (каждый элемент массива является строкой из одного символа).
# Затем заполните символами "*" среднюю строку массива, средний столбец массива, главную диагональ и побочную диагональ.
# В результате единицы в массиве должны образовывать изображение звездочки.
# Выведите полученный массив на экран, разделяя элементы массива пробелами.
import sys
sys.stdin = open('ВкладеніМасиви_Сніжинка.txt', 'r')

n = int(input())
a = [['.'] * n for i in range(n)]
nn = n//2
for i in range(n):
    for j in range(n):
        if i == nn or j == nn:
            a[i][j] = '*'
        elif i == j:
            a[i][j] = '*'
        elif i + j == n - 1:
            a[i][j] = '*'
for row in a:
    print(' '.join(row))
