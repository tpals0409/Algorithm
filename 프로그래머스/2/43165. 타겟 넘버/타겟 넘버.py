from collections import deque
def solution(numbers, target):
    answer = 0
    num = deque([0])
    length = len(numbers)
    numbers = deque(numbers)
    while numbers:
        n = numbers.popleft()
        case = deque()
        while num:
            tmp = num.popleft()
            case.append(tmp+n)
            case.append(tmp-n)
        num = case
    
    while case:
        ans = case.popleft()
        if ans == target:
            answer += 1
            
    return answer