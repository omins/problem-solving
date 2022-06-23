n = int(input())
seq = list(map(int, input().split()))

rev_seq = seq[::-1]
inc = [1 for _ in range(n)]
dec = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if seq[i] > seq[j]:
            inc[i] = max(inc[i], inc[j] + 1)
        if rev_seq[i] > rev_seq[j]:
            dec[i] = max(dec[i], dec[j] + 1)

res = [0 for _ in range(n)]

for i in range(n):
    res[i] = inc[i] + dec[n-i-1] - 1

print(max(res))
