from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
chk = [[False for _ in range(m)] for _ in range(n)]

dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)

q = deque()
q.append((0, 0))
chk[0][0] = True

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not chk[nx][ny]:
            board[nx][ny] = board[x][y] + 1
            chk[nx][ny] == True
            q.append((nx, ny))

print(board[n-1][m-1])
