"""
초기 n의 카드에서 3분의 1의 카드를 뽑는다
라운드 시작:
1. 카드 2개 뽑기 만약 카트가 없다면 게임 종료(동전 소모: 카드 가지기, 소모x: 카드 버리기)
2. 카드의 합이 n+1이 되도록 카드 두장을 낼 수 있음(못내면 종료)

동전소모를 효율적으로 해야함.
현재 가지고 있는 패로 만들수 있을 경우는 무조건 쓰는것이 맞음
"""
from collections import deque
def solution(coin, cards):
    goal = len(cards)+1
    cost_zero = 0
    cost_one = 0
    cost_two = 0
    
    answer = 0
    cards = deque(cards)
    my_cards = deque()
    waste = deque()
    
    for i in range(len(cards)//3):
        tmp = cards.popleft()
        my_cards.append(tmp)
        if (goal-tmp) in my_cards:
            cost_zero += 1
    while True:
        answer += 1
        if not cards:
            break
        A = cards.popleft()
        if (goal-A) in my_cards:
            cost_one += 1
        elif (goal-A) in waste:
            cost_two += 1
        else:
            waste.append(A)
        B = cards.popleft()
        if (goal-B) in my_cards:
            cost_one += 1
        elif (goal-B) in waste:
            cost_two += 1
        else:
            waste.append(B)
        
        if cost_zero > 0:
            cost_zero -= 1
        elif (cost_one > 0) and (coin > 0):
            cost_one -= 1
            coin -= 1
        elif (cost_two > 0) and (coin > 1):
            cost_two -= 1
            coin -= 2
        else:
            break
    return answer