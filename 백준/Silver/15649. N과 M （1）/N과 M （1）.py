from itertools import permutations
N, M = map(int, input().split())
num = [x for x in range(1, N+1)]
case = list(permutations(num, M))

for i in case:
    for j in i:
        print(j, end = " ")
    print()