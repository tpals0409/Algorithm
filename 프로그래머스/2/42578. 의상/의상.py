from collections import defaultdict
def solution(clothes):
    kind = defaultdict(int)
    for clothe, category in clothes:
        kind[category] += 1
    
    answer = 1
    
    for i in kind.keys():
        answer *= (kind[i]+1)
    
    answer -= 1
    return answer