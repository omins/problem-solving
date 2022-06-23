n = int(input())
w = [int(input()) for _ in range(n)]
d = [0] * 10000

if n == 1:
    print(w[0])
elif n == 2:
    print(sum(w))
elif n == 3:
    print(max(w[0] + w[2], w[1] + w[2], w[0] + w[1]))
else:
    d[0] = w[0]
    d[1] = w[0] + w[1]
    d[2] = max(w[0] + w[2], w[1] + w[2], d[1])

    for i in range(3, n):
        d[i] = max(d[i-1], d[i-2] + w[i], d[i-3] + w[i-1] + w[i])
        # 이전까지 마신 양 고려 (현재 와인 안 마시기)
        # 전전 와인까지 마신 양 + 현재 와인 양
        # 전전전 와인까지 마신 양 + 이전 와인 + 현재 와인 양

    print(max(d))
