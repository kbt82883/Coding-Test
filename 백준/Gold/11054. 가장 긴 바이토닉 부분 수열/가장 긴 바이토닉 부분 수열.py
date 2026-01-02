import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

L = [1] * N
R = [1] * N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            L[i] = max(L[i], L[j] + 1)

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if lst[i] > lst[j]:
            R[i] = max(R[i], R[j] + 1)

ans = 0
for i in range(N):
    ans = max(ans, L[i] + R[i] - 1)
print(ans)
