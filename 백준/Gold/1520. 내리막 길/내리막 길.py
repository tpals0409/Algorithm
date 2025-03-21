import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

M, N = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
def move(y, x):
    now = road[y][x]
    if (y == M-1) and (x == N-1):
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    route = 0
    for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ey = y+dy
        ex = x+dx
        if (ey>=0 and ey<M) and (ex>=0 and ex<N):
            if now > road[ey][ex]:
                route += move(ey, ex)
    dp[y][x] = route
    return dp[y][x]

answer = move(0, 0)
print(answer)