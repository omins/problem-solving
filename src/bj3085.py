n = int(input())
grid = [list(input()) for _ in range(n)]
dx = (1, 0)
dy = (0, 1)
maxScore = float('-Inf')


def getMaxScore(n, grid):
    score = float('-Inf')

    # 행의 최대 점수
    for i in range(n):
        cur = ''
        seq = 0
        for j in range(n):
            if cur == grid[i][j]:
                seq += 1
                score = max(score, seq)
            else:
                cur = grid[i][j]
                seq = 1
    # 열의 최대 점수
    for i in range(n):
        cur = ''
        seq = 0
        for j in range(n):
            if cur == grid[j][i]:
                seq += 1
                score = max(score, seq)
            else:
                cur = grid[j][i]
                seq = 1

    return score


for i in range(n):
    for j in range(n):
        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]
            if ni < n and nj < n:
                cur = grid[i][j]
                target = grid[ni][nj]

                # 인접한 두 사탕 바꾸기
                grid[i][j] = target
                grid[ni][nj] = cur

                # 바꾼 grid에서의 최대 점수
                maxScore = max(maxScore, getMaxScore(n, grid))

                # grid 원상 복구
                grid[i][j] = cur
                grid[ni][nj] = target

print(maxScore)
