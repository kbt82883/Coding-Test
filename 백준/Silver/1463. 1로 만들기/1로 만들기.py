n = int(input())

dp = [0] * (n + 1)
if n >= 2:
    dp[2] = 1
    if n >= 3:
        dp[3] = 1

if n >= 4:
    for i in range(4, n + 1):
        dp[i] = float("inf")
        if i % 3 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 3])
        if i % 2 == 0:
            dp[i] = min(dp[i], 1 + dp[i // 2])

        dp[i] = min(dp[i], 1 + dp[i - 1])

print(dp[n])
