from collections import deque
import heapq
import sys
input = sys.stdin.readline


N, E = map(int, input().split())
nodes = [float('inf') for _ in range(N+1)]
matrix = [[] for _ in range(N+1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    matrix[A].append([B, C])
    matrix[B].append([A, C])

def dijkstra(start, end):
    dist = [float('inf') for _ in range(N+1)]
    dist[start] = 0
    q = []
    heapq.heappush(q, [0, start])
    while q:
        cost, node = heapq.heappop(q)
        if cost > dist[node]:
            continue
        for nxt, w in matrix[node]:
            nd = cost+w
            if dist[nxt] > nd:
                dist[nxt] = nd
                heapq.heappush(q, [nd, nxt])
    return dist[end]

mustA, mustB = map(int, input().split())
firstA = dijkstra(1, mustA)
firstB = dijkstra(1, mustB)
bridge = dijkstra(mustA, mustB)
endA = dijkstra(mustB, N)
endB = dijkstra(mustA, N)

answer = min((firstA+bridge+endA), (firstB+bridge+endB))
if answer != float('inf'):
    print(answer)
else:
    print(-1)