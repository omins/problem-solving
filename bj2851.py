lst = [int(input()) for _ in range(10)]
res = 0

for i in range(len(lst)):
    res += lst[i]
    if res == 100:
        print(100)
        exit()
    if res > 100:
        cur = res
        prev = res - lst[i]
        if abs(100 - cur) < abs(100 - prev):
            print(cur)
            exit()
        elif abs(100 - cur) == abs(100 - prev):
            print(cur)
            exit()
        else:
            print(prev)
            exit()

print(res)
