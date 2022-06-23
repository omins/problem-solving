lst = [int(input()) for _ in range(10)]
s = set()

for n in lst:
    m = n % 42
    s.add(m)

print(len(s))
