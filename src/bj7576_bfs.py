from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque([])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0

# 1의 위치 삽입
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit()
    res = max(res, max(i))

print(res - 1)
