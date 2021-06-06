import sys
sys.stdin = open('3_1_10.txt', 'r')

from string import ascii_lowercase
morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}
#text = input().lower().split()
text = input().lower()
for i in text:
    if i in ascii_lowercase:
        txt = text.split()
        for word in txt:
            letter = list(word)
            for i in letter:
                for key, val in morze.items():
                    if i == key:
                        strr = strr + (morze[i] + ' ')
                    print(strr[:-1])
            print(end='\t')
    else:
        text = text.split('\t')
        for elem in text:
            elem = elem.split()
            for i in elem:
                for key, val in morze.items():
                    if i == val:
                        print(key, end = '')
            print(end =' ')
