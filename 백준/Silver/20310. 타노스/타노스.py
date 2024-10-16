zero_one = str(input())
zero_count = zero_one.count('0')
one_count = zero_one.count('1')

for i in range(zero_count//2):
    print('0', end='')
for i in range(one_count//2):
    print('1', end='')