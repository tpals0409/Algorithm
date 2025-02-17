N, L = map(int, input().split())
answer = []
add = 0
while True:
    std = [_ for _ in range(L)]
    tmp = sum(std)
    if N-tmp >= 0:
        if (N-tmp)%L == 0:
            answer = std
            add = (N-tmp)//L
            break
        else:
            L += 1
            if L > 100:
                break
    else:
        break

if len(answer) > 0:
    for _ in answer:
        print(_+add, end=' ')
else:
    print(-1)