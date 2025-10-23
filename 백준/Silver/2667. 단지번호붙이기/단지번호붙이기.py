from collections import deque
n = int(input())
maps = [[0 for i in range(n)] for i in range(n)]

for i in range(n):
    tmp = input()
    for j in range(n):
        maps[i][j] = int(tmp[j])

visited = [[False for i in range(n)] for i in range(n)]

def bfs(sy, sx):
    q = deque([[sy, sx]])
    count = 1
    visited[sy][sx] = True
    while q:
        y, x = q.popleft()
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if (0<=ny<n) and (0<=nx<n):
                if not visited[ny][nx] and maps[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                    count += 1
    return count

answer = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and maps[i][j] == 1:
            tmp = bfs(i, j)
            answer.append(tmp)

answer.sort()
print(len(answer))
for i in answer:
    print(i)