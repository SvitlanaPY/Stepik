import sys
sys.stdin = open('1_10_15.txt', 'r')
request = input()
Server = []
while request != '.':
    request = request.split()
    if 'POST' in request[0]:
        Server.append(request[1:])
    elif 'GET' in request[0]:
        print(*Server[-1])
    elif 'DELETE' in request[0]:
        Server.pop()
    request = input()
for i in Server:
    print(*i, end=' ')