def solution(sequence):
    max_plus = 0
    max_minus = 0
    start_plus = [0 for i in range(len(sequence))]
    start_minus = [0 for i in range(len(sequence))]
    for i in range(len(sequence)):
        if i%2 == 0:
            start_plus[i] = max(sequence[i], start_plus[i-1]+sequence[i])
            start_minus[i] = max(-sequence[i], start_minus[i-1]-sequence[i])
            
        else:
            start_plus[i] = max(-sequence[i], start_plus[i-1]-sequence[i])
            start_minus[i] = max(sequence[i], start_minus[i-1]+sequence[i])
        
        max_plus = max(max_plus, start_plus[i])
        max_minus = max(max_minus, start_minus[i])
    return max(max_plus, max_minus)