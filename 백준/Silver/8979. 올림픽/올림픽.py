import sys
input = sys.stdin.readline

n, who = map(int, input().split())

record = [0]*n

for i in range(n):
    record[i] = list(map(int, input().split()))
    tmp = record[i].pop(0)
    record[i].append(tmp)

record = sorted(record, reverse=True)

start = 1
winner = record[0]
winner.append(1)
for j in range(1, n):
    if record[j][:3] == record[j-1][:3]:
        record[j].append(start)
    else:
        start = j+1
        record[j].append(start)


for k in record:
    if k[3] == who:
        print(k[-1])