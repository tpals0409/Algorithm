for _ in range(10):
    T = int(input())
    matrix = []
    idx = 0
    for i in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
        if i == 99:
            idx = row.index(2)
    
    # 방문 체크 배열 추가 - 핵심!
    visited = [[False] * 100 for _ in range(100)]
    
    def move_right(height, idx):
        while idx + 1 < 100 and matrix[height][idx + 1] == 1 and not visited[height][idx + 1]:
            idx += 1
            visited[height][idx] = True  # 방문 표시
        return idx
    
    def move_left(height, idx):
        while idx - 1 >= 0 and matrix[height][idx - 1] == 1 and not visited[height][idx - 1]:
            idx -= 1
            visited[height][idx] = True  # 방문 표시
        return idx
    
    visited[99][idx] = True  # 시작점 방문 표시
    
    for i in range(99, -1, -1):
        # 오른쪽 확인
        if idx + 1 < 100 and matrix[i][idx + 1] == 1 and not visited[i][idx + 1]:
            idx = move_right(i, idx)
        # 왼쪽 확인
        elif idx - 1 >= 0 and matrix[i][idx - 1] == 1 and not visited[i][idx - 1]:
            idx = move_left(i, idx)
        # 위로 이동할 때 다음 위치 방문 표시
        if i > 0:
            visited[i - 1][idx] = True
    
    print(f"#{_ + 1} {idx}")