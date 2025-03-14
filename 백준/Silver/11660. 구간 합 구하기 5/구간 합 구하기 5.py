N, M = map(int, input().split())
matrix = [[0 for _ in range(N+1)] for a in range(N+1)]
for i in range(1, N+1):
    tmp = list(map(int, input().split()))
    input_tmp = 0
    if i == 1:
        for j in range(1, N+1):
            input_tmp += tmp[j-1]
            matrix[i][j] = input_tmp
    else:
        input_tmp = 0
        for j in range(1, N+1):
            input_tmp += tmp[j-1]
            matrix[i][j] = input_tmp + matrix[i-1][j]

for i in range(M):
    a, b, c, d = map(int, input().split())
    try:
        answer = matrix[c][d] - matrix[c][b-1] - matrix[a-1][d] + matrix[a-1][b-1]
    except:
        continue
    print(answer)