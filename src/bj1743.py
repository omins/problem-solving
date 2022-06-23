import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, k = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
cnt = 0

for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1


def dfs(x, y):

    visited[x][y] = True
    _cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
            _cnt += dfs(nx, ny)

    return _cnt


for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] == 1:
            cnt = max(cnt, dfs(i, j))

print(cnt)
