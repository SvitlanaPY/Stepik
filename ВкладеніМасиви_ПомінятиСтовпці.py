import sys
sys.stdin = open('ВкладеніМасиви_ПомінятиСтовпці.txt', 'r')
from NumPy import *

n, m = [int(i) for i in input().split()]
print(n, m)
a = [[int(j) for j in input().split()] for i in range(n)]
print(a)
i, j = [int(i) for i in input().split()]
print(i, j)
#a(:, [i, j]) = a(:, [j, i]);
#a[:, [1, 0] = a[:, [0, 1]]
def swap_columns(a, i, j):
    temp = a[:, i]
    a[:, i] = a[:, j]
    a[:, j] = temp
print(a)