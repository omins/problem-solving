from collections import deque

f, s, g, u, d = map(int, input().split())

# 0층부터 시작하는 것으로 맞추기
s -= 1
g -= 1

board = [0 for _ in range(f)]
visited = [False for _ in range(f)]

visited[s] = True
q = deque()
q.append(s)

while q:
    cur = q.popleft()

    if cur == g:
        print(board[cur])
        exit()

    nu = cur + u
    nd = cur - d

    if 0 <= nu < f and not visited[nu]:
        board[nu] = board[cur] + 1
        visited[nu] = True
        q.append(nu)

    if 0 <= nd < f and not visited[nd]:
        board[nd] = board[cur] + 1
        visited[nd] = True
        q.append(nd)

print('use the stairs')
