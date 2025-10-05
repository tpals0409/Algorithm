import heapq
def solution(A, B):
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    while A:
        pA = heapq.heappop(A)
        while B:
            pB = heapq.heappop(B)
            if pB > pA:
                answer += 1
                break
    
    print(answer)
    return answer