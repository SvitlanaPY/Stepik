import sys
sys.stdin = open('1_10_7.txt', 'r')
entered_text = input()
roll = ''   # to save entered_text in upper case
All_List = []
count = 0
while entered_text != '.':
    roll = entered_text.upper()
    roll = roll.split()
    if 'PYTHON' in roll:
        count += 1
    All_List.append(entered_text)
    entered_text = input()
for i in range(len(All_List)):
    print(All_List[i][count-1], end=' ')