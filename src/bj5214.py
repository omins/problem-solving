from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque()
    d[0] = 1  # 출발점
    q.append(0)

    while q:
        x = q.popleft()

        if x == n - 1:  # 목적지 도착
            print(d[x])
            return

            # 목적지가 아니면
        for nx in p[x]:
            if not d[nx]:
                if nx >= n:  # 하이퍼튜브이면
                    d[nx] = d[x]  # 이동횟수 세지 않음
                    q.append(nx)
                else:  # 역이면
                    d[nx] = d[x] + 1  # 이동횟수 + 1
                    q.append(nx)

    print(-1)  # 모두 방문했지만 도착하지 못한 경우


n, k, m = map(int, input().split())
p = [[] for _ in range(n + m)]
d = [0 for _ in range(n + m)]


# 역-하이퍼튜브-역 경로 저장
for i in range(m):
    t = list(map(int, input().split()))
    for j in range(k):
        p[t[j] - 1].append(n + i)
        p[n + i].append(t[j] - 1)

bfs()
