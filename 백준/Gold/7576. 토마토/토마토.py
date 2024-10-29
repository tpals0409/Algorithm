from collections import deque
N, M = map(int, input().split())
tomato = [0]*M
is_ripe = deque()
for i in range(M):
    tomato[i] = list(map(int, input().split()))
    for j in range(N):
        if tomato[i][j] == 1:
            is_ripe.append([i, j])

# print(is_ripe)
count = 0
tmp_deque = deque()
while is_ripe:
    tmp_y, tmp_x = is_ripe.popleft()
    for i in range(4):
        if i == 0:
            try:
                if tomato[tmp_y + 1][tmp_x] == 0:
                    tomato[tmp_y + 1][tmp_x] = 1
                    tmp_deque.append([tmp_y + 1, tmp_x])
            except:
                continue
        elif i == 1 and tmp_y > 0:
            try:
                if tomato[tmp_y-1][tmp_x] == 0:
                    tomato[tmp_y-1][tmp_x] = 1
                    tmp_deque.append([tmp_y-1, tmp_x])
            except:
                continue
        elif i == 2:
            try:
                if tomato[tmp_y][tmp_x+1] == 0:
                    tomato[tmp_y][tmp_x+1] = 1
                    tmp_deque.append([tmp_y, tmp_x+1])
            except:
                continue
        elif i == 3 and tmp_x > 0:
            try:
                if tomato[tmp_y][tmp_x - 1] == 0:
                    tomato[tmp_y][tmp_x - 1] = 1
                    tmp_deque.append([tmp_y, tmp_x - 1])
            except:
                continue
    if len(is_ripe) == 0:
        count += 1
        is_ripe = tmp_deque
        tmp_deque = deque()

for i in range(M):
    if 0 in tomato[i]:
        print(-1)
        exit()

print(count-1)