import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
rgCnt = 0
cnt = 0


def dfs(x, y, cur, isRg):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if isRg:
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if cur in ('R', 'G') and board[nx][ny] in ('R', 'G'):
                    visited[nx][ny] = True
                    dfs(nx, ny, board[nx][ny], True)
                elif board[nx][ny] == cur:
                    visited[nx][ny] = True
                    dfs(nx, ny, board[nx][ny], True)

        elif not isRg:
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == cur:
                visited[nx][ny] = True
                dfs(nx, ny, cur, False)


visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt += 1
            dfs(i, j, board[i][j], False)

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            rgCnt += 1
            dfs(i, j, board[i][j], True)

print(cnt)
print(rgCnt)
