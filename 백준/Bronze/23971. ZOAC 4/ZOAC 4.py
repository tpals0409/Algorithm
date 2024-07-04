from math import ceil
H, W, N, M = map(int, input().split())

width = ceil(W/(M+1))
height = ceil(H/(N+1))

print(width*height)