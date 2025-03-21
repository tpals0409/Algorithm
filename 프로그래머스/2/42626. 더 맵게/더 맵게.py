import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while (len(scoville) > 1):
        now = heapq.heappop(scoville)
        if (now >= K):
            heapq.heappush(scoville, now)
            break
        else:
            sec = heapq.heappop(scoville)
            heapq.heappush(scoville, now+(2*sec))
            answer += 1
    min_scoville = heapq.heappop(scoville)

    if min_scoville < K:
        answer = -1

    return answer