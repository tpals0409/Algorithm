import sys
input = sys.stdin.readline

numbers = input().rstrip()
start = 1
idx = 0
while True:
    if numbers[idx] in str(start):
        for i in str(start):
            if i == numbers[idx]:
                idx += 1
            if idx >= len(numbers):
                break
        start += 1
    else:
        start += 1
    if idx >= len(numbers):
        break

print(start-1)