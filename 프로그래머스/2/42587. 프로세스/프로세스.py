"""
1   1911
11  911
911 11

"""
from collections import deque
def solution(priorities, location):
    answer = 0
    std = deque(sorted(priorities, reverse = True))
    for i in range(len(priorities)):
        priorities[i] = [priorities[i], i]
    priorities = deque(priorities)
    left = deque()
    while std:
        now = std.popleft()
        tmp = priorities.popleft()
        if tmp[0] == now:
            left.append(tmp)
        else:
            priorities.append(tmp)
            std.appendleft(now)
    for i in range(len(left)):
        if left[i][-1] == location:
            answer = i+1
            break
    return answer