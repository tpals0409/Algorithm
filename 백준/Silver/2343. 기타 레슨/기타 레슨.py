N, M = map(int, input().split())
video = list(map(int, input().split()))
start = max(video)
end = sum(video)

while start <= end:
    mid = (start+end)//2
    count = 1
    tmp = 0
    for i in video:
        if (tmp+i) > mid:
            count += 1
            tmp = i
        else:
            tmp += i
    if count > M:
        start = mid+1
    else:
        end = mid-1

print(start)