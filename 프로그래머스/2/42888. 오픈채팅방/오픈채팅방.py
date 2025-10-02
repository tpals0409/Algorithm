def solution(record):
    answer = []
    nick_name = dict()
    lines = []
    
    for r in record:
        line = list(r.split())
        command = line[0]
        uid = line[1]
        if command == "Enter":
            nick_name[uid] = line[-1]
            lines.append([command, uid])
        elif command == "Change":
            nick_name[uid] = line[-1]
        else:
            lines.append([command, uid])
    
    for l in lines:
        command, uid = l
        if command == 'Enter':
            result = f"{nick_name[uid]}님이 들어왔습니다."
            answer.append(result)
        else:
            result = f"{nick_name[uid]}님이 나갔습니다."
            answer.append(result)

    return answer