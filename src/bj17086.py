from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안에 있고, 아기 상어가 아닐 때
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1:
                if board[nx][ny] != 0 and board[nx][ny] <= board[x][y] + 1:  # 다른 아기 상어와 더 가까울 때
                    continue
                else:
                    board[nx][ny] = board[x][y] + 1
                    q.append([nx, ny])


dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

q = deque([])

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 아기상어 위치 삽입
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append([i, j])

bfs()

res = 0
for i in range(n):
    res = max(res, max(board[i]))
print(res - 1)
