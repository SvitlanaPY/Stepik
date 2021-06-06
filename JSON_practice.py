import json
from datetime import datetime
from random import randint

str_json = """
{
"response": {
    "count": 5961777,
    "users": [{
        "userId": "krish",
        "jobTitle": "Developer",
        "firstName": "КРІШ",
        "lastName": "Lee",
        "employeeCode": "E1",
        "region": "CA",
        "phoneNumber": "123456",
        "emailAddress": "krish.lee@learningcontainer.com"
    }, {
        "userId": "devid",
        "jobTitle": "Developer",
        "firstName": "Devid",
        "lastName": "Rome",
        "employeeCode": "E2",
        "region": "CA",
        "phoneNumber": "1111111",
        "emailAddress": "devid.rome@learningcontainer.com"
    }, {
        "userId": "tin",
        "jobTitle": "Program Manager",
        "firstName": "tin",
        "lastName": "jonson",
        "employeeCode": "E3",
        "region": "CA",
        "phoneNumber": "2222222",
        "emailAddress": "tin.jonson@learningcontainer.com"
    } ]
}
}
"""
data = json.loads(str_json)   # зчитуємо стічку формату .json

print('Словник data =', data)
print('----------------------------')

print('del employeeCode and add likes and userAge:')
for elem in data['response']['users']:
    print('users:', elem)
#    print(elem['firstName'], elem['lastName'])
#    print('___')
    del elem['employeeCode']
    elem['likes'] = randint(100, 300)
    elem['userAge'] = randint(18, 65)
    elem['date_now'] = datetime.now().strftime('%d.%m.%y')
    elem['canAccess'] = True
    elem['Null_None'] = None
print(data['response']['users'])
print()


# new_json = json.dumps(data, indent=2)    # створює стрічку у вигляді .json-а
# print(new_json)
# print(json.loads(new_json))


# створюємо файл у форматі .json
#with open ('my_json.json', 'w') as ffile:
#    json.dump(data, ffile, indent=3)

# відкриваємо/зчитуємо файл у форматі .json
#with open ('my_json.json', 'r') as ffile:
#    data = json.load(ffile)
#print(data)


