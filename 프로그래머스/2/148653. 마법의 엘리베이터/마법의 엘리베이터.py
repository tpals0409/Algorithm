def solution(storey):
    up = [10, 9, 8, 7, 6]
    storey = list(str(storey))
    storey = reversed(storey)
    storey = list(map(int, storey))
    
    answer = 0
    for i in range(len(storey)-1):
        if storey[i] in up:
            answer += (10 - storey[i])
            storey[i+1] += 1
        elif storey[i] == 5:
            if storey[i+1] > 4:
                answer += (10 - storey[i])
                storey[i+1] += 1
            else:
                answer += storey[i]
        else:
            answer += storey[i]
    final = storey[-1]
    
    if final in up:
        final = 10-final+1
    
    answer += final
    return answer