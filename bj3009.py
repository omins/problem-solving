xLst = []
yLst = []

for i in range(3):
    x, y = map(int, input().split())
    xLst.append(x)
    yLst.append(y)

for j in range(3):
    if xLst.count(xLst[j]) == 1:
        x = xLst[j]
    if yLst.count(yLst[j]) == 1:
        y = yLst[j]

print(x, y)
