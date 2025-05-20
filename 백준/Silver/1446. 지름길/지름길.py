import heapq
import sys
from collections import deque
input = sys.stdin.readline

N, D = map(int, input().split())
min_cost = [float('inf') for _ in range(D+1)]
road = [[[1, i+1]] for i in range(D)]
road.append([])
for _ in range(N):
    A, B, C = map(int, input().split())
    if B <= D:
        road[A].append([C, B])

q = []
heapq.heappush(q, [0, 0])
min_cost[0] = 0
while q:
    weight, x = heapq.heappop(q)
    for w, nxt in road[x]:
        if min_cost[nxt] > weight+w:
            min_cost[nxt] = weight+w
            heapq.heappush(q, [min_cost[nxt], nxt])

print(min_cost[-1])