import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())

    dp = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

    if N > 10:
        dp += [0] * (N - 10)

        for i in range(11, N + 1):
            dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[N])
