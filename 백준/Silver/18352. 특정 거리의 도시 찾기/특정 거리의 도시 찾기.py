import heapq
import sys
input = sys.stdin.readline


N, M, K, X = map(int, input().split())
nodes = [float('inf') for _ in range(N+1)]
matrix = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    matrix[A].append([1, B])

q = []
nodes[X] = 0
heapq.heappush(q, [0, X])

while q:
    w, n = heapq.heappop(q)
    for weight, nxt in matrix[n]:
        if nodes[nxt] > w+weight:
            nodes[nxt] = w+weight
            heapq.heappush(q, [nodes[nxt], nxt])

answer = []
for i in range(1, N+1):
    if nodes[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for n in answer:
        print(n)