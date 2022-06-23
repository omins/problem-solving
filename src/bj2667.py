import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n = int(input())
board = [list(input().strip()) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
cnt = 0
cntList = []


def dfs(x, y):

    visited[x][y] = True
    _cnt = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == '1' and not visited[nx][ny]:
            _cnt += dfs(nx, ny)

    return _cnt


for i in range(n):
    for j in range(n):
        if board[i][j] == '1' and not visited[i][j]:
            cnt += 1
            cntList.append(dfs(i, j))

cntList.sort()
print(cnt)
for c in cntList:
    print(c)
