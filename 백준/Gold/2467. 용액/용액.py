N = int(input())

liq = list(map(int, input().split()))

start = 0
end = N-1
abs_answer = float('inf')
answer = [0, 0]
while start != end:
    tmp = liq[start] + liq[end]
    if abs(tmp) < abs_answer:
        abs_answer = abs(tmp)
        answer = [start, end]
    if tmp >= 0:
        end -= 1
    else:
        start += 1

print(liq[answer[0]], liq[answer[1]])