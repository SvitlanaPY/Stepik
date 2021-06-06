import json

with open("group_people_9.2.json", "r", encoding="utf-8") as ff:
    data = json.load(ff)

groupID_amount = []

for group_data in data:
    count = 0
    # print(group_data)
    for person in group_data['people']:
        # print(person)
        if person['gender'] == 'Female' and person['year'] > 1977:
            count += 1
    groupID_amount.append([group_data['id_group'], count])
#     groupID_amount.append([count, group_data['id_group']])

# maxx = max(groupID_amount)
# print(maxx[1], maxx[0])
print(groupID_amount)
maxx = max(groupID_amount, key = lambda x: x[1])
print(*maxx)