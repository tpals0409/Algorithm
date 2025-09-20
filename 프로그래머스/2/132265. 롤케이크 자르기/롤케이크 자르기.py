def solution(topping):
    answer = 0
    r_dict = dict()
    for t in topping:
        if t in r_dict:
            r_dict[t] += 1
        else:
            r_dict[t] = 1
    r_count = len(r_dict)
    
    l_set = set()
    l_count = 0
    
    for t in topping:
        r_dict[t] -= 1
        if r_dict[t] <= 0:
            r_count -= 1
        if t not in l_set:
            l_set.add(t)
            l_count += 1
        if l_count == r_count:
            answer += 1
    return answer