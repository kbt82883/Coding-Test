import sys

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
pre = [[0] * N for _ in range(N)]
pre[0][0] = grid[0][0]

for i in range(N):
    for j in range(N):
        if i == 0 and j > 0:
            pre[i][j] = pre[i][j - 1] + grid[i][j]
        elif j == 0 and i > 0:
            pre[i][j] = pre[i - 1][j] + grid[i][j]
        elif i > 0 and j > 0:
            pre[i][j] = pre[i][j - 1] + pre[i - 1][j] + grid[i][j] - pre[i - 1][j - 1]

ans = -1
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        ans = pre[x2][y2]
    elif x1 > 0 and y1 == 0:
        ans = pre[x2][y2] - pre[x1 - 1][y2]
    elif y1 > 0 and x1 == 0:
        ans = pre[x2][y2] - pre[x2][y1 - 1]
    elif x1 > 0 and y1 > 0:
        ans = pre[x2][y2] - pre[x2][y1 - 1] - pre[x1 - 1][y2] + pre[x1 - 1][y1 - 1]
    print(ans)
