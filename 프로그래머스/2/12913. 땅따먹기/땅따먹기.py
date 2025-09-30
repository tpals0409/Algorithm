def solution(land):
    undo = -1
    for i in range(1, len(land)):
        for j in range(4):
            tmp = land[i-1].copy()
            tmp[j] = 0
            land[i][j] = land[i][j]+max(tmp)
    answer = max(land[-1])
    return answer