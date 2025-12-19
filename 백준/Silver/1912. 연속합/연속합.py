import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))


cur = lst[0]
best = lst[0]

for i in range(1, n):
    cur = max(lst[i], cur + lst[i])
    best = max(best, cur)

print(best)
