import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
links = [[] for _ in range(V+1)]
cost = [float('inf') for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    links[A].append([B, C])

q = []
heapq.heappush(q, [0, start])
cost[start] = 0

while q:
    w, node = heapq.heappop(q)
    for nxt, weight in links[node]:
        if cost[node] + weight < cost[nxt]:
            cost[nxt] = cost[node] + weight
            heapq.heappush(q, [cost[nxt], nxt])

for i in range(1, V+1):
    if cost[i] == float('inf'):
        print('INF')
    else:
        print(cost[i])