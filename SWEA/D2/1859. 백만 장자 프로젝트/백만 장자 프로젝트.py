from collections import deque
T = int(input())
for i in range(T):
    days = int(input())
    price = list(map(int, input().split()))
    std = 0
    benefit = [0 for _ in range(len(price))]
    answer = 0
    for j in range(len(price)-1, -1, -1):
        if price[j] > std:
            std = price[j]
            benefit[j] = price[j]
        else:
            benefit[j] = std
    for k in range(len(price)):
        answer += benefit[k] - price[k]
    print(f"#{i+1} {answer}")