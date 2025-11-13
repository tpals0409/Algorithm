import heapq

T = 10
for _ in range(T):
    num = int(input())
    heights = list(map(int, input().split()))
    minus_heights = list([-heights[i], i] for i in range(len(heights)))
    plus_heights = list([heights[i], i] for i in range(len(heights)))
    heapq.heapify(plus_heights)
    heapq.heapify(minus_heights)
    answer = float('inf')
    for i in range(num+1):
        while plus_heights and plus_heights[0][0] != heights[plus_heights[0][1]]:
            heapq.heappop(plus_heights)
        min_value = plus_heights[0][0]
        min_idx = plus_heights[0][1]

        while minus_heights and -minus_heights[0][0] != heights[minus_heights[0][1]]:
            heapq.heappop(minus_heights)
        max_value = -minus_heights[0][0]
        max_idx = minus_heights[0][1]

        answer = min(answer, max_value-min_value)
        heights[min_idx] += 1
        heights[max_idx] -= 1

        heapq.heappush(plus_heights, [heights[min_idx], min_idx])
        heapq.heappush(minus_heights, [-heights[max_idx], max_idx])

        if answer in [0, 1]:
            break
    print(f"#{_+1} {answer}")