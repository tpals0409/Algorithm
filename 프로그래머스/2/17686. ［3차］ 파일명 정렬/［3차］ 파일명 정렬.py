num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
def solution(files):
    answer = []
    for f in files:
        start = 0
        end = len(f)
        for i in range(len(f)):
            if f[i] in num:
                start = i
                break
        for j in range(i, len(f)):
            if f[j] not in num:
                end = j
                break
        head = (f[:start])
        number = f[start:end]
        tail = f[end:]
        answer.append([head, number, tail])
    answer = sorted(answer, key=lambda x: (x[0].upper(), int(x[1])))
    
    for i in range(len(answer)):
        head, number, tail = answer[i]
        answer[i] = head+number+tail
    return answer