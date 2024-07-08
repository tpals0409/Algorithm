import sys
input = sys.stdin.readline

N = int(input())

score = [0]*N

for i in range(N):
    kg, cm = map(int, input().split())
    score[i] = [kg, cm]

for j in range(N):
    tmp = score[j]
    count = 1
    for k in range(N):
        if j != k:
            if score[k][0] > tmp[0] and score[k][1] > tmp[1]:
                count += 1
    print(count, end=' ')