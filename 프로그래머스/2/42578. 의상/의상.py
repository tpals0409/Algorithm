def solution(clothes):
    answer = 1
    comb = dict()
    for what, kind in clothes:
        if kind in comb:
            comb[kind] += 1
        else:
            comb[kind] = 1
    for i in comb:
        answer *= (comb[i]+1)
    return answer-1