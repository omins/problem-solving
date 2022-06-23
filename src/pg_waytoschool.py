from collections import deque

puddles = [[2, 2]]


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    dx = [1, 0]
    dy = [0, 1]

    for x, y in puddles:
        board[x-1][y-1] = -1

    q = deque([])
    q.append([0, 0])

    while q:
        x, y = q.popleft()
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if nx < n and ny < m:
                if board[nx][ny] != -1 and not visited[nx][ny]:
                    board[nx][ny] = board[x][y] + 1
                    q.append([nx, ny])
    print(board)
    answer = 0
    return answer


solution(4, 3, puddles)
