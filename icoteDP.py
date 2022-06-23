
n = int(input())
gar = list(map(int, input().split()))
d = [0] * 100

d[0] = gar[0]
d[1] = max(gar[0], gar[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + gar[i])

print(d[n-1])
