import sys
sys.stdin = open('3_1_7.txt', 'r')
#file =open(r'E:\Svetik\Python\Stepic\3_1_7.txt', 'r')

dictt = {'admin': {'read': ['confidential', 'settings', 'system', 'ordinary'],
                   'edit': ['confidential', 'settings', 'system', 'ordinary']},
         'experienced': {'read': ['settings', 'system', 'ordinary'],
                         'edit': ['ordinary']},
         'user': {'read':['ordinary'],
                  'edit': ['ordinary']}}
d = {}
while True:
    text = input()
    if text == '.':
        break
    file, file_type = text.split()
    d[file] = file_type

while True:
    text = input()
    if text == '.':
        break
    file, operation, role = text.split()
    # available_types = dictt[role][operation]
    if d[file] in dictt[role][operation]:
        print("Access granted")
    else:
        print("Access denied")


