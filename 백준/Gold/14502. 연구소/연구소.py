from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
virus = []
maps = []

for i in range(N):
    row = list(map(int, input().split()))
    maps.append(row)
    for j in range(M):
        if row[j] == 2:
            virus.append([i, j])


def bfs(maps):
    maps_tmp = [row[:] for row in maps]
    visited = [[False] * M for _ in range(N)]

    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    q = deque()

    for start_y, start_x in virus:
        q.append([start_y, start_x])
        visited[start_y][start_x] = True

    while q:
        y, x = q.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if not visited[ny][nx] and maps_tmp[ny][nx] == 0:
                    visited[ny][nx] = True
                    maps_tmp[ny][nx] = 2
                    q.append([ny, nx])

    count = 0
    for i in range(N):
        for j in range(M):
            if maps_tmp[i][j] == 0:
                count += 1
    return count


answer = 0


def make_wall(cnt):
    global answer

    if cnt == 3:
        answer = max(answer, bfs(maps))
        return

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                make_wall(cnt + 1)
                maps[i][j] = 0


make_wall(0)
print(answer)