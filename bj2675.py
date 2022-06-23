t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    ns = ''
    for ch in s:
        ns += ch * r
    print(ns)
