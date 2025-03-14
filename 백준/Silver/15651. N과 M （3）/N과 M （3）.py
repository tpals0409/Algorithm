N, M = map(int, input().split())
def make_numbers(start, arr):
    if len(arr) == M:
        print(*arr)
        return 0
    for i in range(start, N+1):
        make_numbers(1, arr+[i])

make_numbers(1, [])