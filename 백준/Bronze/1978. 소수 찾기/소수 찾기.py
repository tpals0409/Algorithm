def is_prime(num):
    if num == 1:
        return False
    tmp = int(num**0.5)
    for i in range(2, tmp+1):
        if num%i == 0:
            return False
    return True

num = int(input())
prime = list(map(int, input().split()))
answer = 0
for n in prime:
    if is_prime(n):
        answer += 1

print(answer)