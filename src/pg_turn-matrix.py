rows = 3
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
expectedAnswer = [1, 1, 5, 3]


def solution(rows, columns, queries):

    # 상, 우, 하, 좌
    dx = (-1, 0, 1, 0)
    dy = (0, 1, 0, -1)

    def turn(direction):
        direction = (direction + 1) % 4
        return direction

    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    answer = []

    # 1부터 rows*columns 까지의 수로 grid 초기화
    n = 1
    for i in range(rows):
        for j in range(columns):
            grid[i][j] = n
            n += 1

    for q in queries:
        direction = 1  # 상(0), 우(1), 하(2), 좌(3)

        # 언번들링, 제로베이스로 맞추기
        x1, y1, x2, y2 = q
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

        # 초기화
        start = (x1, y1)
        minValue = grid[x1][y1]
        prev = grid[x1][y1]
        tmp = 0
        x = x1
        y = y1

        while True:
            nx, ny = x + dx[direction], y + dy[direction]
            x = nx
            y = ny
            minValue = min(minValue, grid[nx][ny])

            # 이전 인덱스의 원소로 현재 인덱스 초기화
            tmp = grid[nx][ny]
            grid[nx][ny] = prev
            prev = tmp

            # 오른쪽 위, 오른쪽 아래, 왼쪽 아래 모서리일 때 회전
            if (nx, ny) == (x1, y2) or (nx, ny) == (x2, y2) or (nx, ny) == (x2, y1):
                direction = turn(direction)
            elif (nx, ny) == start:  # 시작지점으로 되돌아 왔을 때
                answer.append(minValue)
                break

    return answer


print(solution(rows, columns, queries))
