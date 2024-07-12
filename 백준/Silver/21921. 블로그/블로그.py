total_days, during_days = map(int, input().split())
records = list(map(int, input().split()))
start = sum(records[:during_days])
sum_records = [start]
for i in range(total_days-during_days):
    start = start-records[i]+records[during_days+i]
    sum_records.append(start)

max_sum = max(sum_records)

if max_sum == 0:
    print('SAD')
else:
    print(max_sum)
    print(sum_records.count(max_sum))