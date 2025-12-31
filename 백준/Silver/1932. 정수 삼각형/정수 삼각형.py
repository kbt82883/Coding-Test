import sys

input = sys.stdin.readline

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0] = lst[0]

for i in range(1, N):
    for j in range(len(lst[i])):
        if j == 0:
            dp[i][j] = lst[i][j] + dp[i - 1][j]
        elif j == len(lst[i]) - 1:
            dp[i][j] = lst[i][j] + dp[i - 1][j - 1]
        else:
            dp[i][j] = lst[i][j] + max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[N - 1]))
