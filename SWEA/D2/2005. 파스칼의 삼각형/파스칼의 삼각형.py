T = int(input())
def paschal(n):
    tmp = [1 for _ in range(len(n)+1)]
    for i in range(1, len(n)):
        tmp[i] = n[i-1]+n[i]
    return tmp
for _ in range(T):
    N = int(input())
    answer = [[1]]
    for i in range(1, N):
        answer.append(paschal(answer[i-1]))
    print(f"#{_+1}")
    for i in range(N):
        for j in answer[i]:
            print(j, end=" ")
        print()