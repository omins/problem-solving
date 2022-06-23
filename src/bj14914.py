from math import gcd

a, b = map(int, input().split())
gcd_ = gcd(a, b)

for f in range(1, gcd_ // 2 + 1):
    if gcd_ % f == 0:
        print(f, a // f, b // f)

print(gcd_, a // gcd_, b // gcd_)
