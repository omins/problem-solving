from collections import deque

n = int(input())

# 이부분 긴가민가 함
dist = [[-1] * (n+1) for _ in range(n+1)]

q = deque()
q.append((1, 0))  # 처음 스티커, 클립보드 추가
dist[1][0] = 0  # 방문처리

while q:
    s, c = q.popleft()
    if dist[s][s] == -1:  # 클립보드에 복사
        dist[s][s] = dist[s][c] + 1
        q.append((s, s))
    if s + c <= n and dist[s + c][c] == -1:  # 붙여넣기
        dist[s + c][c] = dist[s][c] + 1
        q.append((s + c, c))
    if s - 1 >= 0 and dist[s - 1][c] == -1:  # 스티커 1개 삭제
        dist[s - 1][c] = dist[s][c] + 1
        q.append((s-1, c))

answer = -1

for i in range(n + 1):
    if dist[n][i] != -1:
        if answer == -1 or answer > dist[n][i]:
            answer = dist[n][i]

print(answer)
