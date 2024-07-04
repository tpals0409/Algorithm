import sys
input = sys.stdin.readline

n = int(input())
S = set()
for _ in range(n):
    tmp = list(input().rstrip().split())
    command = tmp[0]
    if len(tmp) == 2:
        number = int(tmp[1])
    if command == 'add':
        S.add(number)
    elif command == 'remove':
        if number in S:
            S.remove(number)
    elif command == 'check':
        if number in S:
            print(1)
        else:
            print(0)
    elif command == 'toggle':
        if number in S:
            S.remove(number)
        else:
            S.add(number)
    elif command == 'all':
        S = {i for i in range(1, 21)}
    elif command == 'empty':
        S = set()