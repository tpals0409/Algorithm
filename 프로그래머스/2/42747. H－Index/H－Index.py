def solution(citations):
    answer = 0
    citations = sorted(citations)
    left = 0
    right = citations[-1]
    
    while left <= right:
        mid = (left+right)//2
        up = 0
        for i in range(len(citations)-1, -1, -1):
            if citations[i] >= mid:
                up += 1
            else:
                break
        down = 0
        for i in range(len(citations)):
            if citations[i] < mid:
                down += 1
            else:
                break
        if up >= mid and down <= mid:
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer