n = int(input())


d = [0, 1, 2]


def fib(n):
    if n == 1:
        return d[1]
    elif n == 2:
        return d[2]
    for i in range(3, n + 1):
        num = (d[i - 1] + d[i - 2]) % 15746
        d.append(num)
    return d[n]


print(fib(n))
