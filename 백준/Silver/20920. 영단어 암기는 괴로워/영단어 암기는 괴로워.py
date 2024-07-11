import sys
words = dict()
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
answer = words.keys()
answer = sorted(answer, key= lambda x: (-words[x], -len(x), x))

for i in answer:
    print(i)