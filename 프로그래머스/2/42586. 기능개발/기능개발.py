from math import ceil
def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        progresses[i] = ceil((100-progresses[i])/speeds[i])
    for i in range(1, len(progresses)):
        progresses[i] = max(progresses[i], progresses[i-1])
    deploy = dict()
    for p in progresses:
        if p in deploy:
            deploy[p] += 1
        else:
            deploy[p] = 1
    answer = list(deploy.values())
    return answer