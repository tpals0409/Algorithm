from collections import deque
def solution(participant, completion):
    answer = ''
    participant = deque(sorted(participant))
    completion = deque(sorted(completion))
    while completion:
        tmp1 = completion.popleft()
        tmp2 = participant.popleft()
        if tmp2 != tmp1:
            participant.append(tmp2)
            completion.appendleft(tmp1)
    answer = participant[0]
    return answer