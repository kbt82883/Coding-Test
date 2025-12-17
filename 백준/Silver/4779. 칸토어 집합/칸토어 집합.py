import sys

input = sys.stdin.read


def cantor(n):
    if n == 1:
        return "-"
    if n == 3:
        return "- -"
    k = n // 3
    return cantor(k) + (" " * k) + cantor(k)


N = list(map(int, input().split()))
for i in N:
    print(cantor(3**i))
