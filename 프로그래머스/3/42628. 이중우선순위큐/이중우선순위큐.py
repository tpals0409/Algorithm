import heapq
from collections import Counter

def solution(operations):
    min_heap = []
    max_heap = []
    counter = Counter()
    
    for op in operations:
        cmd, value = op.split()
        value = int(value)
        
        if cmd == 'I':
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            counter[value] += 1
        
        elif cmd == 'D':
            if sum(counter.values()) == 0:
                continue
            
            if value == 1:
                while max_heap and counter[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    counter[max_val] -= 1
            
            else:
                while min_heap and counter[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    counter[min_val] -= 1
    
    while min_heap and counter[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and counter[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap or sum(counter.values()) == 0:
        return [0, 0]
    
    return [-max_heap[0], min_heap[0]]