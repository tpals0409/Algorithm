home_num, wifi_num = map(int, input().split())
home = sorted([int(input()) for x in range(home_num)])

def possible(home, distance, wifi_num):
    count = 1
    last = home[0]
    for h in home[1:]:
        if h - last >= distance:
            count += 1
            last = h
            if count >= wifi_num:
                return True
    return False

start = 1
end = home[-1] - home[0]
result = 0
while start <= end:
    mid = (start+end)//2
    can = possible(home, mid, wifi_num)
    if can:
        result = mid
        start = mid+1
    else:
        end = mid-1
print((start+end)//2)