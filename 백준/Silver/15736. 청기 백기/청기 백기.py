number = int(input())
count = 0
for i in range(1, number+1):
    if (i*i) <= number:
        count += 1
    else:
        break

print(count)