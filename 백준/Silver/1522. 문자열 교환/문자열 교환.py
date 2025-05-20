import sys
input = sys.stdin.readline

ab = list(input().rstrip())
num = ab.count('a')
ab = ab+ab
answer = float('inf')
for i in range(len(ab)-num):
    tmp = ab[i:i+num].count('b')
    if answer > tmp:
        answer = tmp

print(answer)