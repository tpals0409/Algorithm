N, M = map(int, input().split())
case = list(map(int, input().split()))
case = sorted(case)
def make_numbers(arr):
    if len(arr) == M:
        print(" ".join(map(str, arr)))
        return 0
    for i in range(N):
        make_numbers(arr+[case[i]])

make_numbers([])