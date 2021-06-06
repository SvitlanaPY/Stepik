import json

with open("manager_sales.json", "r", encoding="utf-8") as ff:
    data = json.load(ff)

names = []   # имена
surnames = []    # фамилии
summ = 0    # сумма продаж
total = []  # сумы продаж каждого менеджера
managers = []
for i in range(len(data)):
    managers.append([data[i]['manager']['first_name'], data[i]['manager']['last_name']])
    names.append(data[i]['manager']['first_name'])
    # data - ліст зі словників
    # data[i] - назва словника в лісті
    # data[i]['manager'] - словник "manager"
    # data[i]['cars'] - список машин по і менеджеру
    surnames.append(data[i]['manager']['last_name'])
    summ = 0
    for k in range(len(data[i]['cars'])):
#        print(data[i]['cars'][k]['price'])
        summ = summ + (data[i]['cars'][k]['price'])
#        print(summ)
    total.append(summ)
# print(total)
# print(names)
# print(surnames)
print(managers)
maxx = max(total)   # 103690
index_max = total.index(maxx)   # 4
print(names[index_max], surnames[index_max], maxx)
# print(names[total.index(max(total))], surnames[total.index(max(total))], maxx)
# print(*managers[index_max], maxx)


# print(data[2]['cars'])


print('---------')


# print(data[0]['cars'])