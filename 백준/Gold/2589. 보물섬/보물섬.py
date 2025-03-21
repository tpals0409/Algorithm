from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
road = [list(map(str, input())) for _ in range(N)]

def bfs(y, x):
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[y][x] = 0
    q = deque([[y, x]])
    max_length = 0
    while q:
        y, x = q.popleft()
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ey = y+dy
            ex = x+dx
            if (0<=ey<N) and (0<=ex<M):
                if (visited[ey][ex] == -1) and (road[ey][ex] == 'L'):
                    visited[ey][ex] = visited[y][x]+1
                    max_length = max(max_length, visited[y][x]+1)
                    q.append([ey, ex])
    return max_length

answer = 0
for i in range(N):
    for j in range(M):
        if road[i][j] != 'W':
            answer = max(answer, bfs(i, j))
print(answer)