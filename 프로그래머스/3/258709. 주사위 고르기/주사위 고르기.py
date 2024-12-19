from itertools import product, combinations
def solution(dice):
    num_of_dice = [a for a in range(len(dice))]
    can = list(combinations(num_of_dice, len(dice)//2))
    combination_of_can = []
    answer = []
    can_length = (6**(len(dice)//2))**2
    
    for i in can:
        tmp1 = []
        tmp2 = dict()
        sorted_dice = []
        for j in i:
            tmp1.append(dice[j])
        
        for x in list(product(*tmp1)):
            if sum(x) in tmp2:
                tmp2[sum(x)] += 1
            else:
                tmp2[sum(x)] = 1
        tmp2['kind'] = i
        combination_of_can.append(tmp2)
        

    for p in range(len(combination_of_can)):
        count = 0
        numbers_A = list(combination_of_can[p].keys())
        numbers_A.pop()
        numbers_B = list(combination_of_can[-(p+1)].keys())
        numbers_B.pop()
        for q in numbers_A:
            for r in numbers_B:
                if q > r:
                    count += combination_of_can[p][q]*combination_of_can[-(p+1)][r]
        answer.append([combination_of_can[p]['kind'], count])
    answer = max(answer, key = lambda x: x[1])
    answer = list(answer[0])
    for last in range(len(answer)):
        answer[last] += 1
        
    return(answer)