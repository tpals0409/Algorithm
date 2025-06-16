def count_le(x):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(N, x // i)
    return cnt

N = int(input())
K = int(input())

low, high = 1, N * N
ans = high

while low <= high:
    mid = (low + high) // 2
    if count_le(mid) >= K:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)