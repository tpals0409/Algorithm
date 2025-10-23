from collections import deque
def solution(maps):
    answer = 0
    len_y = len(maps)
    len_x = len(maps[0])
    
    visited = [[False for i in range(len_x)] for i in range(len_y)]
    visited[0][0] = True
    q = deque([[0, 0, 1]])
    while q:
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        y, x, count = q.popleft()
        if (y == len_y-1) and (x == len_x-1):
            return count
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if (0<=ny<len_y) and (0<=nx<len_x):
                if not (visited[ny][nx]) and (maps[ny][nx] == 1):
                    visited[ny][nx] = True
                    q.append([ny, nx, count+1])
            
    return -1