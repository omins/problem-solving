from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, 1, -1, 2, 2, 1, -1]
dy = [1, -1, -2, -2, 1, -1, 2, 2]


def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])

    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            print(board[x][y])
            return
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < b and 0 <= ny < b and board[nx][ny] == 0:
                board[nx][ny] = board[x][y] + 1
                q.append([nx, ny])


t = int(input())
for _ in range(t):
    b = int(input())

    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if sx == ex and sy == ey:
        print(0)
        continue
    board = [[0] * b for _ in range(b)]
    bfs(sx, sy, ex, ey)
