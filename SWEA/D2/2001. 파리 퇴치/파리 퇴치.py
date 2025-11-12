T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    matrix = [[] for _ in range(N)]
    row = [[0 for _ in range(N-M+1)] for _ in range(N)]
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
        tmp = sum(matrix[i][:M])
        row[i][0] = tmp
        for j in range(N-M):
            tmp -= matrix[i][j]
            tmp += matrix[i][j+M]
            row[i][j+1] = tmp
    column = [[0 for _ in range(N-M+1)] for _ in range(N-M+1)]
    for i in range(len(row[0])):
        tmp = 0
        for j in range(M):
            tmp += row[j][i]
        column[0][i] = tmp
        for j in range(N-M):
            tmp -= row[j][i]
            tmp += row[j+M][i]
            column[j+1][i] = tmp

    answer = 0
    for i in range(len(column)):
        answer = max(max(column[i]), answer)
    print(f"#{_+1} {answer}")