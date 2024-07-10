num_switch = int(input())
switch = [-1]*(num_switch+1)
switch[1:] = list(map(int, input().split()))

num_people = int(input())
for i in range(num_people):
    sex, num = map(int, input().split())
    if sex == 1:
        for i in range(1, num_switch+1):
            if i%num == 0:
                switch[i] = (switch[i]+1)%2
    else:
        count = 1
        switch[num] = (switch[num]+1)%2
        while True:
            if ((num+count) > num_switch) or ((num-count) < 1):
                break
            if switch[num+count] == switch[num-count]:
                switch[num+count] = (switch[num+count]+1)%2
                switch[num-count] = (switch[num-count]+1)%2
                count += 1
            else:
                break

for i in range(1, num_switch+1):
    print(switch[i], end = '')
    if i%20 == 0:
        print()
    else:
        print(' ', end='')