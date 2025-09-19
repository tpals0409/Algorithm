"""
123 123 (0, 0)(1, 0)(2, 0)
223 456 (0, 1)(1, 1)(2, 1)
333 789 (0, 2)(1, 2)(2, 2)
"""
def solution(n, left, right):
    answer = [max((i%n+1), (i//n+1)) for i in range(left, right+1)]
    return answer