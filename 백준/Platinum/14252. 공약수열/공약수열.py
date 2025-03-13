from math import gcd

n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
answer = 0
std = 1
while len(numbers)>1:
    if gcd(numbers[std-1], numbers[std]) != 1:
        find = False
        for i in range(numbers[std-1]+1, numbers[std]):
            if (gcd(numbers[std-1], i) == 1) and (gcd(numbers[std], i) == 1):
                answer += 1
                find = True
                break
        if find == False:
            answer += 2
    std += 1
    if std == len(numbers):
        break
print(answer)