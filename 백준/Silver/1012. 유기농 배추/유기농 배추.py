from collections import deque
def bfs(now_y, now_x):
    q = deque([[now_y, now_x]])
    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    while q:
        y, x = q.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if (0 <= ny < N) and (0 <= nx < M):
                if not (visited[ny][nx]) and (maps[ny][nx]) == 1:
                    visited[ny][nx] = True
                    q.append([ny, nx])
    return 1

T = int(input())
for testcase in range(T):
    M, N, K = map(int, input().split())
    maps = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        maps[y][x] = 1

    answer = 0

    for i in range(N):
        for j in range(M):
            if (not visited[i][j]) and (maps[i][j] == 1):
                answer += bfs(i, j)
    print(answer)