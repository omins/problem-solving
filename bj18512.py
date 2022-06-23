x, y, p1, p2 = map(int, input().split())
cnt = 1

found = False
xVisited = [p1]
yVisited = [p2]

while cnt < 10**5:
    p1 += x
    p2 += y
    xVisited.append(p1)
    yVisited.append(p2)

    if p1 in yVisited or p2 in xVisited:
        print(min(p1, p2))
        found = True
        break
    cnt += 1

if not found:
    print(-1)
