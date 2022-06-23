from itertools import combinations

lst = [int(input()) for _ in range(9)]
newLst = []

for combi in combinations(lst, 7):
    if sum(combi) == 100:
        newLst = list(combi)
        break

newLst.sort()

for n in newLst:
    print(n)
