def solution(genres, plays):
    answer = []
    songs = []
    for i in range(len(genres)):
        songs.append([plays[i], genres[i], i])
    
    dict_gen = dict()
    divid_gen = dict()
    
    for num, gen, i in songs:
        if gen in dict_gen:
            dict_gen[gen] += num
            divid_gen[gen].append([num, i])
        else:
            dict_gen[gen] = num
            divid_gen[gen] = [[num, i]]
    many_gen = sorted(dict_gen, key=dict_gen.get, reverse=True)
    
    for gen in divid_gen.keys():
        divid_gen[gen] = sorted(divid_gen[gen], key=lambda x: (-x[0], x[1]))
        
    for gen in many_gen:
        counter = 0
        for num, idx in divid_gen[gen]:
            counter += 1
            answer.append(idx)
            if counter == 2:
                break
    return answer