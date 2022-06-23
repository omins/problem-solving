n = int(input())
sold = list(map(int, input().split()))

sold.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if sold[j] < sold[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
