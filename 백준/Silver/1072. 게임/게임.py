N, M = map(int, input().split())
Z = (M*100)/N
start = 1
end = N

while start <= end:
    mid = (start + end) // 2
    if ((M + mid) * 100) // (N + mid) > Z:
        end = mid - 1
    else:
        start = mid + 1

if start > N:
    print(-1)
else:
    print(start)