import heapq
def solution(n, s):
    answer = []
    div = s//n
    mod = s%n
    answer = [div for i in range(n)]
    heapq.heapify(answer)
    for i in range(mod):
        tmp = heapq.heappop(answer)
        tmp += 1
        heapq.heappush(answer, tmp)
    
    tmp = heapq.heappop(answer)
    if tmp == 0:
        answer = [-1]
    else:
        heapq.heappush(answer, tmp)
        answer = sorted(answer)
    return answer