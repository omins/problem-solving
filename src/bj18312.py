n, k = map(int, input().split())
cnt = 0

for h in range(0, n + 1):
    for m in range(60):
        for s in range(60):
            time = ''
            if h < 10:
                time += '0' + str(h)
            else:
                time += str(h)
            if m < 10:
                time += '0' + str(m)
            else:
                time += str(m)
            if s < 10:
                time += '0' + str(s)
            else:
                time += str(s)
            if str(k) in time:
                cnt += 1
print(cnt)
