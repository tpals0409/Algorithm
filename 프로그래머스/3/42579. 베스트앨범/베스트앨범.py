from collections import defaultdict
def solution(genres, plays):
    answer = []
    gen_dict = defaultdict(list)
    for i in range(len(genres)):
        gen_dict[genres[i]].append([plays[i], i])
    
    sum_gen = []
    for gen in gen_dict:
        total = 0
        for x1, x2 in gen_dict[gen]:
            total += x1
        sum_gen.append([gen, total])
    
    sorted_gen = sorted(sum_gen, key = lambda x: -x[-1])

    for gen, total in sorted_gen:
        tmp = gen_dict[gen]
        tmp = sorted(tmp, key = lambda x: (-x[0], x[1]))
        counter = 0
        for x0, x1 in tmp:
            counter += 1
            if counter > 2:
                break
            answer.append(x1)
    return answer