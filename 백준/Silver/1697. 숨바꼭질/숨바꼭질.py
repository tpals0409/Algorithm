from collections import deque
N, K = map(int, input().split())

count = 0

def find(N, K):
    queue = deque([(N, 0)])
    visited = set()

    while queue:
        pos, count = queue.popleft()
        if pos == K:
            return count

        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos <= 100000 and next_pos not in visited:
                visited.add(next_pos)
                queue.append((next_pos, count + 1))
    return -1

print(find(N, K))