N = int(input())
buget = list(map(int, input().split()))
buget = sorted(buget)
total_buget = int(input())

start = 0
end = max(buget)
mid = 0

while start <= end:
    mid = (start + end) // 2
    sum_buget = sum(min(b, mid) for b in buget)

    if sum_buget > total_buget:
        end = mid - 1
    else:
        start = mid + 1

print(end)