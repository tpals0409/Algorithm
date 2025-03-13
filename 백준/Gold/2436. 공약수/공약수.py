import math
A = 100000000
B = 100000000
GCD, LCM = map(int, input().split())
std = LCM//GCD
for i in range(1, int(std**0.5)+1):
    if std%i == 0:
        a = i
        b = std//i
        if math.gcd(a, b) == 1:
            if (a+b) < (A+B):
                A = a
                B = b
print(A*GCD, B*GCD)