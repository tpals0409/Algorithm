import sys
from collections import deque
input = sys.stdin.readline
node_num = int(input())
bridge_num = int(input())
bridge = [list(map(int, input().split())) for _ in range(bridge_num)]
visited = [False for _ in range(node_num+1)]
matrix = [[0 for _ in range(node_num+1)] for _ in range(node_num+1)]

for a, b in bridge:
    matrix[a][b] = 1
    matrix[b][a] = 1

stack = deque([1])
count = 0
while stack:
    tmp = stack.pop()
    if visited[tmp] == False:
        count += 1
        visited[tmp] = True

    for i in range(len(matrix[tmp])):
        if matrix[tmp][i] == 1:
            if visited[i] == False:
                stack.append(i)
            else:
                continue

print(count-1)