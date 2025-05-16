from collections import deque
import heapq
import sys
input = sys.stdin.readline

subin, sister = map(int, input().split())

cost = 0
street = [float('inf') for _ in range(100001)]

street[subin] = 0
q = deque([[subin, 0]])

while q:
    now, cost = q.popleft()
    # 걷기
    for nxt in (now-1, now+1):
        if 0 <= nxt <= 100000 and street[nxt] > cost + 1:
            street[nxt] = cost + 1
            q.append((nxt, cost+1))
    # 순간이동
    nxt = now*2
    if nxt <= 100000 and street[nxt] > cost:
        street[nxt] = cost
        q.appendleft((nxt, cost))

print(street[sister])