def solution(want, number, discount):
    answer = 0
    want_dict = {}
    
    # 원하는 제품과 수량을 딕셔너리로 저장
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    # 가능한 모든 10일 구간 확인
    for i in range(len(discount) - 9):
        tmp = want_dict.copy()
        
        # 해당 10일 구간의 할인 제품들 처리
        for j in range(i, i + 10):
            if discount[j] in tmp and tmp[discount[j]] > 0:
                tmp[discount[j]] -= 1
        
        # 모든 원하는 제품을 정확히 다 샀는지 확인
        if all(count == 0 for count in tmp.values()):
            answer += 1
    
    return answer