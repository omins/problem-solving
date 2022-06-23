from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append([nz, nx, ny])


m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]


q = deque([])
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

res = 0

# 1의 위치 삽입
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append([i, j, k])

bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit()
            res = max(res, box[i][j][k])

print(res - 1)
