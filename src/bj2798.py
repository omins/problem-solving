from itertools import combinations
n, m = map(int, input().split())
card = list(map(int, input().split()))
res = 0
cnt = 0

for combi in combinations(card, 3):
    print(combi)
    if sum(combi) > m:
        continue
    else:
        res = max(res, sum(combi))

# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             if card[i] + card[j] + card[k] > m:
#                 continue
#             else:
#                 res = max(res, card[i] + card[j] + card[k])

print(res)
