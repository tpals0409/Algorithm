num = int(input())
block = []
for i in range(num):
    l, h = map(int, input().split())
    block.append([l, h])

block.sort(key= lambda x: x[0])
start = block[0][0]
width = block[-1][0] - block[0][0]

location = [0]*(width+1)
for i in range(num):
    location[block[i][0]-start] = block[i][1]

std = location.index(max(location))
answer = 0
temp = 0
for i in range(std):
    if location[i] > temp:
        temp = location[i]
    answer += temp

temp = 0
for i in range(len(location)-1, std, -1):
    if location[i] > temp:
        temp = location[i]
    answer += temp

answer += location[std]
print(answer)