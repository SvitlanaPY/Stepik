n = 4
m = 5
a = [0] * m
print(a)
b = []
for i in range(n):
    b.append(a)
print(b)


nn = 4
mm = 5
aa = [0] * nn
for i in range(nn):
    aa[i] = [0] * mm
print(aa)


k = 4
l = 5
aaa = []
for i in range(k):
    aaa.append([0] * l)
print(aaa)


p = 3
s = 4
b = [[0] * int(input()) for i in range(p)]   # запис [0] * int(input()) - дозволяє задати довжину вкладеного списку у спискові
# вкладений список міститиме стільки елементів, скільки ми введемо/ подамо в інпуті
# або: b = [[0] * s for i in range(p)] - створимо список, довжиною в 3 (р=3) елементи і по 4 (s=4) елементи в кожному вкладеному списку
print(b)



