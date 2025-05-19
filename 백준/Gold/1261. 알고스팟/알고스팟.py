import heapq
import sys
input = sys.stdin.readline


M, N = map(int, input().split())
matrix = [input().rstrip() for _ in range(N)]
min_value = [[float('inf') for _ in range(M)] for _ in range(N)]

min_value[0][0] = 0
q = [[0, [0, 0]]]

while q:
    w, xy = heapq.heappop(q)
    y, x = xy
    if x-1 >= 0:
        if min_value[y][x-1] > w+int(matrix[y][x-1]):
            min_value[y][x-1] = w+int(matrix[y][x-1])
            heapq.heappush(q, [min_value[y][x-1], [y, x-1]])
    if x+1 < M:
        if min_value[y][x+1] > w+int(matrix[y][x+1]):
            min_value[y][x+1] = w+int(matrix[y][x+1])
            heapq.heappush(q, [min_value[y][x+1], [y, x+1]])
    if y-1 >= 0:
        if min_value[y-1][x] > w+int(matrix[y-1][x]):
            min_value[y-1][x] = w+int(matrix[y-1][x])
            heapq.heappush(q, [min_value[y-1][x], [y-1, x]])
    if y+1 < N:
        if min_value[y+1][x] > w+int(matrix[y+1][x]):
            min_value[y+1][x] = w+int(matrix[y+1][x])
            heapq.heappush(q, [min_value[y+1][x], [y+1, x]])

print(min_value[-1][-1])