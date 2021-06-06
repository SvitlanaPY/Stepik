text = input().lower()
signs = '.,!?:;–'
for i in range(len(signs)):     # i=. i=, i=! i=? i=: i=; i=–
    text = text.replace(signs[i],'')
print(text)