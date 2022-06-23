# 8*8 블럭이 될 수 있는 모든 경우의 수에서
# min(res, 블록을 교체해야 하는 횟수)
# 각 원소에서 오른쪽으로 + 7, 아래로 + 7

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]

repair = []

for i in range(n-7):
    for j in range(m-7):
        w_first = 0
        b_first = 0

        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        w_first += 1
                    if board[k][l] != 'B':
                        b_first += 1
                else:
                    if board[k][l] != 'B':
                        w_first += 1
                    if board[k][l] != 'W':
                        b_first += 1
        repair.append(w_first)
        repair.append(b_first)

print(min(repair))
