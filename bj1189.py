import sys
sys.setrecursionlimit(10**6)
r, c, k = map(int, input().split())
board = [list(input()) for _ in range(r)]
dx = (1, -1, 0, 0)
dy = (0, 0, 1, -1)
_dict = {}


def dfs(x, y, d, visited):
    visited.append([x, y])
    if x == 0 and y == c - 1:
        if d in _dict:
            _dict[d] += 1
        else:
            _dict[d] = 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != 'T' and [nx, ny] not in visited:
            dfs(nx, ny, d + 1, visited + [[nx, ny]])


dfs(r-1, 0, 1, [])
print(_dict[k] if k in _dict else 0)
