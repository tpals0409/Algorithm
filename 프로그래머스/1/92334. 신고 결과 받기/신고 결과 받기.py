def solution(id_list, report, k):
    van = set()
    name = dict()
    for i in id_list:
        name[i] = set()
        
    for v in report:
        start, end = v.split()
        if start in name:
            name[start].add(end)
    
    tmp = []
    for n in name.keys():
        for v in name[n]:
            tmp.append(v)

    for i in id_list:
        is_vaned = tmp.count(i)
        if is_vaned >= k:
            van.add(i)
            
    answer = [0 for i in range(len(id_list))]
    for i in range(len(id_list)):
        for n in name[id_list[i]]:
            if n in van:
                answer[i] += 1
    return answer