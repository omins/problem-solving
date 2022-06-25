from collections import deque

"""
주요 변수
1. 진행 방향
2. 몸 길이
3. 회전 방향
4. 회전 타이밍
5. 사과인지, 벽인지, 몸인지, 아무것도 없는지

첫 시작은 1초, 무언가를 만나는 시간이 종료 시간

순서
1. 맵 만들기
2. 사과 찍기
3. 시간-행동 매핑하기
4. 뱀 행동 구현하기
"""


def turnDirection(pol):
    global direction
    if pol == 'L':
        direction = (direction - 1) % 4  # (0 - 1) % 4 = 3
    else:
        direction = (direction + 1) % 4


n = int(input())
k = int(input())

# 지도 만들기
grid = [['*' for _ in range(n)] for _ in range(n)]

# 사과 찍기
for _ in range(k):
    x, y = map(int, input().split())
    grid[x-1][y-1] = 'a'

# 초-행동 매핑
policy = {}
l = int(input())
for _ in range(l):
    sec, pol = input().split()
    policy[int(sec)] = pol

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

# 초기화
direction = 1  # 상(0) 우(1) 하(2) 좌(3)
time = 1
snake = deque([[0, 0]])
x, y = 0, 0
grid[0][0] = 's'

# 뱀 이동
while True:
    # 상(0), 우(1), 하(2), 좌(3) 중에서 현재 direction 코드를 적용
    x, y = x + dx[direction], y + dy[direction]
    if 0 <= x < n and 0 <= y < n and grid[x][y] != 's':  # 벽 혹은 자신의 몸통이 아닐 때
        if not grid[x][y] == 'a':  # 사과가 아닐 때
            tailX, tailY = snake.popleft()  # 꼬리 자르기
            grid[tailX][tailY] = '*'
        grid[x][y] = 's'  # 뱀 전진
        snake.append((x, y))  # 뱀 머리 위치 추가
        if time in policy.keys():  # 정해진 동작이 있으면
            turnDirection(policy[time])
        time += 1
    else:  # 벽을 만났거나, 자신의 몸통을 만났을 때
        print(time)
        break
