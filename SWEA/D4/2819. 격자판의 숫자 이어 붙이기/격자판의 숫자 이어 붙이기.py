T = int(input())
for _ in range(T):
    matrix = [[] for line in range(4)]
    for i in range(4):
        matrix[i] = list(map(int, input().split()))

    move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    answer = set()
    def dfs(y, x, count, number):
        if count >= 7:
            answer.add(number)
            return 0
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if (0<=ny<4) and (0<=nx<4):
                dfs(ny, nx, count+1, number+str(matrix[ny][nx]))
        return 0

    for i in range(4):
        for j in range(4):
            dfs(i, j, 1, str(matrix[i][j]))
    print(f"#{_+1} {len(answer)}")