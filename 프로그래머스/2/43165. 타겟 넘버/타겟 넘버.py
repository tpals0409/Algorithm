def solution(numbers, target):
    answer = [[] for _ in range(len(numbers))]
    answer[0] = [-numbers[0], numbers[0]]
    for i in range(1, len(numbers)):
        for j in range(len(answer[i-1])):
            answer[i].append((answer[i-1][j]-numbers[i]))
            answer[i].append((answer[i-1][j]+numbers[i]))
    result = answer[-1].count(target)
    return result