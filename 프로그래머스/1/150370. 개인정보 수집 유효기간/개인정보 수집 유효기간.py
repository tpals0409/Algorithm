def solution(today, terms, privacies):
    answer = []
    cases = dict()
    today_y, today_m, today_d = map(int, today.split('.'))
    today_total = today_y*12*28 + today_m*28 + today_d  # 오늘 날짜 총 일수

    # 약관 유효기간 저장
    for case in terms:
        a, b = case.split()
        cases[a] = int(b)

    for i in range(len(privacies)):
        temp = privacies[i]
        start, person = temp.split()
        year, month, day = map(int, start.split('.'))

        # 유효기간 더하기
        month += cases[person]
        year += (month-1)//12
        month = (month-1)%12 + 1

        # 하루 빼기
        day -= 1
        if day == 0:
            month -= 1
            if month == 0:
                year -= 1
                month = 12
            day = 28

        expire_total = year*12*28 + month*28 + day  # 만료일 총 일수

        if today_total > expire_total:  # 오늘이 더 크면 만료
            answer.append(i+1)

    return answer
