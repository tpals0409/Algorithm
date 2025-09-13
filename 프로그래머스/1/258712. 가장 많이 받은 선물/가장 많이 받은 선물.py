def solution(friends, gifts):
    answer = [0 for i in range(len(friends))]
    
    match = dict()
    for i in range(len(friends)):
        match[friends[i]] = i
    
    matrix = [[0 for i in range(len(friends)+1)] for i in range(len(friends))]
    for tmp in gifts:
        S, E = tmp.split()
        S = match[S]
        E = match[E]
        matrix[S][E] += 1
        matrix[S][-1] += 1
        matrix[E][-1] -= 1
    
    for i in range(len(friends)):
        tmp = 0
        for j in range(len(friends)):
            if matrix[i][j] > matrix[j][i]:
                tmp += 1
            elif matrix[i][j] == matrix[j][i]:
                if matrix[i][-1] > matrix[j][-1]:
                    tmp += 1
        answer[i] = tmp

    return max(answer)