from collections import deque
def solution(s):
    answer = []
    tuples = deque()
    
    tmp = ""
    state = False
    for i in range(1, len(s)-1):
        if s[i] == '{':
            state = True
            continue
        elif s[i] == '}':
            state = False
            tuples.append(list(map(int, tmp.split(','))))
            tmp = ""
            continue
        if state == True:
            tmp += s[i]
    tuples = deque(sorted(tuples, key= lambda x: (len(x))))
    while tuples:
        t = tuples.popleft()
        for n in t:
            if n in answer:
                continue
            else:
                answer.append(n)
    return answer