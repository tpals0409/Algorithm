from itertools import permutations
def solution(k, dungeons):
    answer = -1
    
    tmp = [x for x in range(len(dungeons))]
    tmp = list(permutations(tmp))
    for case in tmp:
        now = k
        count = 0
        for i in case:
            if now >= dungeons[i][0]:
                now -= dungeons[i][1]
                count += 1
            else:
                break
        answer = max(answer, count)
    return answer