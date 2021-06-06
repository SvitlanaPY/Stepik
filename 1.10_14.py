import sys
sys.stdin = open('1_10_14.txt', 'r')
text = input()
while text != '.':
    if '!! ' in text and ' !!':
        print('предупреждение')
    elif '@@ ' in text and ' @@' in text:
        print('ошибка')
    elif '// ' in text and ' //' in text:
        print('информация')
    elif '** ' in text and ' **' in text:
        print("подробное сообщение")
    text = input()
