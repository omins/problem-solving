n = int(input())
d_sum = 0

for i in range(1, n):  # 1부터 n까지
    lst = list(str(i))  # 자릿수 별 분할
    lst = list(map(int, lst))
    d_sum = i + sum(lst)  # 분해합 구하기

    if d_sum == n:
        print(i)  # i == 생성자
        break

if d_sum != n:
    print(0)
