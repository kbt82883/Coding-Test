import sys
import math

input = sys.stdin.readline


def draw(x, y, size):
    if size == 1:
        grid[x][y] = "*"
        return

    n = size // 3
    draw(x, y, n)
    draw(x, y + n, n)
    draw(x, y + n + n, n)

    draw(x + n, y, n)
    draw(x + n, y + n + n, n)

    draw(x + n + n, y, n)
    draw(x + n + n, y + n, n)
    draw(x + n + n, y + n + n, n)


N = int(input())
grid = [[" "] * N for _ in range(N)]
draw(0, 0, N)
for i in range(N):
    for j in range(N):
        print(grid[i][j], end="")
    print()
