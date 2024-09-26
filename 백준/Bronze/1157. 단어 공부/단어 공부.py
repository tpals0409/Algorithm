word = input()
word = word.upper()
count = dict()
for i in word:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

answer = []
number = []
for j in count:
    answer.append([j, count[j]])
    number.append(count[j])

answer = sorted(answer, key= lambda x : x[1], reverse=True)

if number.count(answer[0][1]) != 1:
    print('?')
else:
    print(answer[0][0])