zero_one = str(input())
zero_count = zero_one.count('0')//2
one_count = zero_one.count('1')//2

tmp = ''
for i in zero_one: #문자열에서 앞에서 부터 0을 채움
    if i == '0':
        if zero_count > 0:
            tmp += i
            zero_count -= 1
    else:
        tmp += i

answer = ''
tmp = list(reversed(tmp)) # 0을 제거한 문자열에서 뒤에서부터 1을 빼기 위해 reverse함
for j in tmp:
    if j == '1':
        if one_count > 0:
            answer += j
            one_count -= 1
    else:
        answer += j
answer = list(reversed(answer)) #다시 reverse해서 원래 순서로 바꿈

for k in answer:
    print(k, end='')