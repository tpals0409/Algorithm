import sys
from collections import deque
input = sys.stdin.readline

from collections import defaultdict
N = int(input())
graph = defaultdict(list)
for _ in range(N-1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

answer = defaultdict(int)
q = deque([1])
visited = [False for _ in range(N+1)]
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if not visited[nxt]:
            visited[nxt] = True
            answer[nxt] = now
            q.append(nxt)

for i in range(2, N+1):
    print(answer[i])