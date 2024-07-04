word = input()
word = word.upper()

alphabet = set(word)
count = [[alpha, 0] for alpha in alphabet]

for alpha in word:
    for i in range(len(count)):
        if alpha in count[i]:
            count[i][1] += 1

count = sorted(count, key= lambda x : x[1], reverse = True)
max_value = count[0][1]
answer = count[0][0]
for i in range(1, len(count)):
    if count[i][1] == max_value:
        answer = '?'
        break
    else:
        break

print(answer)