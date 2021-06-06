import json

with open("manager_sales.json", "r", encoding="utf-8") as ff:
    data = json.load(ff)

names = []   # имена
surnames = []    # фамилии
summ = 0    # сумма продаж
total = []  # сумы продаж каждого менеджера
managers = []
for person in data:
    managers.append([person['manager']['first_name'], person['manager']['last_name']])
#   names.append(person['manager']['first_name'])
#   surnames.append(person['manager']['last_name'])
    summ = 0
    for car in person['cars']:
#        print(car['price'])
        summ = summ + car['price']
    total.append(summ)

maxx = max(total)   # 103690
index_max = total.index(maxx)   # 4
print(*managers[index_max], maxx)
