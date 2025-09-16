"""
8 -> 1000
"""
from math import ceil
from collections import deque
def solution(n, k):
    trance = deque()
    while n != 0:
        tmp = n%k
        n = n//k
        trance.appendleft(tmp)
    answer = -1
    nums = []
    tmp = ''
    while trance:
        pop = trance.popleft()
        if pop == 0:
            if tmp == '':
                continue
            else:
                nums.append(int(tmp))
                tmp = ''
        else:
            tmp += str(pop)
    if len(tmp) != 0:
        nums.append(int(tmp))
    
    counter = 0
    for n in nums:
        tmp = is_prime(n)
        if tmp != -1:
            counter += 1
    return counter

def is_prime(n):
    tmp = ceil(n**0.5)
    if n == 2:
        return n
    elif n == 1:
        return -1
    else:
        for i in range(3, tmp+1):
            if n%i == 0:
                return -1
        return n