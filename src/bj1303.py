import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y, color):
    cnt = 0
    q = deque([])
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if f[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1

    return cnt + 1


m, n = map(int, input().split())
f = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]

white, blue = 0, 0

for i in range(n):
    for j in range(m):
        if f[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2
        elif f[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2

print(white, blue)
