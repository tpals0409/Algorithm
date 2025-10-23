from collections import defaultdict
def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for start, end in sorted(tickets, reverse = True):
        graph[start].append(end)
    
    def dfs(now):
        while graph[now]:
            nxt = graph[now].pop()
            dfs(nxt)
        answer.append(now)
    dfs('ICN')
    return answer[::-1]