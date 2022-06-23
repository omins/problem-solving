n = int(input())

d = [[0 for _ in range(10)] for _ in range(101)]

for i in range(1, 10):
    d[1][i] = 1

# 이전 자릿수에서 계산한 결과를 기준으로 현재 자릿수의 답을 구하기
for i in range(2, n+1):  # i == 자릿수
    for j in range(10):  # j == 뒤에 붙이는 수
        if j == 0:  # 0은 1에만 붙일 수 있음
            d[i][j] = d[i-1][1]
        elif j == 9:  # 9는 8에만 붙일 수 있음
            d[i][j] = d[i-1][8]
        else:  # 0과 9 이외의 수는 +- 1 한 자리 뒤에 모두 붙일 수 있음
            # 따라서 이전 자릿수(i-1)의 결과 중, 붙이려는 수(j)의 +- 1한 값을 더해 d[i][j]에 더한다.
            d[i][j] = d[i-1][j-1] + d[i-1][j+1]
print(sum(d[n]) % 1000000000)
