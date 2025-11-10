import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    str = input().rstrip()
    K = int(input())
    min_value = float('inf')
    max_value = 0
    counter = defaultdict(list)
    for s in range(len(str)):
        counter[str[s]].append(s)
    for key in counter.keys():
        if len(counter[key]) >= K:
            for start in range(len(counter[key])-K+1):
                min_value = min(min_value, counter[key][start+K-1]-counter[key][start]+1)
                max_value = max(max_value, counter[key][start+K-1]-counter[key][start]+1)
    if max_value == 0:
        print(-1)
    else:
        print(min_value, max_value)
