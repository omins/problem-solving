# 노드의 갯수 + 1만큼 빈 []를 graph 리스트에 넣는다.
# 연결된 횟수만큼 반복하며 인풋을 a, b 스플릿으로 나누고
# graph[a]에 b를 추가한다
# 반복적으로 graph a를 정렬한다.

# 1번에서 bfs를 실행한다.
# 방문처리하고 cnt += 1한다
# 인접 노드를 탐색한다.
# 더 이상 인접 노드가 없는 경우 종료한다.

from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    global cnt

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True
                cnt += 1


n = int(input())
v = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()

cnt = 0
bfs(graph, 1, visited)
print(cnt)
