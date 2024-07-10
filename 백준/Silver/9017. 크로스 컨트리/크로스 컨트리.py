import sys
input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    number = int(input())
    team = list(map(int, input().split()))
    six_people = dict()
    for j in team:
        if j not in six_people:
            six_people[j] = 1
        else:
            six_people[j] += 1

    score = []
    start = 1
    for k in range(number):
        if six_people[team[k]] == 6:
            score.append([start, team[k]])
            start += 1

    winner = dict()

    for p in score:
        if p[1] not in winner:
            winner[p[1]] = [p[0]]
        else:
            winner[p[1]].append(p[0])

    for q in winner.keys():
        winner[q] = [sum(winner[q][0:4]), winner[q][4]]

    answer = []

    for r in winner.keys():
        answer.append([winner[r][0], winner[r][1], r])

    answer = sorted(answer, key=lambda x:x[0:2])

    print(answer[0][-1])