alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
from math import floor
def solution(str1, str2):
    dict1 = dict()
    dict2 = dict()
    for i in range(len(str1)-1):
        f,b = str1[i].lower(), str1[i+1].lower()
        if (f in alpha) and (b in alpha):
            if f+b in dict1:
                dict1[f+b] += 1
            else:
                dict1[f+b] = 1
    for i in range(len(str2)-1):
        f,b = str2[i].lower(), str2[i+1].lower()
        if (f in alpha) and (b in alpha):
            if f+b in dict2:
                dict2[f+b] += 1
            else:
                dict2[f+b] = 1
    check = dict2.copy()
    
    for a in dict1:
        if a in check:
            check[a] = max(0, check[a]-dict1[a])
            
    cross = sum(dict2.values())-sum(check.values())
    total = sum(dict2.values())+sum(dict1.values())-cross
    if total == 0:
        cross = 1
        total = 1
    answer = floor((cross/total)*65536)
    return answer