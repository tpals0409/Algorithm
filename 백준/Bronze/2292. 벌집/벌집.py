end = int(input())
start = 1
count = 1
while True:
    if end == 1:
        break
    start += (6*count)
    count += 1
    if start >= end:
        break

print(count)