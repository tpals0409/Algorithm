import heapq
import sys
input = sys.stdin.readline

"""
N <= 10^5
가장 작은 숫자 2개를 합치고 재 정렬을 반복?
반복 횟수는 N-1
"""
N = int(input())
cards = [0]*N
for i in range(N):
    cards[i] = int(input())

answer = 0
heapq.heapify(cards)
for i in range(N-1):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    tmp = a+b
    answer += tmp
    heapq.heappush(cards, tmp)

print(answer)