import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, m, k = map(int, input().split())
board = [[1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(n-ry, n-ly):  # 문제에서 주어지는 y좌표는 왼쪽 하단이 (0,0)
        for j in range(lx, rx):
            board[i][j] = 0  # 직사각형을 0으로 표시


dy = (1, -1, 0, 0)
dx = (0, 0, 1, -1)
cnt = 0
cntList = []


def dfs(y, x):
    visited[y][x] = True
    _cnt = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == 1 and not visited[ny][nx]:
            _cnt += dfs(y, x)

    return _cnt


for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            cntList.append(dfs(i, j))


cntList.sort()
print(cnt)
print(*cntList)
