import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []
answer = []
for i in range(N):
    height = towers[i]
    while stack and stack[-1][1] < height:
        stack.pop()

    if not stack:
        answer.append(0)
    else:
        answer.append(stack[-1][0] + 1)

    stack.append((i, height))

print(' '.join(map(str, answer)))
