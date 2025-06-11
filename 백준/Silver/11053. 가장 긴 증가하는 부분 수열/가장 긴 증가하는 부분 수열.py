N = int(input())
arr = list(map(int, input().split()))
counter = [1 for _ in range(N)]

for i in range(N):
    for j in range(i, -1, -1):
        if arr[i] > arr[j]:
            counter[i] = max(counter[i], counter[j]+1)

print(max(counter))