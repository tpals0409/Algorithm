import sys
input = sys.stdin.readline

city = int(input())
road = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = 0
now = cost[0]
standard = 1
for i in range(len(road)):
    if now > cost[standard]:
        answer += now * road[i]
        now = cost[standard]
        standard += 1
    else:
        answer += now * road[i]
        standard += 1
print(answer)