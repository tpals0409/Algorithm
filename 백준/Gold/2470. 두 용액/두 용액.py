N = int(input())
num = list(map(int, input().split()))
num = sorted(num)

answer = [float('inf'), [0, 0]]

for i in range(N):
    std = num[i]
    start = i + 1
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        current_sum = std + num[mid]
        
        # 현재 합의 절대값이 answer의 절대값보다 작으면 갱신
        if abs(current_sum) < answer[0]:
            answer = [abs(current_sum), [std, num[mid]]]
        
        # 현재 합이 0보다 작으면, 더 큰 값을 탐색하기 위해 start를 증가
        if current_sum < 0:
            start = mid + 1
        # 현재 합이 0보다 크면, 더 작은 값을 탐색하기 위해 end를 감소
        elif current_sum > 0:
            end = mid - 1
        # 현재 합이 0이면, 가장 가까운 값이므로 종료
        else:
            answer = [0, [std, num[mid]]]
            break

# 결과 출력 (작은 값 먼저 출력)
print(min(answer[1][0], answer[1][1]), max(answer[1][0], answer[1][1]))
