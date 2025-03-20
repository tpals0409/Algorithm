def solution(m, n, puddles):
    MOD = 1000000007
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1

    # 웅덩이 표시
    for x, y in puddles:
        dp[y][x] = -1

    for y in range(1, n+1):
        for x in range(1, m+1):
            if x == 1 and y == 1:
                continue
            
            if dp[y][x] == -1:
                dp[y][x] = 0
                continue
            
            else:
                dp[y][x] += dp[y-1][x]
            if dp[y][x-1] != -1:
                dp[y][x] += dp[y][x-1]

            dp[y][x] %= MOD  # 나머지 연산 적용

    return dp[n][m]