from collections import defaultdict, deque
def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for start, end in roads:
        graph[start].append(end)
        graph[end].append(start)
    
    distance = [-1] * (n + 1)
    distance[destination] = 0
    
    queue = deque([destination])
    
    while queue:
        current = queue.popleft()
        for n in graph[current]:
            if distance[n] == -1:
                distance[n] = distance[current] + 1
                queue.append(n)
                
    answer = [distance[source] for source in sources]
    return answer