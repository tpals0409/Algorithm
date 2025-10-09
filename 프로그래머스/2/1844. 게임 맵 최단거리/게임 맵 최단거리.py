from collections import deque
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[False for i in range(len(maps[0]))] for i in range(len(maps))]
    q = deque([[0, 0, 1]])
    visited[0][0] = True
    while q:
        y, x, dist = q.popleft()
        move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        if y == n - 1 and x == m - 1:
            return dist
        else:
            for dy, dx in move:
                ny, nx = y+dy, x+dx
                if (0<=ny<len(maps)) and (0<=nx<len(maps[0])):
                    if maps[ny][nx] == 1 and visited[ny][nx] == False:
                        visited[ny][nx] = True
                        q.append([ny, nx, dist+1])
    return -1