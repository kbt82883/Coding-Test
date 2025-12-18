import sys

input = sys.stdin.readline


def dfs(idx):
    if idx == len(zeros):
        for row in grid:
            print(*row)
        sys.exit(0)

    r, c = zeros[idx]
    k = (r // 3) * 3 + c // 3
    for num in range(1, 10):
        if num not in rows[r] and num not in cols[c] and num not in boxes[k]:
            grid[r][c] = num
            rows[r].add(num)
            cols[c].add(num)
            boxes[k].add(num)

            dfs(idx + 1)

            grid[r][c] = 0
            rows[r].remove(num)
            cols[c].remove(num)
            boxes[k].remove(num)


grid = []
zeros = []
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
boxes = [set() for _ in range(9)]

for _ in range(9):
    grid.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if grid[i][j] == 0:
            zeros.append((i, j))
        else:
            rows[i].add(grid[i][j])
            cols[j].add(grid[i][j])
            boxes[(i // 3) * 3 + j // 3].add(grid[i][j])


dfs(0)
