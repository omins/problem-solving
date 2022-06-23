N = int(input())  # 1 <= N <= 10^6
cnt = 0

for i in range(1, N+1):  # 1부터 N까지
    while i > 0:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            cnt += 1
            i //= 10
        else:
            i //= 10

    # for j in range(len(str(i))):  # str(i)의 각 자릿수에 접근
    #     if str(i)[j] in ('3', '6', '9'):
    #         cnt += 1
print(cnt)
