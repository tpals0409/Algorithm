testcase = int(input())

for _ in range(testcase):
    days = int(input())
    cost = list(map(int, input().split()))
    
    answer = 0
    max_price = 0

    for i in range(days - 1, -1, -1):
        if cost[i] > max_price:
            max_price = cost[i]
        else:
            answer += max_price - cost[i]

    print(answer)