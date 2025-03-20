import sys
input = sys.stdin.readline

N = int(input())
std = list(map(int, input().split()))
material = [0]*N
for i in range(N):
    material[i] = list(map(int, input().split()))

answer = []

def combination(material, comb, prot, fat, carbo, vit, price, num):
    if num == N:
        if (std[0] <= prot) and (std[1] <= fat) and (std[2] <= carbo) and (std[3] <= vit):
            answer.append([price, sorted(comb)])
            comb = []
        return
    else:
        combination(material, comb, prot, fat, carbo, vit, price, num+1)

        combination(material, comb+[num+1],
                    prot+material[num][0],
                    fat+material[num][1],
                    carbo+material[num][2],
                    vit+material[num][3],
                    price+material[num][4],
                    num+1)

combination(material, [], 0, 0, 0, 0, 0, 0)

if len(answer) == 0:
    print(-1)
else:
    answer = min(answer, key= lambda x : (x[0], x[1]))
    print(answer[0])
    for _ in answer[1]:
        print(_, end=" ")