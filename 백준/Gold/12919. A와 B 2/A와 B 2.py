import sys
from collections import deque
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

reversed_A = A[::-1]

q = deque([B])
can = False
while q:
    tmp = q.popleft()
    if tmp == A:
        can = True
    if tmp[-1] == 'A':
        tmp2 = tmp[:-1]
        if A in tmp2 or reversed_A in tmp2:
            q.append(tmp2)
    if tmp[0] == 'B':
        tmp3 = tmp[1:]
        tmp3 = tmp3[::-1]
        if A in tmp3 or reversed_A in tmp3:
            q.append(tmp3)

if can:
    print(1)
else:
    print(0)