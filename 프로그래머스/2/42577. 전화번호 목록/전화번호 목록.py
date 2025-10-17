def solution(phone_book):
    answer = True
    standard = set(phone_book)
    for i in range(len(phone_book)):
        for j in range(1, len(phone_book[i])):
            if phone_book[i][:j] in standard:
                answer = False
                break
    return answer