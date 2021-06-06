import sys
sys.stdin = open('3_1_8.txt', 'r')

text = []
d = {}
while True:
    text = input().replace(',', '').split()
    if text == ['.']:
        break
    if len(text) > 1:
        key = text[0]
        d[key] = d.get(key, []) + text[1:]
    #   d[text[0]] = d.get(text[0], []) + text[1:]
    elif len(text) == 1 and text[0] in d:
        key = text[0]
        print(*d[key], sep=', ')
    else:
        print("Не найдено")