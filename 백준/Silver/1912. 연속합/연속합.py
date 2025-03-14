student = int(input())
temp = list(map(int, input().split()))

for size in range(1, student):
    temp[size] = max(temp[size], temp[size-1] + temp[size])

print(max(temp))