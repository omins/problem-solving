num = set(range(1, 10001))
genetated_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    genetated_num.add(i)

self_num = sorted(num - genetated_num)

for n in self_num:
    print(n)
