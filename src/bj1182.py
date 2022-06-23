n, s = map(int, input().split())
seq = list(map(int, input().split()))
cnt = 0


def recursion(idx, _sum):
    global cnt

    if idx == n:
        return

    _sum += seq[idx]

    if _sum == s:
        cnt += 1

    recursion(idx + 1, _sum)
    recursion(idx + 1, _sum - seq[idx])


recursion(0, 0)
print(cnt)
