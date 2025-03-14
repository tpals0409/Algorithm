N, M = map(int, input().split())
arr = set()
answer = list()
def make_numbers(start, sequence):
    if len(sequence) == M:
        print(" ".join(map(str, sequence)))
        return 0
    for i in range(start, N+1):
        sequence.append(i)
        make_numbers(i+1, sequence)
        sequence.pop()

make_numbers(1, [])