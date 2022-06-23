n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

d = [[0 for _ in range(i)] for i in range(1, len(triangle) + 1)]

d[0][0] = triangle[0][0]

for i in range(len(triangle) - 1):
    for j in range(len(triangle[i])):
        d[i+1][j] = max(d[i+1][j], triangle[i+1][j] + d[i][j])
        d[i+1][j+1] = max(d[i+1][j+1], triangle[i+1][j+1] + d[i][j])

print(max(d[n-1]))
