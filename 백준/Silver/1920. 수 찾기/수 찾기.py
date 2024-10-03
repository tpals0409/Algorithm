pre_N = int(input())  # Number of elements in pre_list
pre_list = list(map(int, input().split()))  # Elements in pre_list
N = int(input())  # Number of elements in is_in
is_in = list(map(int, input().split()))  # Elements to check for presence

# Sort pre_list
pre_list = sorted(pre_list)

# Perform binary search for each element in is_in
for i in is_in:
    start = 0
    end = pre_N - 1  # Set end to pre_N - 1 because list indices are zero-based
    
    found = False
    while start <= end:
        mid = (start + end) // 2  # Recalculate the mid index
        if pre_list[mid] == i:  # If the element is found
            found = True
            break
        elif pre_list[mid] < i:  # If the element is greater than the mid, search the right half
            start = mid + 1
        else:  # If the element is less than the mid, search the left half
            end = mid - 1

    if found:
        print(1)
    else:
        print(0)
