import sys
sys.stdin = open('1_10_13.txt', 'r')
n = input()
numms = []
while n != '.':
    numms.append(str(int(n) ** 2))
    n = input()
print(' '.join(numms[::-1]))