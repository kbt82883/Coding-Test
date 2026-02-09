import sys

input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

sum_lst = [0]
for x in lst:
    sum_lst.append(sum_lst[-1] + x)

ans = float("-inf")
for i in range(N - K + 1):
    ans = max(ans, sum_lst[i + K] - sum_lst[i])

print(ans)
