# Дано число n. Создайте массив размером n×n и заполните его по следующему правилу.
# На главной диагонали должны быть записаны числа 0.
# На двух диагоналях, прилегающих к главной, числа 1. На следующих двух диагоналях числа 2, и т.д.
import sys
sys.stdin = open('ВкладеніМасиви_Діагоналі.txt', 'r')
n = int(input())
a = []
for i in range(n):
    a.append([0]*n)
    for j in range(n):
        a[i][j] = str(abs(j-i))
#a = [[str(abs(j-i)) for j in range(n)] for i in range(n)]  # строки 2-6
for row in a:
    print(' '.join(row))