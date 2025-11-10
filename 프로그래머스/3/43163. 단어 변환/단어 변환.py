from collections import deque
def solution(begin, target, words):
    keys = words.copy()
    keys.append(begin)
    trans = dict()
    for w in keys:
        trans[w] = []
    for w in keys:
        for key in trans.keys():
            count = 0
            for i in range(len(key)):
                if key[i] != w[i]:
                    count += 1
            if count == 1:
                trans[key].append(w)

    q = deque([[begin, 0]])
    visited = deque()
    answer = float('inf')
    while q:
        now, count = q.popleft()
        visited.append(now)
        for value in trans[now]:
            if value in visited:
                continue
            if value == target:
                answer = min(count+1, answer)
            else:
                q.append([value, count+1])
    if answer == float('inf'):
        answer = 0
    return answer