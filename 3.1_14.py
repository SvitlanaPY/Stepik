import sys
sys.stdin = open('3_1_14.txt', 'r')

text = input()
d = {}
for elem in text:
    if elem.isalpha():
        d[elem] = d.get(elem, 0) + 1

d_reverse = {}
for key, val in d.items():
    d_reverse[val] = key

while True:
    line = input()
    if line == ".":
        break
    letter, number = line.split(': ')
    number = int(number)
    text = text.replace(d_reverse[number], letter)
print(text)