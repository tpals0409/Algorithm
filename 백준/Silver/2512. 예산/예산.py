from collections import deque
num = int(input())
costs = list(map(int, input().split()))
costs = deque(sorted(costs))
total_money = int(input())
per_money = total_money//len(costs)

answer = []
while True:
    if costs[0] <= per_money:
        city = costs.popleft()
        total_money -= city
        answer.append(city)
        if len(costs) == 0:
            break
        per_money = total_money//len(costs)
    else:
        break

if len(answer) == num:
    print(max(answer))
else:
    print(per_money)