n = int(input())
number = [0]*1000001

for i in range(2, n+1):
    number[i] = number[i-1]+1
    if i%2 == 0:
        number[i] = min(number[i], number[i//2]+1)
    if i%3 == 0:
        number[i] = min(number[i], number[i//3]+1)
print(number[n])