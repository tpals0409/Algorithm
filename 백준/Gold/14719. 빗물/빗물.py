h, w = map(int, input().split())
block = list(map(int, input().split()))

start = block[0]
std = block.index(max(block))
answer = 0
for i in range(std):
    if block[i] > start:
        start = block[i]
    else:
        answer += start-block[i]
start = block[-1]
for i in range(w-1, std, -1):
    if block[i] > start:
        start = block[i]
    else:
        answer += start-block[i]

print(answer)