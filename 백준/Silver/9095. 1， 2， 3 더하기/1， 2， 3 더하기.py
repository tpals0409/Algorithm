import sys
input = sys.stdin.readline
testcase = int(input())
for i in range(testcase):
    n = int(input())
    dp = [0 for _ in range(n+1)]
    
    dp[0] = 1
    if n>=1:
        dp[1] = 1
    if n>=2:
        dp[2] = 2
    if n>=3:
        dp[3] = 4
    if n >=4:
        for i in range(4, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    
    print(dp[-1])