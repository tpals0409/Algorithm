from math import ceil
def solution(fees, records):
    answer = []
    calc = dict()
    due = (23*60)+59
    for r in records:
        start, car, state = r.split()
        hour, minute = map(int, start.split(':'))
        start = (hour*60)+minute
        if car in calc:
            if calc[car][0] == False:
                calc[car] = [True, 0, calc[car][-1]+(start-calc[car][1])]
            else:
                calc[car] = [False, start, (calc[car][-1])]
        else:
            calc[car] = [False, start, 0]
        
    for car in calc.keys():
        if calc[car][0] == False:
            calc[car] = [True, due, calc[car][-1]+(due-calc[car][1])]
    
    answer = list(map(str, calc.keys()))
    answer = sorted(answer)
    calc_fees(fees, 100)
    for i in range(len(answer)):
        answer[i] = calc_fees(fees, calc[answer[i]][-1])
    return answer

def calc_fees(fees, time):
    fee = fees[1]
    time -= fees[0]
    if time <= 0:
        return fee
    else:
        fee += (fees[-1]*ceil(time/fees[2]))
    return fee