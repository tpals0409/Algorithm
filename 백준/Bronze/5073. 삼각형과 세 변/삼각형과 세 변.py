while True:
    tri = list(map(int, input().split()))
    if (tri[0] == 0) and (tri[1] == 0) and (tri[2] == 0):
        break
    else:
        if max(tri) >= (sum(tri)-max(tri)):
            print('Invalid')
        else:
            tri = set(tri)
            if len(tri) == 1:
                print('Equilateral')
            elif len(tri) == 2:
                print('Isosceles')
            else:
                print('Scalene')
