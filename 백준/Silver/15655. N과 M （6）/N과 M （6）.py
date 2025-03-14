N, M = map(int, input().split())
case = list(map(int, input().split()))
case = sorted(case)
def make_numbers(start, arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return 0
    for i in range(start, N):
        if case[i] in arr:
            continue
        make_numbers(i+1, arr+[case[i]])

make_numbers(0, [])