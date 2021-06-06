import sys
sys.stdin = open('1_10_16.txt', 'r')
numbers = input()
while numbers != '.':
    numbers = numbers.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    a, b, c = numbers
    if int(a) + int(b) == int(c):
        print('{} + {} = {}'.format(a, b, c))
    elif int(a) - int(b) == int(c):
        print('{} - {} = {}'.format(a, b, c))
    elif int(a) * int(b) == int(c):
        print('{} * {} = {}'.format(a, b, c))
    elif int(a) / int(b) == int(c):
        print('{} / {} = {}'.format(a, b, c))
    else:
        print("Error")
    numbers = input()