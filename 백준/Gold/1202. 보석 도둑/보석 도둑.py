import heapq
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = [int(input()) for _ in range(K)]  # ✅ 수정된 부분

# 보석 무게 순 정렬
jewels.sort()
# 가방 무게 순 정렬
bags.sort()

heap = []
answer = 0
idx = 0

for c in bags:
    while idx < N and jewels[idx][0] <= c:
        heapq.heappush(heap, -jewels[idx][1])
        idx += 1
    if heap:
        answer += -heapq.heappop(heap)

print(answer)
