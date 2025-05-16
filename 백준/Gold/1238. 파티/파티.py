import heapq
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())
student = [float('inf') for _ in range(N+1)]
answer = [0 for _ in range(N+1)]
road = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    road[A].append([C, B])

for i in range(1, N+1):
    q = []
    case = student.copy()
    heapq.heappush(q, [0, i])
    case[i] = 0
    while q:
        weight, node = heapq.heappop(q)
        for w, nxt in road[node]:
            if case[node] + w < case[nxt]:
                case[nxt] = case[node] + w
                q.append([case[nxt], nxt])
    answer[i] += case[X]


q = []
case = student.copy()
heapq.heappush(q, [0, X])
case[X] = 0
while q:
    weight, node = heapq.heappop(q)
    if weight > case[node]:
        continue
    for w, nxt in road[node]:
        if case[node] + w < case[nxt]:
            case[nxt] = case[node] + w
            q.append([case[nxt], nxt])

for i in range(1, N+1):
    answer[i] += case[i]

print(max(answer))