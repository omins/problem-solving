def fib_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib_arr = [0, 1]
    for i in range(2, n+1):
        num = fib_arr[i-1] + fib_arr[i - 2]
        fib_arr.append(num)
    return fib_arr[n]


print(fib_dp(int(input())))
