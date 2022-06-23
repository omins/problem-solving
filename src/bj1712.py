a, b, c = map(int, input().split())  # 고정비, 가변비, 가격

if c <= b:
    print(-1)
    exit()

r = c - b  # 순수익
res = (a / r) + 1

print(int(res))
