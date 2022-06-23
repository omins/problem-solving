t = int(input())

for _ in range(t):
    s = input()
    scr = 1
    tot = 0
    for ch in s:
        if ch == 'O':
            tot += scr
            scr += 1
        else:
            scr = 1
    print(tot)
