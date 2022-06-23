n = int(input())
el = [list(map(int, input().split())) for _ in range(n)]
d = [1] * n

el.sort()

for i in range(n):
    for j in range(i):
        if el[i][1] > el[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))
