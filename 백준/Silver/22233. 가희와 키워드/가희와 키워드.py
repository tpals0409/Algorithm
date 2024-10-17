import sys
input = sys.stdin.readline

keyword_number, write_number = map(int, input().split())

keywords = dict()

for i in range(keyword_number):
    keyword = input().rstrip()
    keywords[keyword] = True

for j in range(write_number):
    words = list(input().rstrip().split(','))
    for k in words:
        if k in keywords:
            keywords.pop(k)
    print(len(keywords.keys()))