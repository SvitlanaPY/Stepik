import sys
sys.stdin = open('3_1_11.txt', 'r')

product = input().split(', ')
price = int(input())
person = input().split(', ')
d = {}

while True:
    text = input()
    if text == 'Аукцион закончен!':
        break
    text = text.split()
    key1_product = (' '.join(text[1:-1]))
    key2_name = text[0]
    val_price = int(text[-1])
    if key2_name in person:
        if key1_product not in d:
            d[key1_product] = dict({key2_name: int(val_price)})
        else:
            if int(val_price) > d[key1_product].get(key2_name, int(price)):
                d[key1_product][key2_name] = int(val_price)
            else:
                d[key1_product].setdefault(key2_name, int(val_price))

for i in product:
    if i in d.keys():
        maxx = max(d[i].values())
        for key, val in d[i].items():
            if val == maxx:
                if maxx > price:
                    print(i, key, maxx)
                    break
                else:
                    print(i, "Предложений не было")
    else:
        print(i, "Предложений не было")