import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
graph[0] = [0, 0]

visited = [False for _ in range(n+1)]

cnt = 0

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()


def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


for i in range(1, len(visited)):
    if not visited[i]:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)
