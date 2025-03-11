num = int(input())
checker_x = []
checker_y = []
checker = []
answer = [-1]*num

for _ in range(num):
    a, b = map(int, input().split())
    checker_x.append(a)
    checker_y.append(b)
    checker.append([a, b])

for y in checker_y:
    for x in checker_x:
        cost = []
        for cost_x, cost_y in checker:
            cost_per = abs(cost_x-x) + abs(cost_y-y)
            cost.append(cost_per)
        cost.sort()

        tmp = 0
        for i in range(len(cost)):
            c = cost[i]
            tmp += c
            if answer[i] == -1:
                answer[i] = tmp
            else:
                answer[i] = min(tmp, answer[i])

for _ in range(num):
    print(answer[_], end=" ")