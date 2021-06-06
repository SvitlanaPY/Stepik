# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу:
# Числа на диагонали, идущей из правого верхнего в левый нижний угол равны 1.
# Числа, стоящие выше этой диагонали, равны 0.
# Числа, стоящие ниже этой диагонали, равны 2.
# Полученный массив выведите на экран. Числа в строке разделяйте одним пробелом.
import sys
sys.stdin = open('ВкладеніМасиви_ПобічнаДіагональ.txt.txt', 'r')
n = int(input())
a = [['1']*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i+j == n-1:
            a[i][j] = '1'
        elif i+j > n-1:
            a[i][j] = '2'
        else:
            a[i][j] = '0'
for row in a:
    print(' '.join(row))
for i in range(n):
    for j in range(n):
        a[i][j] = str(a[i][j])
a = [[str(a[i][j]) for j in range(n)] for i in range(n)]
