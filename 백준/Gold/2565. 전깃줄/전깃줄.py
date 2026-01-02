import sys

input = sys.stdin.readline

N = int(input())
lst = []

dp = [1] * N

for _ in range(N):
    a, b = map(int, input().split())
    lst.append((a, b))

lst.sort(key=lambda x: x[0])

for i in range(N):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
