def solution(stones, k):
    def can_cross(num):
        count = 0
        for i in range(len(stones)):
            if stones[i] < num:
                count += 1
            else:
                count = 0
            if count >= k:
                return False
        return True
    
    answer = 0
    
    left = 0
    right = max(stones)+k
    
    while left <= right:
        mid = (left+right)//2
        if can_cross(mid):
            answer = mid
            left = mid+1
        else:
            right = mid-1
    return answer