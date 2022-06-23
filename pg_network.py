from collections import deque


def bfs(start, computers, visited):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in range(len(computers)):
            if computers[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
    return 1  # bfs를 최대로 수행해도 결국 하나의 네트워크이기에 return 1


def solution(n, computers):
    visited = [False for _ in range(201)]
    answer = 0

    for i in range(n):
        if not visited[i]:  # 모든 컴퓨터를 돌다가 방문하지 않은 컴퓨터를 bfs
            answer += bfs(i, computers, visited)

    return answer


print(solution(3, computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
