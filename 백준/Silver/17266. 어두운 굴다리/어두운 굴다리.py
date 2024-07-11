from math import ceil

length = int(input())
num = int(input())
loc = list(map(int, input().split()))

first, last = loc[0], length - loc[-1]
heights = [first, last]

for i in range(1, len(loc)):
    heights.append(ceil((loc[i] - loc[i-1])/2))

print(max(heights))
