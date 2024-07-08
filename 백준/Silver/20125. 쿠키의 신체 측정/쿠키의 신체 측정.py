import sys
input = sys.stdin.readline

N = int(input())
answer = []
for i in range(N):
    row = input().rstrip()
    tmp = []
    for i in range(N):
        if row[i] == '*':
            tmp.append(i)
    answer.append(tmp)

#find head
head = 0
start = 0
for j in range(N):
    if len(answer[j]) > 0:
        head = answer[j][0]
        start = j
        break
start += 1
heart_x, heart_y = head+1, start+1

#find hand
left_hand = head - answer[start][0]
right_hand = answer[start][-1] - head
start += 1

#find waist
waist = 0
for k in range(start, N):
    if head in answer[k]:
        waist += 1
start += waist

#find leg
left_leg = 0
right_leg = 0
for p in range(start, N):
    if head-1 in answer[p]:
        left_leg += 1
    if head+1 in answer[p]:
        right_leg += 1

print(heart_y, heart_x)
print(left_hand, right_hand, waist, left_leg, right_leg)