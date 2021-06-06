# Даны два числа n и m. Создайте двумерный массив размером n×m и заполните его символами "." и "*" в шахматном порядке.
# В левом верхнем углу должна стоять точка.
import sys
sys.stdin = open('ВкладеніМасиви_ШахматнаДошка.txt', 'r')
n, m = [int(i) for i in input().split()]
a = [['.']*m for i in range(n)]
for i in range(n):
    for j in range(m):  # if (i%2==0 and j%2==1) or (i%2==1 and j%2==0)
        if (i + j) % 2 == 1:
            a[i][j] = '*'
for row in a:
    print(' '.join(row))