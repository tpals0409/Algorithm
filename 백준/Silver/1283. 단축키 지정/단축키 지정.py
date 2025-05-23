import heapq
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
where_command = [-1]*N
command = set(' ')
line = []
for _ in range(N):
    is_in = False
    l = input().rstrip()
    line.append(l)
    tmp = list(l.split())
    count = 0
    for i in range(len(tmp)):
        if tmp[i][0].upper() in command:
            count += len(tmp[i])+1
            continue
        else:
            command.add(tmp[i][0].upper())
            where_command[_] = count
            is_in = True
            break
    if is_in:
        continue
    for i in range(len(l)):
        if l[i].upper() in command:
            continue
        else:
            command.add(l[i].upper())
            where_command[_] = i
            break

command.remove(' ')
for i in range(N):
    for j in range(len(line[i])):
        if j == where_command[i]:
            print(f'[{line[i][j]}]', end="")
        else:
            print(line[i][j], end="")
    print()