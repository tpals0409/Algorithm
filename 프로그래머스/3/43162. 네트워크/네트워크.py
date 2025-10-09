from collections import deque
def solution(n, computers):
    answer = 0
    q = deque()
    visited = [False for i in range(len(computers))]
    q.append(0)
    visited[0] = True
    kind = deque([x for x in range(len(computers))])
    
    found = set()
    count = 0
    while kind:
        start = kind.popleft()
        if start in found:
            continue
        count += 1
        q.append(start)
        while q:
            com = q.popleft()
            for i in range(len(computers[com])):
                if i == com:
                    continue
                else:
                    if (computers[com][i] == 1) and (visited[i] == False):
                        visited[i] = True
                        q.append(i)
                        found.add(i)
    return count