triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    if len(triangle) == 2:
        d[0][0] = triangle[0][0]
        d[1][0] = d[0][0] + triangle[1][0]
        d[1][1] = d[0][0] + triangle[1][1]
        return max(d[1][1], d[1][0])

    d = [[0 for _ in range(i)] for i in range(1, len(triangle) + 1)]

    d[0][0] = triangle[0][0]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])): # 이 부분을 떠올리지 못했음 (간단히 len(tri[i])하면 됨)
            d[i+1][j] = max(d[i+1][j], triangle[i+1][j] + d[i][j])
            d[i+1][j+1] = max(d[i+1][j+1], triangle[i+1][j+1] + d[i][j])
    answer = max(d[len(triangle)-1])
    return answer


print(solution(triangle))
