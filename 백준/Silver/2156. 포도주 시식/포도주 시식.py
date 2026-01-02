import sys

input = sys.stdin.readline

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]

dp = [0] * (N + 1)

if N >= 1:
    dp[1] = lst[1]
if N >= 2:
    dp[2] = lst[1] + lst[2]

for i in range(3, N + 1):
    cost1 = dp[i - 3] + lst[i - 1] + lst[i]
    cost2 = dp[i - 2] + lst[i]
    cost3 = dp[i - 1]
    dp[i] = max(cost1, cost2, cost3)

print(dp[N])
