import sys
sys.stdin = open('3_1_9.txt', 'r')

d = {}
while True:
    text = input()
    if text == '.':
        break
    text = text.split(': ')
    key = text[0]
    d[key] = text[1]

while True:
    flag = 0
    word = input()
    if word == '.':
        break
    for key in d:
        if word == key:
            print(d[key])
            flag = 1
            break
        if word == d[key]:
            print(key)
            flag = 1
            break
    if flag == 0:
        print("Нет данных")