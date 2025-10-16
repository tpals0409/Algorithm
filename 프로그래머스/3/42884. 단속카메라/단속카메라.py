"""
-20 -15
-20 -15     -14 -5
-18 -15     -5 -5
"""
from collections import deque
def solution(routes):
    answer = 1
    routes = sorted(routes)
    for i in range(1, len(routes)):
        if routes[i][0] <= routes[i-1][1]:
            routes[i][1] = min(routes[i][1], routes[i-1][1])
        else:
            answer+= 1
    return answer