from math import ceil
def solution(n, stations, w):
    answer = 0
    start = 1
    end = n
    rest = []
    for st in stations:
        tmp = (st-w)-start
        rest.append(tmp)
        start = st+w+1
    rest.append(max(end-start+1, 0))
    
    for r in rest:
        answer += ceil(r/(w*2+1))
    return answer