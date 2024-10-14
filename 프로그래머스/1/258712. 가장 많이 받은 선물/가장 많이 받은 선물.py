def solution(friends, gifts):
    num = len(friends)
    answer = [0]*num
    matrix = [[0]*num for _ in range(num)]
    for give in gifts:
        A, B = give.split()
        matrix[friends.index(A)][friends.index(B)] += 1
    score_dict = [[0]*2 for _ in range(num)]
    for i in range(num):
        score_dict[i][0] = sum(matrix[i])
        for j in range(num):
            score_dict[j][1] += matrix[i][j]
    for i in range(num):
        for j in range(num):
            if matrix[i][j] > matrix[j][i]:
                answer[i] += 1
            elif matrix[i][j] == matrix[j][i]:
                if (score_dict[i][0]-score_dict[i][1]) > (score_dict[j][0]-score_dict[j][1]):
                    answer[i] += 1
    return max(answer)