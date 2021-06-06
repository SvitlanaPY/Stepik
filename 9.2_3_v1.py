import json

with open("group_people_9.2.json", "r", encoding="utf-8") as ff:
    data = json.load(ff)

group_id = []
amount = []

print(len(data))

for group_data in data:
    group_id.append(group_data['id_group'])
    count = 0
    print(group_data)
    for person in group_data['people']:
        print(person)
        if person['gender'] == 'Female' and person['year'] > 1977:
            count += 1
    amount.append(count)

print(group_id)
print(amount)

maxx = max(amount)
print(maxx)
index_max = amount.index(maxx)
print(index_max)
print(group_id[index_max], maxx)