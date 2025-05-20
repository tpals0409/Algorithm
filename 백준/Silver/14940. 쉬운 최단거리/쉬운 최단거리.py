import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]

INF = -1
dist = [[INF]*m for _ in range(n)]
ty = tx = -1

for i in range(n):
    for j in range(m):
        if road[i][j] == 0:
            dist[i][j] = 0
        elif road[i][j] == 2:
            ty, tx = i, j
            dist[i][j] = 0

dq = deque()
dq.append((ty, tx))
while dq:
    y, x = dq.popleft()
    for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
        ny, nx = y+dy, x+dx
        if 0 <= ny < n and 0 <= nx < m and dist[ny][nx] == -1:
            dist[ny][nx] = dist[y][x] + 1
            dq.append((ny, nx))
for i in range(n):
    print(' '.join(map(str, dist[i])))