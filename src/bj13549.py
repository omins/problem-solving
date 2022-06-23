from collections import deque


def bfs():
    q = deque()
    q.append(n)
    lst[n] = 0

    while q:
        l = q.popleft()
        if l == k:
            return lst[k]
        for nl in (2 * l, l - 1, l + 1):
            if 0 <= nl < 100001 and lst[nl] == -1:
                if nl == 2*l:
                    lst[nl] = lst[l]
                    q.append(nl)
                elif nl == l - 1 or nl == l + 1:
                    lst[nl] = lst[l] + 1
                    q.append(nl)


n, k = map(int, input().split())
lst = [-1 for _ in range(100001)]

print(bfs())
