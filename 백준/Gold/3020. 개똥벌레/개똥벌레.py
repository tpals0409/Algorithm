import sys
input = sys.stdin.readline

N, H = map(int, input().rstrip().split())

bottom = [0]*(H+1)
top = [0]*(H+1)

for i in range(N):
    height = int(input())
    if i%2 == 0:
        bottom[height] += 1
    else:
        top[H-height+1] += 1

for i in range(H-1, 0, -1):
    bottom[i] += bottom[i+1]
for i in range(1, H+1):
    top[i] += top[i-1]

answer = float('inf')
count = 1

for i in range(1, H+1):
    tmp = bottom[i]+top[i]
    if tmp < answer:
        answer = tmp
        count = 1
    elif tmp == answer:
        count += 1

print(answer, count)