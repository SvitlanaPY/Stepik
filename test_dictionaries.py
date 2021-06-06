# q = dict.fromkeys(['a', 'b', 'c'], 100)
# print(q)

# numbers = {1: "one", 2: "two", 3: "three", "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]}
# print(numbers["nums"])

# print(n[0])

numbers = {1: "one", 2: "two", 3: "three"}
numbers[4] = "four"
numbers[5] = "five"
print(numbers)
del numbers[5]
print(numbers)
print(len(numbers))
print(1 in numbers, 5 not in numbers)

if 6 in numbers:
    print(numbers[6])
else:
    numbers[6] = "six"
print(numbers)

# person = {}
# s = "IVANOV IVAN SAMARA SGU 5 4 5 5 4 3 5"
# s = s.split()
# print(s)
# person["last_name"] = s[0]
# person["first_name"] = s[1]
# person["city"] = s[2]
# person["univer"] = s[3]
# person["marks"] = []
# for i in s[4:]:
#     person["marks"].append(int(i))
# print(person)