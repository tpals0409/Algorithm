N = int(input())
line = [[0, 0] for _ in range(N)]
for i in range(N):
    S, E = map(int ,input().split())
    line[i] = [S, E]

line = sorted(line)
des = []
for s, e in line:
    des.append(e)

counter = [1 for _ in range(N)]

for i in range(N):
    for j in range(i, -1, -1):
        if des[i] > des[j]:
            counter[i] = max(counter[i], counter[j]+1)

print(N-max(counter))