pre_N = int(input())
pre_list = list(map(int, input().split()))
N = int(input())
is_in = list(map(int, input().split()))

pre_list = sorted(pre_list)
for i in is_in:
    start = 0
    end = pre_N-1
    found = False
    while (start<=end):
        mid = (end+start)//2
        if i == pre_list[mid]:
            found = True
            break
        elif i > pre_list[mid]:
            start = mid+1
        elif i < pre_list[mid]:
            end = mid-1
    if found:
        print(1)
    else:
        print(0)
