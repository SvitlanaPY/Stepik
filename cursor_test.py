file = open('numbers.txt', 'r')
count_three = 0
sum_two = 0
for i in file.read().split():
    if len(str(i)) == 3:
        count_three += 1
    elif len(str(i)) == 2:
        sum_two += int(i)
print(count_three)
print(sum_two)
file.close()