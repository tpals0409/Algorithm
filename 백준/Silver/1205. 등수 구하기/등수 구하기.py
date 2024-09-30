default, teo_score, rank_length = map(int, input().split())
rank = [-1]*rank_length
if default > 0:
    tmp = list(map(int, input().split()))
    for i in range(default):
        rank[i] = tmp[i]

if len(rank) < rank_length:
    for i in range(rank_length-len(rank)):
        rank.append(0)

if teo_score <= rank[-1]:
    print(-1)
else:
    teo_rank = 0
    for score in rank:
        if score > teo_score:
            teo_rank += 1
        else:
            break
    print(teo_rank+1)