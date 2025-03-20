import sys
input = sys.stdin.readline

N = int(input())
schedule = [0]*N
for i in range(N):
    schedule[i] = list(map(int, input().split()))

answer = []
def make_schedule(schedule, cost, day):
    if day == N:
        answer.append(cost)
        return
    else:
        make_schedule(schedule, cost, day+1)
        if day+schedule[day][0] <= N:
            make_schedule(schedule, cost+schedule[day][1], day+schedule[day][0])
        else:
            make_schedule(schedule, cost, N)

make_schedule(schedule, 0, 0)
print(max(answer))