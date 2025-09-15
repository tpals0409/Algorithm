from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    sum_1 = sum(queue1)
    
    queue2 = deque(queue2)
    sum_2 = sum(queue2)
    goal = (sum(queue1)+sum(queue2))//2
    max_value = len(queue1)*3
    while answer < max_value:
        if sum_1 > sum_2:
            tmp = queue1.popleft()
            sum_1 -= tmp
            queue2.append(tmp)
            sum_2 += tmp
            answer += 1
        elif sum_1 < sum_2:
            tmp = queue2.popleft()
            sum_2 -= tmp
            queue1.append(tmp)
            sum_1 += tmp
            answer += 1
        else:
            break
        if answer+1 > max_value:
            answer = -1
            break
    return answer