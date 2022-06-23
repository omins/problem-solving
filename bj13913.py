# TODO

from collections import deque


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x]+1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            path(x)
            return x
        for i in (x + 1, x - 1, 2 * x):
            if 0 <= i < 100001 and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                # 이전 경로를 넣어주기
                move[i] = x


n, k = map(int, input().split())

dist = [0] * 100001
move = [0] * 100001

bfs()
