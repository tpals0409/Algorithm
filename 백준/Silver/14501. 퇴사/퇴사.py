import sys
input = sys.stdin.readline
N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    if (schedule[i][0]+i) > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+schedule[i][0]]+schedule[i][1], dp[i+1])

print(dp[0])