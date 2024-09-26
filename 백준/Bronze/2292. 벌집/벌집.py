room = int(input())
answer = 0
std = 1
while True:
    if room <= std:
        break
    else:
        answer += 1
        std = std + (6 * answer)

print(answer+1)