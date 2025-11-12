T = int(input())
for _ in range(T):
    N = int(input())
    matrix = [[False for _ in range(N)] for _ in range(N)]
    move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    idx = 0
    y, x = 0, 0
    count = 1
    matrix[y][x] = count
    for i in range(N*N-1):
        ny, nx = y+move[idx][0], x+move[idx][1]
        if not(0<=ny<N and 0<=nx<N) or matrix[ny][nx]:
            idx = (idx+1)%4
            ny, nx = y+move[idx][0], x+move[idx][1]
        count += 1
        matrix[ny][nx] = count
        y, x = ny, nx
    print(f"#{_ + 1}")
    for j in range(N):
        for k in range(N):
            print(matrix[j][k], end=" ")
        print()