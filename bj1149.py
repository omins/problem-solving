n = int(input())
p = []

for _ in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):  # 1번 인덱스부터 이전 인덱스를 확인하며, 각 경로에서 도출할 수 있는 최솟값을 기록하며 진행
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]

print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))  # 마지막 인덱스에서 최솟값 출력
