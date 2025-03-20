import sys
input = sys.stdin.readline
N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]

undo_cost = cost[0]
for i in range(1, N):
    tmp = [0, 0, 0]
    tmp[0] = min(cost[i][0]+undo_cost[1], cost[i][0]+undo_cost[2])
    tmp[1] = min(cost[i][1]+undo_cost[0], cost[i][1]+undo_cost[2])
    tmp[2] = min(cost[i][2]+undo_cost[0], cost[i][2]+undo_cost[1])
    undo_cost = tmp
print(min(undo_cost))