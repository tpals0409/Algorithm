from itertools import combinations
N = int(input())
materials = [0]*N
for i in range(N):
    materials[i] = list(map(int, input().split()))

answer = float('inf')
for i in range(1, N+1):
    comb = list(combinations(materials, i))
    for j in range(len(comb)):
        tmp_sour = 1
        tmp_bitter = 0
        for sour, bitter in comb[j]:
            tmp_sour *= sour
            tmp_bitter += bitter
        if abs(tmp_sour-tmp_bitter) < answer:
            answer = abs(tmp_sour-tmp_bitter)

print(answer)