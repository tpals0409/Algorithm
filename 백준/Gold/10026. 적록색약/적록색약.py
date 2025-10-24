from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
maps_no = [[] for _ in range(N)]
maps_yes = [[] for _ in range(N)]

for i in range(N):
    tmp = list(input().rstrip())
    for j in tmp:
        if j == 'B':
            maps_no[i].append(j)
            maps_yes[i].append(j)
        else:
            maps_no[i].append(j)
            maps_yes[i].append('R')

M = len(maps_no[0])
def bfs(maps):
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            q = deque()
            if not visited[i][j]:
                q.append([i, j])
                while q:
                    y, x = q.popleft()
                    for dy, dx in move:
                        ny, nx = y+dy, x+dx
                        if 0<=ny<N and 0<=nx<M:
                            if not visited[ny][nx] and maps[y][x] == maps[ny][nx]:
                                visited[ny][nx] = True
                                q.append([ny, nx])
                count += 1
    return count
print(bfs(maps_no), bfs(maps_yes))