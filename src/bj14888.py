import sys
sys.setrecursionlimit(10**7)

n = int(input())
seq = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
_max = float('-Inf')
_min = float('Inf')


def dfs(_sum, _idx, _add, _sub, _mul, _div):
    global _max
    global _min

    if _idx == n:  # 끝까지 탐색했으면
        _max = max(_max, _sum)
        _min = min(_min, _sum)
        return

    if _add:
        dfs(_sum + seq[_idx], _idx + 1, _add - 1, _sub, _mul, _div)
    if _sub:
        dfs(_sum - seq[_idx], _idx + 1, _add, _sub - 1, _mul, _div)
    if _mul:
        dfs(_sum * seq[_idx], _idx + 1, _add, _sub, _mul - 1, _div)
    if _div:
        dfs(int(_sum / seq[_idx]), _idx + 1, _add, _sub, _mul, _div - 1)


dfs(seq[0], 1, add, sub, mul, div)

print(_max)
print(_min)
