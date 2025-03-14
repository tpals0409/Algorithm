student, num = map(int, input().split())
temp = list(map(int, input().split()))
answer = sum(temp[0:num])
window = answer

for i in range(num, student):
    window -= temp[i-num]
    window += temp[i]
    if window > answer:
        answer = window
print(answer)