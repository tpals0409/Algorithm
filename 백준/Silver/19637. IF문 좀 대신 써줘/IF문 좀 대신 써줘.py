import sys
input = sys.stdin.readline

level_number, input_number = map(int, input().split())
levels = [0]*(level_number+1)
levels[0] = ['no', -1]
for i in range(1, level_number+1):
    level, strength = input().rstrip().split()
    strength = int(strength)
    levels[i] = [level, strength]

def judge(levels, strength, start, end):
    mid = (start+end)//2
    if strength <= levels[mid][1]:
        if strength > levels[mid-1][1]:
            print(levels[mid][0])
        else:
            end = mid
            judge(levels, strength, start, end)
    else:
        start = mid
        judge(levels, strength, start, end)

for j in range(input_number):
    strength = int(input())
    judge(levels, strength, 0, level_number+1)