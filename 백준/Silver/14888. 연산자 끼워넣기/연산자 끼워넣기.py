import sys

input = sys.stdin.readline


def dfs(idx, value):
    global maxv
    global minv
    if idx == N:
        maxv = max(maxv, value)
        minv = min(minv, value)
        return

    for i in range(4):
        if O[i] > 0:
            O[i] -= 1
            if i == 0:
                dfs(idx + 1, value + A[idx])
            elif i == 1:
                dfs(idx + 1, value - A[idx])
            elif i == 2:
                dfs(idx + 1, value * A[idx])
            elif i == 3:
                if value >= 0:
                    dfs(idx + 1, value // A[idx])
                else:
                    dfs(idx + 1, -(-value // A[idx]))

            O[i] += 1


N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))

maxv = float("-inf")
minv = float("inf")

dfs(1, A[0])

print(maxv)
print(minv)
