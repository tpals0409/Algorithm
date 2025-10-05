import heapq
def solution(n, works):
    works = [-x for x in works]
    heapq.heapify(works)
    for i in range(n):
        tmp = heapq.heappop(works)
        tmp = min(0, tmp+1)
        heapq.heappush(works, tmp)
    works = [(x*x) for x in works]
    answer = sum(works)
    return answer