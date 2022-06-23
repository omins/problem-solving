import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
d = [1] * n

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))
