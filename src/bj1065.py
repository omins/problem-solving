n = int(input())
cnt = 0

for i in range(1, n + 1):
    if i < 100:
        cnt += 1
        continue
    listI = list(map(int, str(i)))
    if listI[0] - listI[1] == listI[1] - listI[2]:
        cnt += 1
print(cnt)
