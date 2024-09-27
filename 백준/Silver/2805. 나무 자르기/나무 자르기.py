def get_cut_wood(trees, height):
    total = 0
    for tree in trees:
        if tree > height:
            total += tree - height
    return total

def find_height(trees, M):
    low, high = 0, max(trees)

    while low <= high:
        mid = (low + high) // 2
        cut_wood = get_cut_wood(trees, mid)

        if cut_wood >= M:
            low = mid + 1
        else:
            high = mid - 1

    return high

N, M = map(int, input().split())
trees = list(map(int, input().split()))

result = find_height(trees, M)
print(result)