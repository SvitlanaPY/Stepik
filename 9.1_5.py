file = open('numbers.txt', 'r')
count_3 = 0
summ = 0
for row in file:
    row = row.replace('\n', '')
    if len(row) == 3:
        count_3 += 1
    elif len(row) == 2:
        row = int(row)
        summ += row
print(count_3, summ, sep=',')
file.close()
