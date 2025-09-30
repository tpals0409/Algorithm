
from collections import deque

def solution(order):
    answer = 0
    
    # 메인 컨베이어 벨트 (1부터 n까지 순서대로)
    belt = deque(range(1, len(order) + 1))
    
    # 보조 컨베이어 벨트 (스택)
    sub = []
    
    # order를 deque로 변환
    order = deque(order)
    
    while order:
        target = order[0]  # 현재 실어야 할 상자 번호
        
        # 1. 보조 컨베이어 맨 위에 원하는 상자가 있는 경우
        if sub and sub[-1] == target:
            sub.pop()
            order.popleft()
            answer += 1
        
        # 2. 메인 컨베이어에 상자가 남아있는 경우
        elif belt:
            box = belt.popleft()
            
            # 2-1. 원하는 상자면 바로 트럭에 실음
            if box == target:
                order.popleft()
                answer += 1
            
            # 2-2. 원하는 상자가 아니면 보조 컨베이어에 보관
            else:
                sub.append(box)
        
        # 3. 메인 컨베이어도 비고, 보조 컨베이어에도 원하는 상자 없음
        else:
            break
    
    return answer