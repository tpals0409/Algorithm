import math
H, W, N, K = map(int, input().split())

can_y = math.ceil(H/(N+1))
can_x = math.ceil(W/(K+1))

print(can_y*can_x)