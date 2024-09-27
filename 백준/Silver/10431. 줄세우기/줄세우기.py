testcase = int(input())

for i in range(testcase):
    students = list(map(int, input().split()))
    number = students.pop(0)
    sorting = [0]
    answer = 0
    for student in students:
        start = 0
        while True:
            if student > sorting[start]:
                sorting.insert(start, student)
                answer += start
                break
            else:
                start += 1
    print(number, answer)