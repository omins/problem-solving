import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
graph = [[[0] for _ in range(N)] for _ in range(N)]
chk = [False] * N
res = 0


def dfs(n):
    for i in range(len(graph[n])):
        if graph[n][i] == 1 and not chk[i]:
            chk[i] = True
            dfs(i)


for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = graph[v][u] = 1

for i in range(N):
    if not chk[i]:
        dfs(i)
        res += 1

print(res)
