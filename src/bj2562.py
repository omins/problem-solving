lst = [int(input()) for _ in range(9)]
res = float('-Inf')
idx = 0

for i in range(len(lst)):
    if lst[i] > res:
        res = lst[i]
        idx = i

print(res)
print(idx + 1)
