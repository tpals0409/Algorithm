import bisect
N = int(input())
numbers = list(map(int, input().split()))

answer = []
for i in range(N):
    std = numbers[i]
    idx = bisect.bisect_left(answer, std)
    if idx == len(answer):
        answer.append(std)
    else:
        answer[idx] = std
print(len(answer))