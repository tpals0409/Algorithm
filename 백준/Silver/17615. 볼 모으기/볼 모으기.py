import sys
input = sys.stdin.readline

N = int(input())
balls = input().rstrip()

def count_moves(color, direction):
    if direction == 'left':
        # 왼쪽부터 연속된 같은 색 건너뛰기
        i = 0
        while i < N and balls[i] == color:
            i += 1
        # 나머지 중에서 해당 색 개수 세기
        return balls[i:].count(color)
    else:  # right
        # 오른쪽부터 연속된 같은 색 건너뛰기
        i = N - 1
        while i >= 0 and balls[i] == color:
            i -= 1
        # 나머지 중에서 해당 색 개수 세기
        return balls[:i+1].count(color)

# 4가지 경우 모두 확인
answer = min(
    count_moves('R', 'left'),   # 빨강 왼쪽으로
    count_moves('R', 'right'),  # 빨강 오른쪽으로
    count_moves('B', 'left'),   # 파랑 왼쪽으로
    count_moves('B', 'right')   # 파랑 오른쪽으로
)

print(answer)