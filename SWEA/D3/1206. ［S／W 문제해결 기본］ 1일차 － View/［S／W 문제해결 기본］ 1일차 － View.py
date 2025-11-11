for _ in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    max_height = max(buildings)
    now = 1
    count = 0
    while now <= max_height:
        for i in range(2, N-2):
            if buildings[i] >= now:
                if (buildings[i-2] < now and buildings[i-1] < now) and (buildings[i+1] < now and buildings[i+2] < now):
                    count += 1
        now += 1
    print(f"#{_+1} {count}")