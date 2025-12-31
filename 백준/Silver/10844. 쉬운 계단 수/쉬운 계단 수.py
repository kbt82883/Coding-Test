import sys

input = sys.stdin.readline

N = int(input())

dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for size in range(2, N + 1):
    for d in range(10):
        if d == 0:
            dp[size][d] = dp[size - 1][1]
        elif d == 9:
            dp[size][d] = dp[size - 1][8]
        else:
            dp[size][d] = (dp[size - 1][d - 1] + dp[size - 1][d + 1]) % 1000000000

print(sum(dp[N]) % 1000000000)
