def solution(user_id, banned_id):
    # 1. 패턴 매칭 함수
    def match(user, banned):
        if len(user) != len(banned):
            return False
        for i in range(len(user)):
            if banned[i] != '*' and user[i] != banned[i]:
                return False
        return True
    
    # 2. 각 banned_id에 매칭되는 user_id들 찾기
    candidates = []
    for banned in banned_id:
        matched = []
        for user in user_id:
            if match(user, banned):
                matched.append(user)
        candidates.append(matched)
    
    # 3. 백트래킹으로 모든 조합 찾기
    result = set()
    
    def backtrack(index, selected):
        if index == len(banned_id):
            # 정렬해서 튜플로 변환 (중복 제거용)
            result.add(tuple(sorted(selected)))
            return
        
        for user in candidates[index]:
            if user not in selected:
                backtrack(index + 1, selected + [user])
    
    backtrack(0, [])
    
    return len(result)