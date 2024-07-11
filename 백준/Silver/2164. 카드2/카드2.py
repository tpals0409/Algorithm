from collections import deque

N = int(input())
cards = deque(x for x in range(1, N+1))

while True:
    if len(cards) == 1:
        print(cards.popleft())
        break
    cards.popleft()
    cards.append(cards.popleft())