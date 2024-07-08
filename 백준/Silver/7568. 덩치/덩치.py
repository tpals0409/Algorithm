N = int(input())
people = []
for _ in range(N):
    person = list(map(int, input().split()))
    people.append(person)


for i in range(N):
    answer = 1
    for j in range(N):
        if (people[i][0] < people[j][0]) and (people[i][1] < people[j][1]):
            answer += 1
    print(answer, end = ' ')