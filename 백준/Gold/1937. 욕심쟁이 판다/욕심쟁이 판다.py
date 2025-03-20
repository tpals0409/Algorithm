import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 증가

input = sys.stdin.readline
N = int(input())  # 격자의 크기 입력
matrix = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 (메모이제이션) - 초기값 -1
dp = [[-1] * N for _ in range(N)]

def moving(y, x):
    if dp[y][x] != -1:
        return dp[y][x]  # 이미 계산된 값이면 그대로 반환

    dp[y][x] = 1  # 최소한 현재 위치 1칸 포함

    # 네 방향 탐색
    for dy, dx in [[0,1], [0,-1], [1,0], [-1,0]]:
        ey = y + dy
        ex = x + dx
        if (0 <= ey < N) and (0 <= ex < N):  # 범위 확인
            if matrix[y][x] < matrix[ey][ex]:  # 증가하는 경우만 이동
                dp[y][x] = max(dp[y][x], moving(ey, ex) + 1)

    return dp[y][x]

# 모든 위치에서 출발하여 최장 증가 경로 찾기
max_path = max(moving(y, x) for y in range(N) for x in range(N))

# 최장 증가 경로 출력
print(max_path)
