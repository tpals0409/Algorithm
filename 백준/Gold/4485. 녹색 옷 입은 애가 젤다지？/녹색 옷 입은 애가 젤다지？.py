import heapq
import sys
input = sys.stdin.readline

def dijstra(matrix, min_cost):
    q = []
    min_cost[0][0] = matrix[0][0]
    heapq.heappush(q, [min_cost[0][0], [0, 0]])
    while q:
        cost, xy = heapq.heappop(q)
        y, x = xy
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nxt_y, nxt_x = y+dy, x+dx
            if (0 <= nxt_y < len(matrix)) and (0 <= nxt_x < len(matrix)):
                if min_cost[nxt_y][nxt_x] > cost+matrix[nxt_y][nxt_x]:
                    min_cost[nxt_y][nxt_x] = cost+matrix[nxt_y][nxt_x]
                    heapq.heappush(q, [min_cost[nxt_y][nxt_x], [nxt_y, nxt_x]])
    return min_cost[-1][-1]

cnt = 0
while True:
    N = int(input())
    if N == 0:
        break
    cnt += 1
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_cost = [[float('inf') for _ in range(N)] for _ in range(N)]
    answer = dijstra(matrix, min_cost)
    print(f"Problem {cnt}: {answer}")