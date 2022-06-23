from math import lcm
from itertools import combinations

nums = list(map(int, input().split()))
lcms = []

for combi in combinations(nums, 3):
    a, b, c = combi
    lcm_ = lcm(lcm(a, b), c)
    lcms.append(lcm_)

print(min(lcms))
