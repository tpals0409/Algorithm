from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
maps = [[0 for _ in range(N)] for _ in range(N)]

max_value = 0
min_value = float('inf')
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        max_value = max(max_value, line[j])
        min_value = min(min_value, line[j])
        maps[i][j] = line[j]

def bfs(rain):
    visited = [[False for _ in range(N)] for _ in range(N)]
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and maps[i][j] > rain:
                q = deque([[i, j]])
                visited[i][j] = True
                while q:
                    y, x = q.popleft()
                    for dy, dx in move:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<N and 0<=nx<N:
                            if not visited[ny][nx] and maps[ny][nx] > rain:
                                visited[ny][nx] = True
                                q.append([ny, nx])
                count += 1
    return count

answer = 1

for i in range(min_value, max_value+1):
    answer = max(answer, bfs(i))

print(answer)