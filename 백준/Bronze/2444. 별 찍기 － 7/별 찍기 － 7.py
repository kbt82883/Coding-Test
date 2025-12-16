n = int(input())

for i in range(n):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))

for j in range(n - 2, -1, -1):
    print(" " * (n - j - 1) + "*" * (2 * j + 1))
