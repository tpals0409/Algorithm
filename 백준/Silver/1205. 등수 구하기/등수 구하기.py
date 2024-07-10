import sys
input = sys.stdin.readline

N, tesu_score, max_rank = map(int, input().split())

ranking = list(map(int, input().split()))

for i in range(max_rank-N):
    ranking.append(-1)

start = 1

for j in range(max_rank):
    if ranking[j] > tesu_score:
        start += 1
    if j == max_rank-1:
        if tesu_score == ranking[j]:
            start = max_rank+1

if start > max_rank:
    print(-1)
else:
    print(start)