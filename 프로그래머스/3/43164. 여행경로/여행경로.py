from collections import deque, defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, end in sorted(tickets, reverse = True):
        graph[start].append(end)
    
    def dfs(airport):
        while graph[airport]:
            next_airport = graph[airport].pop()
            dfs(next_airport)
        answer.append(airport)
    dfs('ICN')
    return answer[::-1]