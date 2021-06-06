#
import sys
sys.stdin = open('ВкладеніМасиви_Ввід.txt', 'r')

a = []
p = int(input())
for i in range(p):
    b = input().split()
    for j in range(len(b)):
        b[j] = int(b[j])
    a.append(b)
print(a)


aa = []
nn = int(input())
for i in range(nn):
    aa.append([int(j) for j in input().split()])
print(aa)


aaa = []
m = int(input())
aaa = [[int(j) for j in input().split()] for i in range(m)]
print(aaa)

